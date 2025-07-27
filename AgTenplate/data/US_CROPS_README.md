# US Crop Records for Agriculture Template

This directory contains crop records for major crops harvested in the United States, designed for use with the Agriculture Template Salesforce org.

## 📁 Files

- `generate_us_crops.py` - Python script to generate crop records
- `us_crops.csv` - Generated CSV file with crop data
- `import_us_crops.sh` - Shell script to import crops into Salesforce

## 🌾 Crop Categories

### Cereal Grains (6 crops)
- **Corn (Maize)** - Most widely grown crop in the US
- **Wheat** - Great Plains staple crop
- **Soybeans** - Major oilseed crop
- **Rice** - Southern states specialty
- **Barley** - Used for malting and feed
- **Oats** - Human consumption and animal feed

### Fiber Crops (1 crop)
- **Cotton** - Southern US fiber crop

### Tubers (2 crops)
- **Potatoes** - Cool climate regions
- **Sweet Potatoes** - Southeast specialty

### Vegetables (6 crops)
- **Tomatoes** - California/Florida major crop
- **Lettuce** - Year-round California/Arizona
- **Onions** - Multiple state production
- **Carrots** - Root vegetable
- **Broccoli** - Cool-season vegetable
- **Bell Peppers** - Sweet pepper variety

### Fruits (8 crops)
- **Apples** - Washington/New York/Michigan
- **Oranges** - Florida/California citrus
- **Grapes** - California wine and table grapes
- **Strawberries** - California/Florida berries
- **Peaches** - Stone fruit
- **Blueberries** - Michigan/Oregon/Washington
- **Almonds** - California nut specialty
- **Pecans** - Southern US native nut

## 🗂️ Data Fields

Each crop record includes:

| Field | Type | Description |
|-------|------|-------------|
| `Name` | Text | Crop name |
| `Type__c` | Picklist | Crop category (Cereal Grain, Fiber Crop, Tuber, Vegetable, Fruit) |
| `Climate__c` | Picklist | Climate requirement (Temperate, Warm Temperate, Cool Temperate, etc.) |
| `Growing_Season__c` | Text | Growing season description |
| `Harvest_Time_Days__c` | Number | Days from planting to harvest |
| `Soil_Type__c` | Text | Preferred soil type |
| `Water_Requirements__c` | Picklist | Water needs (Low, Medium, High, Very High) |
| `Description__c` | Text | Detailed crop description |
| `Image_Name__c` | Text | Associated image filename |

## 🚀 Usage

### 1. Generate Crop Data
```bash
cd data
python3 generate_us_crops.py
```

### 2. Import to Salesforce
```bash
cd scripts
./import_us_crops.sh <your-org-alias>
```

## 📊 Crop Statistics

- **Total Crops**: 23
- **Geographic Coverage**: All major US agricultural regions
- **Climate Types**: 6 different climate zones
- **Water Requirements**: 4 levels (Low to Very High)
- **Growing Seasons**: Spring to Fall, Year-round, and Fall to Summer

## 🎯 Key Features

### Realistic Data
- Based on actual US agricultural production
- Accurate growing seasons and harvest times
- Proper climate and soil requirements
- Scientific names and descriptions

### Regional Focus
- **Corn Belt**: Corn, Soybeans
- **Great Plains**: Wheat, Barley
- **Southeast**: Cotton, Sweet Potatoes, Pecans
- **California**: Almonds, Grapes, Tomatoes, Oranges
- **Pacific Northwest**: Apples, Blueberries
- **Florida**: Oranges, Strawberries, Tomatoes

### Agricultural Diversity
- Covers all major crop categories
- Includes both food and fiber crops
- Represents different farming systems
- Supports various agricultural business models

## 🔧 Customization

You can modify `generate_us_crops.py` to:
- Add more crops
- Change field values
- Adjust growing seasons
- Add regional specificity
- Include additional metadata

## 📈 Business Value

These crop records support:
- **Farm Management**: Crop planning and rotation
- **Supply Chain**: Agricultural product tracking
- **Market Analysis**: Regional crop production data
- **Educational Content**: Agricultural knowledge base
- **Business Intelligence**: Crop performance analytics

## 🌍 Environmental Considerations

The data includes:
- Climate-specific requirements
- Water usage information
- Soil type preferences
- Growing season limitations

This helps support sustainable agriculture practices and environmental planning. 