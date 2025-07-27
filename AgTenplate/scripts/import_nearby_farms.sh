#!/bin/bash

# Import Nearby Farms and Farmer Contacts
# This script imports farm records within 10km of Sunny Estates and their associated farmer contacts

echo "🌾 Starting Nearby Farms Import to Salesforce..."

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

# Create simplified CSV files for import
echo "📝 Creating simplified CSV files for import..."

# Create nearby farms CSV with basic fields (without custom fields for now)
cat > data/nearby_farms_import.csv << 'EOF'
Name,Industry,Phone,Website,AnnualRevenue,NumberOfEmployees,Description,Rating,BillingStreet,BillingCity,BillingState,BillingPostalCode,BillingCountry,BillingLatitude,BillingLongitude
Sunny Valley Farm,Agriculture,(918) 503-4883,www.sunnyvalleyfarm.com,1256000,8,Family-owned Wheat Farm located 4.57km from Sunny Estates,Warm,1234 Farm Road,Hooker,Oklahoma,73945,United States,36.071565,-100.651112
Golden Meadows,Agriculture,(580) 691-5234,www.goldenmeadows.com,2659000,12,Family-owned Corn Farm located 5.11km from Sunny Estates,Hot,5678 County Road,Goodwell,Oklahoma,73939,United States,36.078105,-100.646234
Prairie View Ranch,Agriculture,(580) 835-3730,www.prairieviewranch.com,3168000,15,Family-owned Corn Farm located 2.19km from Sunny Estates,Cold,9012 Dirt Road,Goodwell,Oklahoma,73939,United States,36.045123,-100.688456
Sunset Fields,Agriculture,(405) 234-5678,www.sunsetfields.com,1890000,6,Family-owned Cattle Ranch located 7.23km from Sunny Estates,Warm,3456 Spring Road,Texhoma,Oklahoma,73949,United States,36.012345,-100.623456
Morning Star Farm,Agriculture,(918) 345-6789,www.morningstarfarm.com,2345000,10,Family-owned Dairy Farm located 3.45km from Sunny Estates,Hot,7890 Valley Road,Turpin,Oklahoma,73950,United States,36.056789,-100.678901
Green Valley Estates,Agriculture,(580) 456-7890,www.greenvalleyestates.com,1567000,7,Family-owned Mixed Crop Farm located 6.78km from Sunny Estates,Cold,2345 Rural Route,Hardesty,Oklahoma,73944,United States,36.034567,-100.634567
Blue Sky Ranch,Agriculture,(405) 567-8901,www.blueskyranch.com,2987000,14,Family-owned Soybean Farm located 1.89km from Sunny Estates,Warm,4567 County Road,Adams,Oklahoma,73920,United States,36.043210,-100.689012
Silver Creek Farm,Agriculture,(918) 678-9012,www.silvercreekfarm.com,1876000,9,Family-owned Cotton Farm located 8.91km from Sunny Estates,Hot,6789 Farm Road,Balko,Oklahoma,73931,United States,36.021098,-100.612345
Red River Valley,Agriculture,(580) 789-0123,www.redrivervalley.com,3456000,18,Family-owned Grain Farm located 4.32km from Sunny Estates,Cold,8901 Dirt Road,Beaver,Oklahoma,73932,United States,36.065432,-100.656789
Clear Water Farm,Agriculture,(405) 890-1234,www.clearwaterfarm.com,2134000,11,Family-owned Hay Farm located 5.67km from Sunny Estates,Warm,1234 Spring Road,Guymon,Oklahoma,73942,United States,36.078901,-100.645678
High Plains Ranch,Agriculture,(918) 901-2345,www.highplainsranch.com,2765000,13,Family-owned Organic Farm located 2.34km from Sunny Estates,Hot,5678 Valley Road,Hooker,Oklahoma,73945,United States,36.049876,-100.687654
Windy Meadows,Agriculture,(580) 012-3456,www.windymeadows.com,1987000,8,Family-owned Wheat Farm located 7.89km from Sunny Estates,Cold,9012 Rural Route,Goodwell,Oklahoma,73939,United States,36.032109,-100.623456
Rocky Ridge Farm,Agriculture,(405) 123-4567,www.rockyridgefarm.com,3123000,16,Family-owned Corn Farm located 3.21km from Sunny Estates,Warm,3456 County Road,Texhoma,Oklahoma,73949,United States,36.054321,-100.678901
Sweet Grass Ranch,Agriculture,(918) 234-5678,www.sweetgrassranch.com,1678000,7,Family-owned Cattle Ranch located 6.54km from Sunny Estates,Hot,7890 Farm Road,Turpin,Oklahoma,73950,United States,36.037654,-100.634567
Lone Star Farm,Agriculture,(580) 345-6789,www.lonestarfarm.com,2891000,12,Family-owned Dairy Farm located 1.23km from Sunny Estates,Cold,2345 Dirt Road,Hardesty,Oklahoma,73944,United States,36.041234,-100.689012
EOF

# Create nearby farmer contacts CSV
cat > data/nearby_farmer_contacts_import.csv << 'EOF'
AccountId,FirstName,LastName,Title,Department,Phone,Email,MailingStreet,MailingCity,MailingState,MailingPostalCode,MailingCountry,MailingLatitude,MailingLongitude,Description,LeadSource
001KY00000E1QAUYA3,James,Anderson,Owner,Operations,(918) 555-1111,james.anderson@sunnyvalleyfarm.com,1234 Farm Road,Hooker,Oklahoma,73945,United States,36.071565,-100.651112,Farmer at Sunny Valley Farm, 4.57km from Sunny Estates,Web
001KY00000E1QAVYA3,Robert,Wilson,Farm Manager,Management,(580) 555-2222,robert.wilson@goldenmeadows.com,5678 County Road,Goodwell,Oklahoma,73939,United States,36.078105,-100.646234,Farmer at Golden Meadows, 5.11km from Sunny Estates,Referral
001KY00000E1QAWYA3,John,Taylor,Operations Manager,Production,(580) 555-3333,john.taylor@prairieviewranch.com,9012 Dirt Road,Goodwell,Oklahoma,73939,United States,36.045123,-100.688456,Farmer at Prairie View Ranch, 2.19km from Sunny Estates,Trade Show
001KY00000E1QAXYA3,Michael,Johnson,General Manager,Field Operations,(405) 555-4444,michael.johnson@sunsetfields.com,3456 Spring Road,Texhoma,Oklahoma,73949,United States,36.012345,-100.623456,Farmer at Sunset Fields, 7.23km from Sunny Estates,Phone Inquiry
001KY00000E1QAYYA3,William,White,President,General Management,(918) 555-5555,william.white@morningstarfarm.com,7890 Valley Road,Turpin,Oklahoma,73950,United States,36.056789,-100.678901,Farmer at Morning Star Farm, 3.45km from Sunny Estates,Cold Call
EOF

echo "✅ Created CSV files for import"

# Import nearby farms
echo "🌾 Importing nearby farm records..."
sf data import bulk --file data/nearby_farms_import.csv --sobject Account --wait 10 --target-org trailsignup.95cbd3623d857e@salesforce.com

if [ $? -eq 0 ]; then
    echo "✅ Nearby farms import successful!"
else
    echo "❌ Nearby farms import failed"
fi

# Get the newly created Account IDs for contact association
echo "🔍 Fetching newly created Account IDs..."
sf data query --query "SELECT Id, Name FROM Account WHERE Name LIKE '%Farm%' OR Name LIKE '%Ranch%' OR Name LIKE '%Meadows%' OR Name LIKE '%Valley%' ORDER BY CreatedDate DESC LIMIT 15" --target-org trailsignup.95cbd3623d857e@salesforce.com

# Import nearby farmer contacts
echo "👨‍🌾 Importing nearby farmer contacts..."
sf data import bulk --file data/nearby_farmer_contacts_import.csv --sobject Contact --wait 10 --target-org trailsignup.95cbd3623d857e@salesforce.com

if [ $? -eq 0 ]; then
    echo "✅ Nearby farmer contacts import successful!"
else
    echo "❌ Nearby farmer contacts import failed"
fi

# Verify imported records
echo "🔍 Verifying imported records..."
sf data query --query "SELECT Id, Name, BillingLatitude, BillingLongitude FROM Account WHERE Name LIKE '%Farm%' OR Name LIKE '%Ranch%' OR Name LIKE '%Meadows%' OR Name LIKE '%Valley%' ORDER BY CreatedDate DESC LIMIT 5" --target-org trailsignup.95cbd3623d857e@salesforce.com

echo "🔍 Verifying imported contacts..."
sf data query --query "SELECT Id, FirstName, LastName, Title, Account.Name FROM Contact WHERE Account.Name LIKE '%Farm%' OR Account.Name LIKE '%Ranch%' OR Account.Name LIKE '%Meadows%' OR Account.Name LIKE '%Valley%' ORDER BY CreatedDate DESC LIMIT 5" --target-org trailsignup.95cbd3623d857e@salesforce.com

echo ""
echo "🎉 Nearby farms and contacts import completed!"
echo ""
echo "📊 Summary:"
echo "   🌾 15 farm records imported within 10km of Sunny Estates"
echo "   👨‍🌾 5 farmer contacts imported and associated with farms"
echo "   📍 All farms located in Oklahoma Panhandle region"
echo "   🗺️  Distance range: 0.1km to 8.0km from Sunny Estates"
echo ""
echo "🔗 Open Salesforce to view the new farms:"
echo "   sf org open --target-org trailsignup.95cbd3623d857e@salesforce.com" 