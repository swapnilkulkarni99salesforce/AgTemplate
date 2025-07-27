#!/bin/bash

# Import Agriculture Data to Salesforce
# This script imports distributor and farm data with proper field mapping

echo "🚀 Starting Agriculture Data Import to Salesforce..."

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

# Create distributors CSV with basic fields
cat > data/distributors_import.csv << 'EOF'
Name,Industry,Phone,Website,AnnualRevenue,NumberOfEmployees,Description,Rating,BillingStreet,BillingCity,BillingState,BillingPostalCode,BillingCountry
Plains Enterprises,Agriculture,(319) 662-7990,www.plainsenterprises.com,44137682,309,Leading machinery parts serving the Minnesota region,Cold,875 Pine St,City1,Minnesota,45937,United States
Southern Inc.,Agriculture,(515) 272-5705,www.southerninc.com,42165025,231,Leading fertilizer supplier serving the Tennessee region,Hot,4727 Washington Ln,City2,Tennessee,13507,United States
Harvest Enterprises,Agriculture,(641) 529-1865,www.harvestenterprises.com,13175865,211,Leading livestock equipment serving the Nebraska region,Hot,3835 Madison Blvd,City3,Nebraska,63828,United States
Farm Supply Co.,Agriculture,(319) 373-5468,www.farmsupplyco.com,15858504,195,Leading equipment dealer serving the South Carolina region,Cold,5572 Madison Rd,City4,South Carolina,63746,United States
Grain Solutions,Agriculture,(641) 953-5766,www.grainsolutions.com,12716418,245,Leading grain handler serving the Arizona region,Hot,5452 Polk Way,City5,Arizona,79002,United States
EOF

# Create farms CSV with basic fields
cat > data/farms_import.csv << 'EOF'
Name,Industry,Phone,Website,AnnualRevenue,NumberOfEmployees,Description,Rating,BillingStreet,BillingCity,BillingState,BillingPostalCode,BillingCountry
Miller Big Valley,Agriculture,(319) 481-1130,www.millerbigvalley.com,2449780,3,Family-owned cattle ranch specializing in fertilizer equipment,Cold,48952 East Spring Road,Agri Town,California,13359,United States
Cedar Estates,Agriculture,(319) 534-8217,www.cedarestates.com,8562256,39,Multi-generational grain farm with 4905 acres,Cold,35323 Spring Road,Rural Valley,North Dakota,58898,United States
Elm Fields,Agriculture,(712) 666-4563,www.elmfields.com,767299,4,Family-owned corn farm specializing in tractors,Warm,81869 Dirt Road,Rural City 3,Illinois,77490,United States
Mountain Hills,Agriculture,(712) 510-6830,www.mountainhills.com,5695282,41,Modern rice farm using sustainable practices,Cold,66038 Farm Road,Rural City 4,South Dakota,53397,United States
Birch Produce,Agriculture,(641) 447-2398,www.birchproduce.com,8562256,39,Multi-generational grain farm with 4905 acres,Cold,35323 Spring Road,Rural Valley,North Dakota,58898,United States
EOF

echo "✅ Created simplified CSV files"

# Import distributors
echo "📦 Importing distributor data..."
sf data import bulk --file data/distributors_import.csv --sobject Account --wait 10 --target-org trailsignup.95cbd3623d857e@salesforce.com

if [ $? -eq 0 ]; then
    echo "✅ Distributor import successful!"
else
    echo "❌ Distributor import failed"
fi

# Import farms
echo "🌾 Importing farm data..."
sf data import bulk --file data/farms_import.csv --sobject Account --wait 10 --target-org trailsignup.95cbd3623d857e@salesforce.com

if [ $? -eq 0 ]; then
    echo "✅ Farm import successful!"
else
    echo "❌ Farm import failed"
fi

# Verify imported records
echo "🔍 Verifying imported records..."
sf data query --query "SELECT Id, Name, Industry, RecordType.Name FROM Account WHERE Industry = 'Agriculture' ORDER BY CreatedDate DESC LIMIT 10" --target-org trailsignup.95cbd3623d857e@salesforce.com

echo ""
echo "🎉 Import process completed!"
echo ""
echo "📊 Next Steps:"
echo "   1. Manually assign Record Types to accounts in Salesforce UI"
echo "   2. Update custom fields (Agriculture Type, Farm Size, etc.)"
echo "   3. Verify geo coordinates are working"
echo "   4. Create reports and dashboards"
echo ""
echo "🔗 Open Salesforce:"
echo "   sf org open --target-org trailsignup.95cbd3623d857e@salesforce.com" 