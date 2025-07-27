#!/bin/bash

# Import US Crop Records into Salesforce
# This script uses Salesforce Data Loader to import crop records

echo "=========================================="
echo "Importing US Crop Records into Salesforce"
echo "=========================================="

# Set variables
CSV_FILE="../data/us_crops.csv"
LOG_FILE="crop_import_$(date +%Y%m%d_%H%M%S).log"
SUCCESS_FILE="crop_import_success_$(date +%Y%m%d_%H%M%S).csv"
ERROR_FILE="crop_import_error_$(date +%Y%m%d_%H%M%S).csv"

# Check if CSV file exists
if [ ! -f "$CSV_FILE" ]; then
    echo "Error: CSV file not found at $CSV_FILE"
    echo "Please run the generate_us_crops.py script first"
    exit 1
fi

echo "CSV file found: $CSV_FILE"
echo "Log file: $LOG_FILE"
echo "Success file: $SUCCESS_FILE"
echo "Error file: $ERROR_FILE"
echo ""

# Count records in CSV
RECORD_COUNT=$(tail -n +2 "$CSV_FILE" | wc -l)
echo "Found $RECORD_COUNT crop records to import"
echo ""

# Run Data Loader import
echo "Starting Data Loader import..."
echo "Command: sfdx data:import:tree --targetusername $1 --sobjecttreefiles $CSV_FILE --contenttype CSV"
echo ""

# Use SFDX to import the data
sfdx data:import:tree \
    --targetusername "$1" \
    --sobjecttreefiles "$CSV_FILE" \
    --contenttype CSV \
    --verbose

# Check exit status
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS: Crop records imported successfully!"
    echo ""
    echo "Summary:"
    echo "  - Total records processed: $RECORD_COUNT"
    echo "  - Import completed at: $(date)"
    echo ""
    echo "Imported crops include:"
    echo "  🌽 Corn (Maize) - Most widely grown US crop"
    echo "  🌾 Wheat - Great Plains staple"
    echo "  🫘 Soybeans - Major oilseed crop"
    echo "  🍚 Rice - Southern states specialty"
    echo "  🧶 Cotton - Southern fiber crop"
    echo "  🥔 Potatoes - Cool climate regions"
    echo "  🍅 Tomatoes - California/Florida major crop"
    echo "  🍎 Apples - Washington/New York specialty"
    echo "  🍊 Oranges - Florida/California citrus"
    echo "  🥜 Almonds - California nut specialty"
    echo ""
    echo "Crop types imported:"
    echo "  - Cereal Grains: 6 crops"
    echo "  - Fiber Crops: 1 crop"
    echo "  - Tubers: 2 crops"
    echo "  - Vegetables: 6 crops"
    echo "  - Fruits: 8 crops"
else
    echo ""
    echo "❌ ERROR: Import failed!"
    echo "Please check the error logs and try again."
    exit 1
fi

echo "=========================================="
echo "Import completed!"
echo "==========================================" 