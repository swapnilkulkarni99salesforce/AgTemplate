#!/usr/bin/env python3
"""
Generate US Crop Records for Salesforce
Creates crop records for major crops harvested in the United States
"""

import csv
import os

def generate_us_crops():
    """Generate crop records for major US crops"""
    
    crops = [
        # Cereal Grains
        {
            'Name': 'Corn (Maize)',
            'Type__c': 'Cereal Grain',
            'Climate__c': 'Warm Temperate',
            'Growing_Season__c': 'Spring to Fall',
            'Harvest_Time_Days__c': 120,
            'Soil_Type__c': 'Well-drained loamy soil',
            'Water_Requirements__c': 'Medium',
            'Description__c': 'Zea mays, the most widely grown crop in the US. Used for food, feed, ethanol, and industrial products.',
            'Image_Name__c': 'corn.jpg'
        },
        {
            'Name': 'Wheat',
            'Type__c': 'Cereal Grain',
            'Climate__c': 'Temperate',
            'Growing_Season__c': 'Fall to Summer',
            'Harvest_Time_Days__c': 240,
            'Soil_Type__c': 'Well-drained clay loam',
            'Water_Requirements__c': 'Medium',
            'Description__c': 'Triticum aestivum, grown for bread, pasta, and animal feed. Major crop in the Great Plains.',
            'Image_Name__c': 'wheat.jpg'
        },
        {
            'Name': 'Soybeans',
            'Type__c': 'Cereal Grain',
            'Climate__c': 'Warm Temperate',
            'Growing_Season__c': 'Spring to Fall',
            'Harvest_Time_Days__c': 130,
            'Soil_Type__c': 'Well-drained fertile soil',
            'Water_Requirements__c': 'Medium',
            'Description__c': 'Glycine max, major oilseed crop used for animal feed, biodiesel, and food products.',
            'Image_Name__c': 'soybeans.jpg'
        },
        {
            'Name': 'Rice',
            'Type__c': 'Cereal Grain',
            'Climate__c': 'Warm Humid',
            'Growing_Season__c': 'Spring to Fall',
            'Harvest_Time_Days__c': 150,
            'Soil_Type__c': 'Clay loam with good water retention',
            'Water_Requirements__c': 'Very High',
            'Description__c': 'Oryza sativa, primarily grown in Arkansas, California, Louisiana, Mississippi, Missouri, and Texas.',
            'Image_Name__c': 'rice.jpg'
        },
        {
            'Name': 'Barley',
            'Type__c': 'Cereal Grain',
            'Climate__c': 'Cool Temperate',
            'Growing_Season__c': 'Spring to Summer',
            'Harvest_Time_Days__c': 90,
            'Soil_Type__c': 'Well-drained loamy soil',
            'Water_Requirements__c': 'Medium',
            'Description__c': 'Hordeum vulgare, used for malting, animal feed, and food products.',
            'Image_Name__c': 'barley.jpg'
        },
        {
            'Name': 'Oats',
            'Type__c': 'Cereal Grain',
            'Climate__c': 'Cool Temperate',
            'Growing_Season__c': 'Spring to Summer',
            'Harvest_Time_Days__c': 100,
            'Soil_Type__c': 'Well-drained fertile soil',
            'Water_Requirements__c': 'Medium',
            'Description__c': 'Avena sativa, used for human consumption, animal feed, and cover crops.',
            'Image_Name__c': 'oats.jpg'
        },
        
        # Fiber Crops
        {
            'Name': 'Cotton',
            'Type__c': 'Fiber Crop',
            'Climate__c': 'Warm Temperate',
            'Growing_Season__c': 'Spring to Fall',
            'Harvest_Time_Days__c': 180,
            'Soil_Type__c': 'Well-drained sandy loam',
            'Water_Requirements__c': 'High',
            'Description__c': 'Gossypium hirsutum, grown for fiber and cottonseed oil. Major crop in the Southern US.',
            'Image_Name__c': 'cotton.jpg'
        },
        
        # Tubers
        {
            'Name': 'Potatoes',
            'Type__c': 'Tuber',
            'Climate__c': 'Cool Temperate',
            'Growing_Season__c': 'Spring to Fall',
            'Harvest_Time_Days__c': 100,
            'Soil_Type__c': 'Well-drained sandy loam',
            'Water_Requirements__c': 'High',
            'Description__c': 'Solanum tuberosum, grown for fresh consumption, processing, and seed potatoes.',
            'Image_Name__c': 'potatoes.jpg'
        },
        {
            'Name': 'Sweet Potatoes',
            'Type__c': 'Tuber',
            'Climate__c': 'Warm Temperate',
            'Growing_Season__c': 'Spring to Fall',
            'Harvest_Time_Days__c': 120,
            'Soil_Type__c': 'Well-drained sandy soil',
            'Water_Requirements__c': 'Medium',
            'Description__c': 'Ipomoea batatas, nutritious root crop grown primarily in the Southeast.',
            'Image_Name__c': 'sweet_potatoes.jpg'
        },
        
        # Vegetables
        {
            'Name': 'Tomatoes',
            'Type__c': 'Vegetable',
            'Climate__c': 'Warm Temperate',
            'Growing_Season__c': 'Spring to Fall',
            'Harvest_Time_Days__c': 80,
            'Soil_Type__c': 'Well-drained loamy soil',
            'Water_Requirements__c': 'Medium',
            'Description__c': 'Solanum lycopersicum, grown for fresh market and processing. Major crop in California and Florida.',
            'Image_Name__c': 'tomatoes.jpg'
        },
        {
            'Name': 'Lettuce',
            'Type__c': 'Vegetable',
            'Climate__c': 'Cool Temperate',
            'Growing_Season__c': 'Spring to Fall',
            'Harvest_Time_Days__c': 60,
            'Soil_Type__c': 'Well-drained fertile soil',
            'Water_Requirements__c': 'High',
            'Description__c': 'Lactuca sativa, leafy green vegetable grown year-round in California and Arizona.',
            'Image_Name__c': 'lettuce.jpg'
        },
        {
            'Name': 'Onions',
            'Type__c': 'Vegetable',
            'Climate__c': 'Temperate',
            'Growing_Season__c': 'Spring to Summer',
            'Harvest_Time_Days__c': 100,
            'Soil_Type__c': 'Well-drained sandy loam',
            'Water_Requirements__c': 'Medium',
            'Description__c': 'Allium cepa, grown for fresh market and storage. Major crops in California, Washington, and Georgia.',
            'Image_Name__c': 'onions.jpg'
        },
        {
            'Name': 'Carrots',
            'Type__c': 'Vegetable',
            'Climate__c': 'Cool Temperate',
            'Growing_Season__c': 'Spring to Fall',
            'Harvest_Time_Days__c': 75,
            'Soil_Type__c': 'Well-drained sandy soil',
            'Water_Requirements__c': 'Medium',
            'Description__c': 'Daucus carota, root vegetable grown for fresh market and processing.',
            'Image_Name__c': 'carrots.jpg'
        },
        {
            'Name': 'Broccoli',
            'Type__c': 'Vegetable',
            'Climate__c': 'Cool Temperate',
            'Growing_Season__c': 'Spring to Fall',
            'Harvest_Time_Days__c': 70,
            'Soil_Type__c': 'Well-drained fertile soil',
            'Water_Requirements__c': 'High',
            'Description__c': 'Brassica oleracea var. italica, cool-season vegetable grown in California and Arizona.',
            'Image_Name__c': 'broccoli.jpg'
        },
        {
            'Name': 'Bell Peppers',
            'Type__c': 'Vegetable',
            'Climate__c': 'Warm Temperate',
            'Growing_Season__c': 'Spring to Fall',
            'Harvest_Time_Days__c': 80,
            'Soil_Type__c': 'Well-drained loamy soil',
            'Water_Requirements__c': 'Medium',
            'Description__c': 'Capsicum annuum, sweet pepper variety grown for fresh market.',
            'Image_Name__c': 'bell_peppers.jpg'
        },
        
        # Fruits
        {
            'Name': 'Apples',
            'Type__c': 'Fruit',
            'Climate__c': 'Temperate',
            'Growing_Season__c': 'Spring to Fall',
            'Harvest_Time_Days__c': 150,
            'Soil_Type__c': 'Well-drained loamy soil',
            'Water_Requirements__c': 'Medium',
            'Description__c': 'Malus domestica, major fruit crop grown in Washington, New York, and Michigan.',
            'Image_Name__c': 'apples.jpg'
        },
        {
            'Name': 'Oranges',
            'Type__c': 'Fruit',
            'Climate__c': 'Warm Temperate',
            'Growing_Season__c': 'Year-round',
            'Harvest_Time_Days__c': 300,
            'Soil_Type__c': 'Well-drained sandy soil',
            'Water_Requirements__c': 'High',
            'Description__c': 'Citrus sinensis, major citrus crop grown primarily in Florida and California.',
            'Image_Name__c': 'oranges.jpg'
        },
        {
            'Name': 'Grapes',
            'Type__c': 'Fruit',
            'Climate__c': 'Temperate',
            'Growing_Season__c': 'Spring to Fall',
            'Harvest_Time_Days__c': 180,
            'Soil_Type__c': 'Well-drained gravelly soil',
            'Water_Requirements__c': 'Medium',
            'Description__c': 'Vitis vinifera, grown for table grapes, wine, and raisins. Major crop in California.',
            'Image_Name__c': 'grapes.jpg'
        },
        {
            'Name': 'Strawberries',
            'Type__c': 'Fruit',
            'Climate__c': 'Temperate',
            'Growing_Season__c': 'Spring to Summer',
            'Harvest_Time_Days__c': 90,
            'Soil_Type__c': 'Well-drained sandy loam',
            'Water_Requirements__c': 'High',
            'Description__c': 'Fragaria × ananassa, grown for fresh market and processing. Major crops in California and Florida.',
            'Image_Name__c': 'strawberries.jpg'
        },
        {
            'Name': 'Peaches',
            'Type__c': 'Fruit',
            'Climate__c': 'Warm Temperate',
            'Growing_Season__c': 'Spring to Summer',
            'Harvest_Time_Days__c': 120,
            'Soil_Type__c': 'Well-drained loamy soil',
            'Water_Requirements__c': 'Medium',
            'Description__c': 'Prunus persica, stone fruit grown for fresh market and processing.',
            'Image_Name__c': 'peaches.jpg'
        },
        {
            'Name': 'Blueberries',
            'Type__c': 'Fruit',
            'Climate__c': 'Cool Temperate',
            'Growing_Season__c': 'Spring to Summer',
            'Harvest_Time_Days__c': 90,
            'Soil_Type__c': 'Acidic well-drained soil',
            'Water_Requirements__c': 'High',
            'Description__c': 'Vaccinium corymbosum, high-value berry crop grown in Michigan, Oregon, and Washington.',
            'Image_Name__c': 'blueberries.jpg'
        },
        {
            'Name': 'Almonds',
            'Type__c': 'Fruit',
            'Climate__c': 'Warm Temperate',
            'Growing_Season__c': 'Spring to Fall',
            'Harvest_Time_Days__c': 240,
            'Soil_Type__c': 'Well-drained deep soil',
            'Water_Requirements__c': 'High',
            'Description__c': 'Prunus dulcis, major nut crop grown primarily in California.',
            'Image_Name__c': 'almonds.jpg'
        },
        {
            'Name': 'Pecans',
            'Type__c': 'Fruit',
            'Climate__c': 'Warm Temperate',
            'Growing_Season__c': 'Spring to Fall',
            'Harvest_Time_Days__c': 200,
            'Soil_Type__c': 'Well-drained deep soil',
            'Water_Requirements__c': 'Medium',
            'Description__c': 'Carya illinoinensis, native nut tree grown in the Southern US.',
            'Image_Name__c': 'pecans.jpg'
        }
    ]
    
    return crops

def write_crop_csv(crops, filename='us_crops.csv'):
    """Write crop data to CSV file"""
    
    fieldnames = [
        'Name', 'Type__c', 'Climate__c', 'Growing_Season__c', 
        'Harvest_Time_Days__c', 'Soil_Type__c', 'Water_Requirements__c',
        'Description__c', 'Image_Name__c'
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(crops)
    
    print(f"Generated {len(crops)} crop records in {filename}")

def main():
    """Main function to generate US crop records"""
    print("Generating US Crop Records...")
    
    # Generate crop data
    crops = generate_us_crops()
    
    # Write to CSV
    write_crop_csv(crops)
    
    # Print summary
    print(f"\nSummary:")
    print(f"Total crops: {len(crops)}")
    
    # Count by type
    type_counts = {}
    for crop in crops:
        crop_type = crop['Type__c']
        type_counts[crop_type] = type_counts.get(crop_type, 0) + 1
    
    print("\nCrops by type:")
    for crop_type, count in type_counts.items():
        print(f"  {crop_type}: {count}")
    
    print("\nMajor US crops included:")
    print("  - Corn (most widely grown)")
    print("  - Soybeans (major oilseed)")
    print("  - Wheat (Great Plains staple)")
    print("  - Cotton (Southern fiber crop)")
    print("  - Rice (Southern states)")
    print("  - Potatoes (cool climate regions)")
    print("  - Tomatoes (California/Florida)")
    print("  - Apples (Washington/New York)")
    print("  - Oranges (Florida/California)")
    print("  - Almonds (California specialty)")

if __name__ == "__main__":
    main() 