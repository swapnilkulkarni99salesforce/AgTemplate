/**
 * Apex controller for the Account Radar Lightning Web Component
 * Provides methods to find nearby accounts based on geolocation
 */
public with sharing class AccountRadarController {
    
    /**
     * Inner class to represent an account with distance information
     */
    public class AccountWithDistance {
        @AuraEnabled
        public String Id { get; set; }
        @AuraEnabled
        public String Name { get; set; }
        @AuraEnabled
        public String Type { get; set; }
        @AuraEnabled
        public String Phone { get; set; }
        @AuraEnabled
        public Decimal BillingLatitude { get; set; }
        @AuraEnabled
        public Decimal BillingLongitude { get; set; }
        @AuraEnabled
        public Address BillingAddress { get; set; }
        @AuraEnabled
        public Decimal distance { get; set; }
        
        public AccountWithDistance(Account acc, Decimal dist) {
            this.Id = acc.Id;
            this.Name = acc.Name;
            this.Type = acc.Type;
            this.Phone = acc.Phone;
            this.BillingLatitude = acc.BillingLatitude;
            this.BillingLongitude = acc.BillingLongitude;
            this.BillingAddress = acc.BillingAddress;
            this.distance = dist;
        }
    }
    
    /**
     * Get nearby accounts within the specified radius
     * @param currentAccountId The ID of the current account
     * @param latitude The latitude of the current account
     * @param longitude The longitude of the current account
     * @param radiusKm The search radius in kilometers
     * @return List of nearby accounts with distance information
     */
    @AuraEnabled(cacheable=true)
    public static List<AccountWithDistance> getNearbyAccounts(
        String currentAccountId, 
        Decimal latitude, 
        Decimal longitude, 
        Integer radiusKm
    ) {
        try {
            // Validate input parameters
            if (String.isBlank(currentAccountId) || latitude == null || longitude == null || radiusKm == null) {
                throw new AuraHandledException('Missing required parameters');
            }
            
            if (radiusKm <= 0 || radiusKm > 500) {
                throw new AuraHandledException('Radius must be between 1 and 500 kilometers');
            }
            
            // Calculate approximate latitude and longitude bounds for the search
            // This is a rough approximation to limit the SOQL query results
            Decimal latitudeDelta = radiusKm / 111.0; // Approximately 111 km per degree of latitude
            Decimal longitudeDelta = radiusKm / (111.0 * Math.cos((latitude.doubleValue() * Math.PI) / 180));
            
            Decimal minLatitude = latitude - latitudeDelta;
            Decimal maxLatitude = latitude + latitudeDelta;
            Decimal minLongitude = longitude - longitudeDelta;
            Decimal maxLongitude = longitude + longitudeDelta;
            
            // Query accounts within the approximate bounds
            List<Account> candidateAccounts = [
                SELECT Id, Name, BillingLatitude, BillingLongitude,Type,Phone,BillingAddress
                FROM Account
                WHERE Id != :currentAccountId
                AND BillingLatitude != null
                AND BillingLongitude != null
                AND BillingLatitude >= :minLatitude
                AND BillingLatitude <= :maxLatitude
                AND BillingLongitude >= :minLongitude
                AND BillingLongitude <= :maxLongitude
                LIMIT 200
            ];
            
            List<AccountWithDistance> nearbyAccounts = new List<AccountWithDistance>();
            
            // Calculate exact distances and filter by radius
            for (Account acc : candidateAccounts) {
                Decimal distance = calculateDistance(
                    latitude, longitude, 
                    acc.BillingLatitude, acc.BillingLongitude
                );
                
                if (distance <= radiusKm) {
                    nearbyAccounts.add(new AccountWithDistance(acc, distance));
                }
            }
            
            // Sort by distance (closest first)
            nearbyAccounts.sort(new DistanceComparator());
            
            // Limit to 50 results for performance
            if (nearbyAccounts.size() > 50) {
                List<AccountWithDistance> limitedAccounts = new List<AccountWithDistance>();
                for (Integer i = 0; i < 50; i++) {
                    limitedAccounts.add(nearbyAccounts[i]);
                }
                nearbyAccounts = limitedAccounts;
            }
            
            return nearbyAccounts;
            
        } catch (Exception e) {
            throw new AuraHandledException('Error retrieving nearby accounts: ' + e.getMessage());
        }
    }
    
    /**
     * Calculate the distance between two points using the Haversine formula
     * @param lat1 Latitude of first point
     * @param lon1 Longitude of first point
     * @param lat2 Latitude of second point
     * @param lon2 Longitude of second point
     * @return Distance in kilometers
     */
    private static Decimal calculateDistance(Decimal lat1, Decimal lon1, Decimal lat2, Decimal lon2) {
        if (lat1 == null || lon1 == null || lat2 == null || lon2 == null) {
            return null;
        }
        
        Double earthRadius = 6371; // Earth's radius in kilometers
        
        Double dLat = ((lat2 - lat1).doubleValue() * Math.PI) / 180;
        Double dLon = ((lon2 - lon1).doubleValue() * Math.PI) / 180;
        
        Double a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
                   Math.cos((lat1.doubleValue() * Math.PI) / 180) * 
                   Math.cos((lat2.doubleValue() * Math.PI) / 180) *
                   Math.sin(dLon / 2) * Math.sin(dLon / 2);
        
        Double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        Double distance = earthRadius * c;
        
        return Decimal.valueOf(distance);
    }
    
    /**
     * Comparator class to sort accounts by distance
     */
    private class DistanceComparator implements Comparator<AccountWithDistance> {
        public Integer compare(AccountWithDistance a1, AccountWithDistance a2) {
            if (a1.distance == a2.distance) {
                return 0;
            } else if (a1.distance > a2.distance) {
                return 1;
            } else {
                return -1;
            }
        }
    }
    
    /**
     * Get accounts with addresses for map display
     * @param accountIds Optional list of specific account IDs to retrieve
     * @return List of accounts with address information
     */
    @AuraEnabled(cacheable=true)
    public static List<Account> getAccountsWithAddresses(List<String> accountIds) {
        try {
            String query = 'SELECT Id, Name, Type, Phone, BillingStreet, BillingCity, BillingState, ' +
                          'BillingPostalCode, BillingCountry, BillingLatitude, BillingLongitude, ' +
                          'BillingAddress ' +
                          'FROM Account ' +
                          'WHERE BillingLatitude != null AND BillingLongitude != null';
            
            if (accountIds != null && !accountIds.isEmpty()) {
                query += ' AND Id IN :accountIds';
            }
            
            query += ' ORDER BY Name LIMIT 1000';
            
            List<Account> accounts = Database.query(query);
            
            return accounts;
            
        } catch (Exception e) {
            throw new AuraHandledException('Error retrieving accounts: ' + e.getMessage());
        }
    }
    
    /**
     * Get nearby accounts based on user's current location
     * @param userLatitude The user's current latitude
     * @param userLongitude The user's current longitude
     * @param radiusKm The search radius in kilometers (default 50km)
     * @return List of nearby accounts with distance information
     */
    @AuraEnabled(cacheable=true)
    public static List<AccountWithDistance> getNearbyAccountsByLocation(
        Decimal userLatitude, 
        Decimal userLongitude, 
        Integer radiusKm
    ) {
        try {
            // Validate input parameters
            if (userLatitude == null || userLongitude == null) {
                throw new AuraHandledException('User location coordinates are required');
            }
            
            if (radiusKm == null || radiusKm <= 0 || radiusKm > 500) {
                radiusKm = 50; // Default to 50km if invalid
            }
            
            // Calculate approximate latitude and longitude bounds for the search
            Decimal latitudeDelta = radiusKm / 111.0; // Approximately 111 km per degree of latitude
            Decimal longitudeDelta = radiusKm / (111.0 * Math.cos((userLatitude.doubleValue() * Math.PI) / 180));
            
            Decimal minLatitude = userLatitude - latitudeDelta;
            Decimal maxLatitude = userLatitude + latitudeDelta;
            Decimal minLongitude = userLongitude - longitudeDelta;
            Decimal maxLongitude = userLongitude + longitudeDelta;
            
            // Query accounts within the approximate bounds
            List<Account> candidateAccounts = [
                SELECT Id, Name, Type, Phone, BillingStreet, BillingCity, BillingState,
                       BillingPostalCode, BillingCountry, BillingLatitude, BillingLongitude,
                       BillingAddress
                FROM Account
                WHERE BillingLatitude != null
                AND BillingLongitude != null
                AND BillingLatitude >= :minLatitude
                AND BillingLatitude <= :maxLatitude
                AND BillingLongitude >= :minLongitude
                AND BillingLongitude <= :maxLongitude
                LIMIT 200
            ];
            
            List<AccountWithDistance> nearbyAccounts = new List<AccountWithDistance>();
            
            // Calculate exact distances and filter by radius
            for (Account acc : candidateAccounts) {
                Decimal distance = calculateDistance(
                    userLatitude, userLongitude, 
                    acc.BillingLatitude, acc.BillingLongitude
                );
                
                if (distance <= radiusKm) {
                    AccountWithDistance accountWithDistance = new AccountWithDistance(acc, distance);
                    // Add additional fields that weren't in the original AccountWithDistance class
                    accountWithDistance.Type = acc.Type;
                    accountWithDistance.Phone = acc.Phone;
                    accountWithDistance.BillingAddress = acc.BillingAddress;
                    nearbyAccounts.add(accountWithDistance);
                }
            }
            
            // Sort by distance (closest first)
            nearbyAccounts.sort(new DistanceComparator());
            
            // Limit to 50 results for performance
            if (nearbyAccounts.size() > 50) {
                List<AccountWithDistance> limitedAccounts = new List<AccountWithDistance>();
                for (Integer i = 0; i < 50; i++) {
                    limitedAccounts.add(nearbyAccounts[i]);
                }
                nearbyAccounts = limitedAccounts;
            }
            
            return nearbyAccounts;
            
        } catch (Exception e) {
            throw new AuraHandledException('Error retrieving nearby accounts: ' + e.getMessage());
        }
    }
} 