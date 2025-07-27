# Agriculture Data

This folder contains generated agriculture data for Salesforce Account object with both distributor and farm record types.

## Files

### `agriculture_distributors.csv`
- **Records**: 50 agriculture distributor companies
- **Format**: CSV with Salesforce Account object fields
- **Record Type**: Distributor
- **Coverage**: 27 US states with major agriculture regions

### `agriculture_farms.csv`
- **Records**: 50 agriculture farm companies
- **Format**: CSV with Salesforce Account object fields
- **Record Type**: Farm
- **Coverage**: 25 US states with major farming regions
- **Additional Fields**: Farm size, equipment, certification, water source, soil type

### `generate_distributor_data.py`
- **Purpose**: Python script to generate realistic agriculture distributor data
- **Features**: 
  - US-based addresses with geo coordinates
  - Realistic company names and types
  - Complete billing address information
  - Salesforce Account object field mapping

### `generate_farm_data.py`
- **Purpose**: Python script to generate realistic agriculture farm data
- **Features**: 
  - US-based rural addresses with geo coordinates
  - Realistic farm names and types
  - Farm-specific fields (acres, equipment, certification)
  - Rural address generation
  - Salesforce Account object field mapping

## Data Fields

| Field | Description | Example |
|-------|-------------|---------|
| Account Name | Company name | "Agri Supply Co." |
| Record Type | Salesforce record type | "Distributor" |
| Record Type ID | Salesforce record type ID | "012KY0000001OFdYAM" |
| Agriculture Type | Custom agriculture type | "Seed Distributor" |
| Industry | Industry classification | "Agriculture" |
| Billing Street | Street address | "1234 Main St" |
| Billing City | City name | "Fresno" |
| Billing State | US State | "California" |
| Billing Postal Code | ZIP code | "93710" |
| Billing Country | Country | "United States" |
| Phone | Contact phone | "(515) 123-4567" |
| Website | Company website | "www.agrisupplyco.com" |
| Annual Revenue | Revenue in USD | 5000000 |
| Number of Employees | Employee count | 150 |
| Description | Company description | "Leading seed distributor serving the California region" |
| Rating | Lead rating | "Hot/Warm/Cold" |
| Customer Priority | Priority level | "High/Medium/Low" |
| SLA | Service level agreement | "Gold/Silver/Bronze" |
| Upsell Opportunity | Upsell potential | "Yes/No/Maybe" |
| Active | Active status | "Yes" |
| Created Date | Account creation date | "2023-01-15" |
| Last Activity Date | Last activity | "2024-01-20" |
| Billing Latitude | Geographic latitude | 36.7378 |
| Billing Longitude | Geographic longitude | -119.7871 |

## Company Types Included

### Distributor Types
1. Seed Distributor
2. Fertilizer Supplier
3. Equipment Dealer
4. Crop Protection
5. Irrigation Systems
6. Grain Handler
7. Feed Supplier
8. Chemical Distributor
9. Machinery Parts
10. Organic Products
11. Precision Agriculture
12. Livestock Equipment

### Farm Types
1. Dairy Farm
2. Cattle Ranch
3. Corn Farm
4. Soybean Farm
5. Wheat Farm
6. Cotton Farm
7. Rice Farm
8. Vegetable Farm
9. Fruit Orchard
10. Vineyard
11. Poultry Farm
12. Hog Farm
13. Mixed Crop Farm
14. Organic Farm
15. Grain Farm

## Geographic Coverage

The data covers major agriculture states including:
- California (Central Valley, Salinas Valley, Imperial Valley)
- Iowa (Corn Belt, Northeast Iowa, Southeast Iowa)
- Illinois (Central Illinois, Northern Illinois, Southern Illinois)
- Texas (Panhandle, High Plains, Central Texas)
- Florida (Central Florida, South Florida, North Florida)
- And 20+ other US states with major farming regions

## Usage

### Import to Salesforce
1. Use Data Import Wizard or Data Loader
2. Map fields to Account object
3. Set Record Type to "Distributor"
4. Import with appropriate settings

### Regenerate Data
```bash
# Generate distributor data
python3 data/generate_distributor_data.py

# Generate farm data
python3 data/generate_farm_data.py
```

## Data Quality

- ✅ Realistic company names
- ✅ Valid US addresses
- ✅ Accurate geo coordinates
- ✅ Proper phone number format
- ✅ Salesforce-compatible field values
- ✅ Diverse business types
- ✅ Geographic distribution across US

Generated on: $(date)
Total Records: 100 (50 distributors + 50 farms)
States Covered: 27 (distributors) + 25 (farms)
Company Types: 12 (distributors) + 15 (farms) 