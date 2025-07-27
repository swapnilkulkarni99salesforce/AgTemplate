#!/bin/bash

# Run Address Copy Apex Script
# This script executes the Apex code to copy billing addresses to shipping addresses

echo "🚀 Running Address Copy Script in Salesforce..."

# Check if Salesforce CLI is installed
if ! command -v sf &> /dev/null; then
    echo "❌ Salesforce CLI is not installed. Please install it first."
    echo "   Visit: https://developer.salesforce.com/tools/sfdxcli"
    exit 1
fi

# Check if we're authenticated to a Salesforce org
if ! sf org display &> /dev/null; then
    echo "❌ Not authenticated to a Salesforce org."
    echo "   Please run: sf org login web"
    exit 1
fi

echo "✅ Salesforce CLI found and authenticated"

# Create a temporary Apex file for execution
echo "📝 Creating temporary Apex execution file..."

cat > temp_address_copy.apex << 'EOF'
// Execute the address copy logic
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

Integer updatedCount = 0;
Integer skippedCount = 0;

for(Account acc : accountsToUpdate) {
    Boolean hasChanges = false;
    
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

if(!accountsToUpdate.isEmpty()) {
    try {
        update accountsToUpdate;
        System.debug('✅ Successfully updated ' + updatedCount + ' accounts');
        System.debug('⏭️  Skipped ' + skippedCount + ' accounts (no changes needed)');
        System.debug('📊 Total accounts processed: ' + accountsToUpdate.size());
        
        System.debug('=== ADDRESS COPY SUMMARY ===');
        System.debug('🏢 Accounts with billing addresses: ' + accountsToUpdate.size());
        System.debug('✅ Accounts updated: ' + updatedCount);
        System.debug('⏭️  Accounts skipped: ' + skippedCount);
        System.debug('📍 Fields copied: Street, City, State, Postal Code, Country, Latitude, Longitude');
        
    } catch(Exception e) {
        System.debug('❌ Error updating accounts: ' + e.getMessage());
    }
} else {
    System.debug('ℹ️  No accounts found with billing addresses to copy');
}

// Display sample results
List<Account> sampleResults = [
    SELECT Id, Name, 
           BillingStreet, BillingCity, BillingState,
           ShippingStreet, ShippingCity, ShippingState,
           BillingLatitude, BillingLongitude,
           ShippingLatitude, ShippingLongitude
    FROM Account 
    WHERE ShippingStreet != null 
    LIMIT 3
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
EOF

echo "✅ Created temporary Apex file"

# Execute the Apex code
echo "🔧 Executing Apex code in Salesforce..."
sf apex run --file temp_address_copy.apex --target-org trailsignup.95cbd3623d857e@salesforce.com

# Clean up temporary file
rm temp_address_copy.apex

echo ""
echo "🎉 Address copy script execution completed!"
echo ""
echo "📊 To verify results, run:"
echo "   sf data query --query \"SELECT Id, Name, BillingStreet, ShippingStreet, BillingLatitude, ShippingLatitude FROM Account WHERE ShippingStreet != null LIMIT 5\" --target-org trailsignup.95cbd3623d857e@salesforce.com"
echo ""
echo "🔗 Open Salesforce to view updated accounts:"
echo "   sf org open --target-org trailsignup.95cbd3623d857e@salesforce.com" 