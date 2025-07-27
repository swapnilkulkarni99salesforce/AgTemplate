#!/bin/bash

# Deploy Agriculture Account Record Types and Custom Fields
# This script deploys the Account Record Types (Distributor and Farm) 
# along with custom fields for farm-specific data

echo "🚀 Deploying Agriculture Account Record Types and Custom Fields..."

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

# Deploy the metadata
echo "📦 Deploying metadata from manifest/package.xml..."

sf project deploy start --manifest manifest/package.xml -w 10

if [ $? -eq 0 ]; then
    echo "✅ Deployment successful!"
    echo ""
    echo "🎉 Account Record Types and Custom Fields deployed:"
    echo "   📋 Record Types:"
    echo "      - Distributor (for agriculture distributors/suppliers)"
    echo "      - Farm (for agriculture farms/ranches)"
    echo ""
    echo "   🏷️  Custom Fields:"
    echo "      - Farm Size (Acres) - Number field"
    echo "      - Primary Equipment - Text field"
    echo "      - Farming Region - Text field"
    echo "      - Certification - Picklist (Organic, Conventional, GAP Certified, None)"
    echo "      - Water Source - Picklist (Well, Irrigation District, River, Lake, Municipal)"
    echo "      - Soil Type - Picklist (Loam, Clay, Sandy, Silt, Mixed)"
    echo ""
    echo "📊 Next Steps:"
    echo "   1. Import distributor data: data/agriculture_distributors.csv"
    echo "   2. Import farm data: data/agriculture_farms.csv"
    echo "   3. Use Data Import Wizard or Data Loader"
    echo "   4. Map 'Record Type' field to the appropriate Record Type"
else
    echo "❌ Deployment failed. Please check the error messages above."
    exit 1
fi 