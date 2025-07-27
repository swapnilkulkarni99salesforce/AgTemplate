/**
 * Copy Billing Address to Shipping Address for All Accounts
 * This script copies all billing address fields to shipping address fields
 * including longitude and latitude coordinates
 */

// Query all accounts with billing address information
List<Account> accountsToUpdate = [
    SELECT Id, Name,
           BillingStreet, BillingCity, BillingState, BillingPostalCode, BillingCountry,
           BillingLatitude, BillingLongitude,
           ShippingStreet, ShippingCity, ShippingState, ShippingPostalCode, ShippingCountry,
           ShippingLatitude, ShippingLongitude
    FROM Account
    WHERE BillingStreet != null 
    AND BillingCity != null
];

System.debug('Found ' + accountsToUpdate.size() + ' accounts with billing addresses to update');

// Counter for tracking
Integer updatedCount = 0;
Integer skippedCount = 0;

// Process each account
for(Account acc : accountsToUpdate) {
    Boolean hasChanges = false;
    
    // Copy billing address to shipping address
    if(acc.BillingStreet != acc.ShippingStreet) {
        acc.ShippingStreet = acc.BillingStreet;
        hasChanges = true;
    }
    
    if(acc.BillingCity != acc.ShippingCity) {
        acc.ShippingCity = acc.BillingCity;
        hasChanges = true;
    }
    
    if(acc.BillingState != acc.ShippingState) {
        acc.ShippingState = acc.BillingState;
        hasChanges = true;
    }
    
    if(acc.BillingPostalCode != acc.ShippingPostalCode) {
        acc.ShippingPostalCode = acc.BillingPostalCode;
        hasChanges = true;
    }
    
    if(acc.BillingCountry != acc.ShippingCountry) {
        acc.ShippingCountry = acc.BillingCountry;
        hasChanges = true;
    }
    
    // Copy latitude and longitude
    if(acc.BillingLatitude != acc.ShippingLatitude) {
        acc.ShippingLatitude = acc.BillingLatitude;
        hasChanges = true;
    }
    
    if(acc.BillingLongitude != acc.ShippingLongitude) {
        acc.ShippingLongitude = acc.BillingLongitude;
        hasChanges = true;
    }
    
    if(hasChanges) {
        updatedCount++;
        System.debug('Updating shipping address for: ' + acc.Name);
    } else {
        skippedCount++;
        System.debug('No changes needed for: ' + acc.Name);
    }
}

// Update accounts in batches to avoid governor limits
if(!accountsToUpdate.isEmpty()) {
    try {
        update accountsToUpdate;
        System.debug('✅ Successfully updated ' + updatedCount + ' accounts');
        System.debug('⏭️  Skipped ' + skippedCount + ' accounts (no changes needed)');
        System.debug('📊 Total accounts processed: ' + accountsToUpdate.size());
        
        // Display summary
        System.debug('=== ADDRESS COPY SUMMARY ===');
        System.debug('🏢 Accounts with billing addresses: ' + accountsToUpdate.size());
        System.debug('✅ Accounts updated: ' + updatedCount);
        System.debug('⏭️  Accounts skipped: ' + skippedCount);
        System.debug('📍 Fields copied: Street, City, State, Postal Code, Country, Latitude, Longitude');
        
    } catch(Exception e) {
        System.debug('❌ Error updating accounts: ' + e.getMessage());
        System.debug('Stack trace: ' + e.getStackTraceString());
    }
} else {
    System.debug('ℹ️  No accounts found with billing addresses to copy');
}

// Optional: Query and display sample results
List<Account> sampleResults = [
    SELECT Id, Name, 
           BillingStreet, BillingCity, BillingState,
           ShippingStreet, ShippingCity, ShippingState,
           BillingLatitude, BillingLongitude,
           ShippingLatitude, ShippingLongitude
    FROM Account 
    WHERE ShippingStreet != null 
    LIMIT 5
];

System.debug('=== SAMPLE RESULTS ===');
for(Account acc : sampleResults) {
    System.debug('Account: ' + acc.Name);
    System.debug('  Billing: ' + acc.BillingStreet + ', ' + acc.BillingCity + ', ' + acc.BillingState);
    System.debug('  Shipping: ' + acc.ShippingStreet + ', ' + acc.ShippingCity + ', ' + acc.ShippingState);
    System.debug('  Billing Coords: ' + acc.BillingLatitude + ', ' + acc.BillingLongitude);
    System.debug('  Shipping Coords: ' + acc.ShippingLatitude + ', ' + acc.ShippingLongitude);
    System.debug('---');
} 