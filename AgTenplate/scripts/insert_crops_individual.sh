#!/bin/bash

# Insert US Crop Records Individually
# This script creates crop records one by one to avoid CSV line ending issues

echo "=========================================="
echo "Inserting US Crop Records Individually"
echo "=========================================="

# Function to create a crop record
create_crop() {
    local name="$1"
    local type="$2"
    local climate="$3"
    local season="$4"
    local harvest_days="$5"
    local soil="$6"
    local water="$7"
    local description="$8"
    local image="$9"
    
    echo "Creating crop: $name"
    
    sfdx data:record:create \
        --sobject Crop__c \
        --values "Name='$name' Type__c='$type' Climate__c='$climate' Growing_Season__c='$season' Harvest_Time_Days__c=$harvest_days Soil_Type__c='$soil' Water_Requirements__c='$water' Description__c='$description' Image_Name__c='$image'" \
        --target-org "Ag Template"
    
    if [ $? -eq 0 ]; then
        echo "✅ Successfully created: $name"
    else
        echo "❌ Failed to create: $name"
    fi
    echo ""
}

# Create Cereal Grains
create_crop "Corn (Maize)" "Cereal Grain" "Warm Temperate" "Spring to Fall" 120 "Well-drained loamy soil" "Medium" "Zea mays, the most widely grown crop in the US. Used for food, feed, ethanol, and industrial products." "corn.jpg"

create_crop "Wheat" "Cereal Grain" "Temperate" "Fall to Summer" 240 "Well-drained clay loam" "Medium" "Triticum aestivum, grown for bread, pasta, and animal feed. Major crop in the Great Plains." "wheat.jpg"

create_crop "Soybeans" "Cereal Grain" "Warm Temperate" "Spring to Fall" 130 "Well-drained fertile soil" "Medium" "Glycine max, major oilseed crop used for animal feed, biodiesel, and food products." "soybeans.jpg"

create_crop "Rice" "Cereal Grain" "Warm Humid" "Spring to Fall" 150 "Clay loam with good water retention" "Very High" "Oryza sativa, primarily grown in Arkansas, California, Louisiana, Mississippi, Missouri, and Texas." "rice.jpg"

create_crop "Barley" "Cereal Grain" "Cool Temperate" "Spring to Summer" 90 "Well-drained loamy soil" "Medium" "Hordeum vulgare, used for malting, animal feed, and food products." "barley.jpg"

create_crop "Oats" "Cereal Grain" "Cool Temperate" "Spring to Summer" 100 "Well-drained fertile soil" "Medium" "Avena sativa, used for human consumption, animal feed, and cover crops." "oats.jpg"

# Create Fiber Crops
create_crop "Cotton" "Fiber Crop" "Warm Temperate" "Spring to Fall" 180 "Well-drained sandy loam" "High" "Gossypium hirsutum, grown for fiber and cottonseed oil. Major crop in the Southern US." "cotton.jpg"

# Create Tubers
create_crop "Potatoes" "Tuber" "Cool Temperate" "Spring to Fall" 100 "Well-drained sandy loam" "High" "Solanum tuberosum, grown for fresh consumption, processing, and seed potatoes." "potatoes.jpg"

create_crop "Sweet Potatoes" "Tuber" "Warm Temperate" "Spring to Fall" 120 "Well-drained sandy soil" "Medium" "Ipomoea batatas, nutritious root crop grown primarily in the Southeast." "sweet_potatoes.jpg"

# Create Vegetables
create_crop "Tomatoes" "Vegetable" "Warm Temperate" "Spring to Fall" 80 "Well-drained loamy soil" "Medium" "Solanum lycopersicum, grown for fresh market and processing. Major crop in California and Florida." "tomatoes.jpg"

create_crop "Lettuce" "Vegetable" "Cool Temperate" "Spring to Fall" 60 "Well-drained fertile soil" "High" "Lactuca sativa, leafy green vegetable grown year-round in California and Arizona." "lettuce.jpg"

create_crop "Onions" "Vegetable" "Temperate" "Spring to Summer" 100 "Well-drained sandy loam" "Medium" "Allium cepa, grown for fresh market and storage. Major crops in California, Washington, and Georgia." "onions.jpg"

create_crop "Carrots" "Vegetable" "Cool Temperate" "Spring to Fall" 75 "Well-drained sandy soil" "Medium" "Daucus carota, root vegetable grown for fresh market and processing." "carrots.jpg"

create_crop "Broccoli" "Vegetable" "Cool Temperate" "Spring to Fall" 70 "Well-drained fertile soil" "High" "Brassica oleracea var. italica, cool-season vegetable grown in California and Arizona." "broccoli.jpg"

create_crop "Bell Peppers" "Vegetable" "Warm Temperate" "Spring to Fall" 80 "Well-drained loamy soil" "Medium" "Capsicum annuum, sweet pepper variety grown for fresh market." "bell_peppers.jpg"

# Create Fruits
create_crop "Apples" "Fruit" "Temperate" "Spring to Fall" 150 "Well-drained loamy soil" "Medium" "Malus domestica, major fruit crop grown in Washington, New York, and Michigan." "apples.jpg"

create_crop "Oranges" "Fruit" "Warm Temperate" "Year-round" 300 "Well-drained sandy soil" "High" "Citrus sinensis, major citrus crop grown primarily in Florida and California." "oranges.jpg"

create_crop "Grapes" "Fruit" "Temperate" "Spring to Fall" 180 "Well-drained gravelly soil" "Medium" "Vitis vinifera, grown for table grapes, wine, and raisins. Major crop in California." "grapes.jpg"

create_crop "Strawberries" "Fruit" "Temperate" "Spring to Summer" 90 "Well-drained sandy loam" "High" "Fragaria × ananassa, grown for fresh market and processing. Major crops in California and Florida." "strawberries.jpg"

create_crop "Peaches" "Fruit" "Warm Temperate" "Spring to Summer" 120 "Well-drained loamy soil" "Medium" "Prunus persica, stone fruit grown for fresh market and processing." "peaches.jpg"

create_crop "Blueberries" "Fruit" "Cool Temperate" "Spring to Summer" 90 "Acidic well-drained soil" "High" "Vaccinium corymbosum, high-value berry crop grown in Michigan, Oregon, and Washington." "blueberries.jpg"

create_crop "Almonds" "Fruit" "Warm Temperate" "Spring to Fall" 240 "Well-drained deep soil" "High" "Prunus dulcis, major nut crop grown primarily in California." "almonds.jpg"

create_crop "Pecans" "Fruit" "Warm Temperate" "Spring to Fall" 200 "Well-drained deep soil" "Medium" "Carya illinoinensis, native nut tree grown in the Southern US." "pecans.jpg"

echo "=========================================="
echo "Crop insertion completed!"
echo "=========================================="

# Count total records
echo "Counting total crop records..."
sfdx data:record:query --sobject Crop__c --target-org "Ag Template" --json | grep -o '"totalSize":[0-9]*' | cut -d':' -f2 