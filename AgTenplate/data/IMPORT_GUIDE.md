# Agriculture Data Import Guide

This guide will help you import the agriculture distributor and farm data into your Salesforce org with proper Record Types.

## Prerequisites

1. **Salesforce Org**: You need access to a Salesforce org
2. **Salesforce CLI**: Install Salesforce CLI for deployment
3. **Record Types**: Deploy the Account Record Types first

## Step 1: Deploy Record Types and Custom Fields

Before importing data, you must deploy the Account Record Types and custom fields:

```bash
# Make sure you're authenticated to your Salesforce org
sf org login web

# Deploy the metadata
./scripts/deploy_metadata.sh
```

This will create:
- **Account Record Types**: Distributor and Farm
- **Custom Fields**: Farm-specific fields for the Farm record type

## Step 2: Import Data

### Option A: Using Data Import Wizard (Recommended for small datasets)

1. **Go to Setup** → **Data Import Wizard**
2. **Choose the object**: Account
3. **Upload your CSV file**:
   - For distributors: `data/agriculture_distributors.csv`
   - For farms: `data/agriculture_farms.csv`
4. **Map fields**:
   - **Record Type**: Map to "Record Type" field (or use Record Type ID)
   - **Record Type ID**: Map to "Record Type ID" field (alternative to Record Type)
   - **Account Name**: Map to "Account Name"
   - **Agriculture Type**: Map to "Agriculture Type" custom field
   - **Industry**: Map to "Industry" field
   - **Billing Address**: Map all billing fields
   - **Phone**: Map to "Phone"
   - **Website**: Map to "Website"
   - **Annual Revenue**: Map to "Annual Revenue"
   - **Number of Employees**: Map to "Number of Employees"
   - **Description**: Map to "Description"
   - **Rating**: Map to "Rating"
   - **Customer Priority**: Map to "Customer Priority"
   - **SLA**: Map to "SLA"
   - **Upsell Opportunity**: Map to "Upsell Opportunity"
   - **Active**: Map to "Active"
   - **Created Date**: Map to "Created Date"
   - **Last Activity Date**: Map to "Last Activity Date"
   - **Billing Latitude**: Map to "Billing Latitude"
   - **Billing Longitude**: Map to "Billing Longitude"

5. **For Farm data, also map**:
   - **Farm Size (Acres)**: Map to "Farm Size (Acres)" custom field
   - **Primary Equipment**: Map to "Primary Equipment" custom field
   - **Farming Region**: Map to "Farming Region" custom field
   - **Certification**: Map to "Certification" custom field
   - **Water Source**: Map to "Water Source" custom field
   - **Soil Type**: Map to "Soil Type" custom field

### Option B: Using Data Loader

1. **Download Data Loader** from Salesforce
2. **Login** to your org
3. **Choose "Insert"** operation
4. **Select "Account"** object
5. **Upload CSV file** and map fields as described above
6. **Set Record Type**: Make sure to map the "Record Type" field correctly

## Step 3: Verify Import

After import, verify that:

1. **Record Types are assigned correctly**:
   - Distributor accounts should have "Distributor" record type
   - Farm accounts should have "Farm" record type

2. **Custom fields are populated** (for farm data):
   - Farm Size (Acres)
   - Primary Equipment
   - Farming Region
   - Certification
   - Water Source
   - Soil Type

3. **Geo coordinates are working**:
   - Check that Billing Latitude and Billing Longitude are populated
   - Verify on a map view if available

## Troubleshooting

### Common Issues:

1. **"Record Type not found" error**:
   - Make sure you deployed the Record Types first
   - Check that the Record Type names match exactly: "Distributor" and "Farm"

2. **"Field not found" error**:
   - Ensure custom fields are deployed
   - Check field API names match exactly

3. **Import fails**:
   - Check for required fields that might be missing
   - Verify data format (dates, numbers, etc.)
   - Check for duplicate Account Names

### Data Validation:

Before importing, you can validate your data:

```bash
# Check CSV format
head -5 data/agriculture_distributors.csv
head -5 data/agriculture_farms.csv

# Count records
wc -l data/agriculture_distributors.csv
wc -l data/agriculture_farms.csv
```

## Post-Import Tasks

1. **Create Page Layouts** for each Record Type
2. **Set up Validation Rules** if needed
3. **Create Reports** to analyze your agriculture data
4. **Set up Dashboards** for monitoring
5. **Configure Workflows** or Process Builder for automation

## Support

If you encounter issues:
1. Check Salesforce Trailhead for Data Import tutorials
2. Review the Salesforce Data Import Guide
3. Check the generated data files for any formatting issues

## Data Summary

- **Distributors**: 50 records across 27 US states
- **Farms**: 50 records across 25 US states
- **Total**: 100 agriculture accounts ready for import

Both datasets include complete billing addresses with geo coordinates for mapping and location-based features. 