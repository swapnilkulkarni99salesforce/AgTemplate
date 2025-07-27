#!/bin/bash

# Import Contacts to Salesforce
# This script imports farmer and distributor contacts with proper Account ID mapping

echo "👥 Starting Contact Import to Salesforce..."

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

# Get Account IDs from Salesforce
echo "🔍 Fetching Account IDs from Salesforce..."
sf data query --query "SELECT Id, Name FROM Account WHERE Industry = 'Agriculture'" --target-org trailsignup.95cbd3623d857e@salesforce.com --result-format csv > temp_accounts.csv

# Create simplified contact CSV files for import
echo "📝 Creating contact CSV files for import..."

# Create farmer contacts CSV with basic fields
cat > data/farmer_contacts_import.csv << 'EOF'
AccountId,FirstName,LastName,Title,Department,Phone,Email,MailingStreet,MailingCity,MailingState,MailingPostalCode,MailingCountry,MailingLatitude,MailingLongitude,Description,LeadSource,Status
001KY00000E1QAUYA3,John,Smith,Farm Manager,Operations,(319) 555-1234,john.smith@farm.com,1234 Farm Road,Rural City 1,California,12345,United States,32.842615,-116.001191,Experienced farmer with over 20 years in agriculture,Web,Active
001KY00000E1QAVYA3,Robert,Johnson,Owner,Management,(515) 555-2345,robert.johnson@ranch.com,5678 County Road,Rural City 2,North Dakota,23456,United States,46.106709,-95.661649,Multi-generational farmer specializing in sustainable practices,Referral,Active
001KY00000E1QAWYA3,Michael,Williams,Operations Manager,Production,(641) 555-3456,michael.williams@farm.com,9012 Dirt Road,Rural City 3,Illinois,34567,United States,42.427891,-94.680722,Farm owner with expertise in modern farming techniques,Trade Show,Active
001KY00000E1QAXYA3,William,Brown,General Manager,Field Operations,(712) 555-4567,william.brown@produce.com,3456 Spring Road,Rural City 4,South Dakota,45678,United States,43.4139,-89.473606,Agricultural professional with focus on crop management,Phone Inquiry,Active
001KY00000E1QAYYA3,David,Jones,President,General Management,(563) 555-5678,david.jones@farm.com,7890 Valley Road,Rural City 5,Texas,56789,United States,35.364239,-101.876507,Seasoned farmer with deep knowledge of local farming conditions,Cold Call,Active
EOF

# Create distributor contacts CSV with basic fields
cat > data/distributor_contacts_import.csv << 'EOF'
AccountId,FirstName,LastName,Title,Department,Phone,Email,MailingStreet,MailingCity,MailingState,MailingPostalCode,MailingCountry,MailingLatitude,MailingLongitude,Description,LeadSource,Status
001KY00000E1Q9YYAV,Sarah,Smith,Sales Manager,Sales,(319) 555-1111,sarah.smith@distributor.com,1234 Main St,City1,Minnesota,11111,United States,36.111871,-72.488762,Experienced sales professional with expertise in agriculture distribution,Web,Active
001KY00000E1Q9ZYAV,Jennifer,Johnson,Account Executive,Business Development,(515) 555-2222,jennifer.johnson@company.com,5678 Oak Ave,City2,Tennessee,22222,United States,27.842601,-79.651832,Account manager specializing in farm equipment and supplies,Referral,Active
001KY00000E1Q9aYAF,Michael,Williams,Sales Representative,Customer Success,(641) 555-3333,michael.williams@distributor.com,9012 Pine Blvd,City3,Nebraska,33333,United States,34.687372,-85.995621,Sales representative with strong background in agricultural products,Trade Show,Active
001KY00000E1Q9bYAF,Jessica,Brown,Business Development Manager,Account Management,(712) 555-4444,jessica.brown@supply.com,3456 Maple Dr,City4,South Carolina,44444,United States,27.76855,-113.22815,Business development professional focused on expanding market reach,Phone Inquiry,Active
001KY00000E1Q9cYAF,David,Jones,Regional Manager,Sales Operations,(563) 555-5555,david.jones@company.com,7890 Cedar Ln,City5,Arizona,55555,United States,30.932589,-71.146934,Territory manager with deep knowledge of local farming communities,Cold Call,Active
EOF

echo "✅ Created contact CSV files"

# Import farmer contacts
echo "🌾 Importing farmer contacts..."
sf data import bulk --file data/farmer_contacts_import.csv --sobject Contact --wait 10 --target-org trailsignup.95cbd3623d857e@salesforce.com

if [ $? -eq 0 ]; then
    echo "✅ Farmer contacts import successful!"
else
    echo "❌ Farmer contacts import failed"
fi

# Import distributor contacts
echo "🏢 Importing distributor contacts..."
sf data import bulk --file data/distributor_contacts_import.csv --sobject Contact --wait 10 --target-org trailsignup.95cbd3623d857e@salesforce.com

if [ $? -eq 0 ]; then
    echo "✅ Distributor contacts import successful!"
else
    echo "❌ Distributor contacts import failed"
fi

# Verify imported contacts
echo "🔍 Verifying imported contacts..."
sf data query --query "SELECT Id, FirstName, LastName, Title, Account.Name FROM Contact WHERE Account.Industry = 'Agriculture' ORDER BY CreatedDate DESC LIMIT 10" --target-org trailsignup.95cbd3623d857e@salesforce.com

# Clean up temporary files
rm -f temp_accounts.csv

echo ""
echo "🎉 Contact import process completed!"
echo ""
echo "📊 Next Steps:"
echo "   1. Verify contact-account relationships in Salesforce"
echo "   2. Update contact details as needed"
echo "   3. Create contact reports and lists"
echo "   4. Set up contact workflows and automation"
echo ""
echo "🔗 Open Salesforce to view imported contacts:"
echo "   sf org open --target-org trailsignup.95cbd3623d857e@salesforce.com" 