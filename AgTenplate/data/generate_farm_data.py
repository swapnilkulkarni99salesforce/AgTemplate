#!/usr/bin/env python3
"""
Generate Agriculture Farm Data for Salesforce Account Object
Creates realistic farm data with US addresses and geo coordinates
"""

import csv
import random
from datetime import datetime, timedelta

# US States with major agriculture regions
US_STATES = [
    "California", "Iowa", "Illinois", "Nebraska", "Minnesota", "Indiana", 
    "Kansas", "Ohio", "Texas", "Wisconsin", "Missouri", "North Dakota",
    "South Dakota", "Michigan", "Kentucky", "Tennessee", "Arkansas",
    "Georgia", "North Carolina", "South Carolina", "Florida", "Alabama",
    "Mississippi", "Louisiana", "Oklahoma", "Colorado", "Washington",
    "Oregon", "Idaho", "Montana", "Wyoming", "Utah", "Arizona", "New Mexico"
]

# Major farming regions with approximate coordinates
FARM_REGIONS = {
    "California": [
        ("Central Valley", 36.7378, -119.7871),
        ("Salinas Valley", 36.6777, -121.6555),
        ("Imperial Valley", 32.9787, -115.5301),
        ("San Joaquin Valley", 36.7378, -119.7871),
        ("Sacramento Valley", 38.5816, -121.4944)
    ],
    "Iowa": [
        ("Corn Belt", 41.5868, -93.6250),
        ("Northeast Iowa", 42.4963, -96.4049),
        ("Southeast Iowa", 40.6936, -89.5890),
        ("Central Iowa", 41.9779, -91.6656),
        ("Western Iowa", 42.4928, -92.3426)
    ],
    "Illinois": [
        ("Central Illinois", 40.6936, -89.5890),
        ("Northern Illinois", 42.2711, -89.0940),
        ("Southern Illinois", 37.0859, -88.4761),
        ("Western Illinois", 40.1164, -88.2434),
        ("Eastern Illinois", 39.7817, -89.6501)
    ],
    "Texas": [
        ("Panhandle", 35.4019, -101.8951),
        ("High Plains", 34.1848, -101.7068),
        ("Central Texas", 30.2672, -97.7431),
        ("East Texas", 32.7767, -96.7970),
        ("South Texas", 29.4241, -98.4936)
    ],
    "Florida": [
        ("Central Florida", 28.5383, -81.3792),
        ("South Florida", 25.7617, -80.1918),
        ("North Florida", 30.3322, -81.6557),
        ("Gulf Coast", 27.9506, -82.4572),
        ("Atlantic Coast", 28.5383, -81.3792)
    ]
}

# Farm types and crops
FARM_TYPES = [
    "Dairy Farm", "Cattle Ranch", "Corn Farm", "Soybean Farm", "Wheat Farm",
    "Cotton Farm", "Rice Farm", "Vegetable Farm", "Fruit Orchard", "Vineyard",
    "Poultry Farm", "Hog Farm", "Mixed Crop Farm", "Organic Farm", "Grain Farm"
]

# Farm name components
FARM_PREFIXES = [
    "Green", "Golden", "Sunny", "Happy", "Lucky", "Big", "Little", "Old", "New",
    "River", "Valley", "Hill", "Mountain", "Prairie", "Meadow", "Spring", "Oak",
    "Maple", "Pine", "Cedar", "Elm", "Willow", "Birch", "Cherry", "Apple"
]

FARM_SUFFIXES = [
    "Farm", "Ranch", "Acres", "Fields", "Meadows", "Valley", "Hills", "Springs",
    "Orchard", "Vineyard", "Dairy", "Cattle", "Grain", "Produce", "Estates"
]

# Street names for rural areas
RURAL_STREET_NAMES = [
    "County Road", "Farm Road", "Rural Route", "Old Highway", "Dirt Road",
    "Gravel Road", "Farm Lane", "Ranch Road", "Valley Road", "Hill Road",
    "Spring Road", "Creek Road", "River Road", "Bridge Road", "Church Road"
]

# Farm equipment and specialties
FARM_EQUIPMENT = [
    "Tractors", "Harvesters", "Irrigation Systems", "Grain Storage", "Livestock Equipment",
    "Precision Agriculture", "Greenhouse Systems", "Dairy Equipment", "Poultry Houses",
    "Fertilizer Equipment", "Seed Drills", "Sprayers", "Hay Equipment"
]

def generate_farm_name():
    """Generate a realistic farm name"""
    prefix = random.choice(FARM_PREFIXES)
    suffix = random.choice(FARM_SUFFIXES)
    
    # Sometimes add a family name
    if random.random() < 0.3:
        family_names = ["Johnson", "Smith", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
        family = random.choice(family_names)
        return f"{family} {prefix} {suffix}"
    else:
        return f"{prefix} {suffix}"

def generate_phone():
    """Generate a realistic US phone number"""
    area_codes = ["515", "319", "563", "712", "641", "319", "515", "712", "641", "319"]
    area = random.choice(area_codes)
    prefix = str(random.randint(200, 999))
    suffix = str(random.randint(1000, 9999))
    return f"({area}) {prefix}-{suffix}"

def generate_farm_address(state):
    """Generate a realistic rural farm address"""
    street_name = random.choice(RURAL_STREET_NAMES)
    street_num = random.randint(1000, 99999)
    
    # Add directional or descriptive elements
    directions = ["North", "South", "East", "West", "Northeast", "Northwest", "Southeast", "Southwest"]
    if random.random() < 0.4:
        direction = random.choice(directions)
        street_address = f"{street_num} {direction} {street_name}"
    else:
        street_address = f"{street_num} {street_name}"
    
    return street_address

def generate_farm_data(num_records=50):
    """Generate farm data for Salesforce Account object"""
    
    farms = []
    
    for i in range(num_records):
        # Generate farm name
        farm_name = generate_farm_name()
        
        # Select state and region
        state = random.choice(US_STATES)
        if state in FARM_REGIONS:
            region, base_lat, base_lng = random.choice(FARM_REGIONS[state])
        else:
            # Generate approximate coordinates for other states
            base_lat = random.uniform(25.0, 49.0)  # US latitude range
            base_lng = random.uniform(-125.0, -66.0)  # US longitude range
            region = f"Agricultural Region {i+1}"
        
        # Generate address
        street_address = generate_farm_address(state)
        
        # Generate city name (often smaller towns in rural areas)
        rural_cities = ["Farmville", "Rural Center", "Agri Town", "Farm City", "Rural Valley"]
        city = random.choice(rural_cities) if random.random() < 0.3 else f"Rural City {i+1}"
        
        # Generate zip code
        zip_code = str(random.randint(10000, 99999))
        
        # Generate phone and website
        phone = generate_phone()
        clean_name = farm_name.replace(" ", "").replace(".", "").replace(",", "").lower()
        website = f"www.{clean_name}.com"
        
        # Generate farm-specific fields
        farm_type = random.choice(FARM_TYPES)
        acres = random.randint(50, 5000)
        annual_revenue = random.randint(100000, 10000000)
        employees = random.randint(1, 50)
        
        # Generate equipment and specialties
        equipment = random.choice(FARM_EQUIPMENT)
        
        # Generate dates
        created_date = datetime.now() - timedelta(days=random.randint(1, 365*5))
        last_activity = datetime.now() - timedelta(days=random.randint(1, 180))
        
        # Generate description
        descriptions = [
            f"Family-owned {farm_type.lower()} specializing in {equipment.lower()}",
            f"Multi-generational {farm_type.lower()} with {acres} acres",
            f"Modern {farm_type.lower()} using sustainable practices",
            f"Established {farm_type.lower()} serving the {state} region",
            f"Premium {farm_type.lower()} with state-of-the-art {equipment.lower()}"
        ]
        description = random.choice(descriptions)
        
        farm = {
            "Account Name": farm_name,
            "Record Type": "Farm",
            "Record Type ID": "012KY0000001OFfYAM",
            "Agriculture Type": farm_type,
            "Industry": "Agriculture",
            "Billing Street": street_address,
            "Billing City": city,
            "Billing State": state,
            "Billing Postal Code": zip_code,
            "Billing Country": "United States",
            "Phone": phone,
            "Website": website,
            "Annual Revenue": annual_revenue,
            "Number of Employees": employees,
            "Description": description,
            "Rating": random.choice(["Hot", "Warm", "Cold"]),
            "Customer Priority": random.choice(["High", "Medium", "Low"]),
            "SLA": random.choice(["Gold", "Silver", "Bronze"]),
            "Upsell Opportunity": random.choice(["Maybe", "No", "Yes"]),
            "Active": "Yes",
            "Created Date": created_date.strftime("%Y-%m-%d"),
            "Last Activity Date": last_activity.strftime("%Y-%m-%d"),
            "Billing Latitude": round(base_lat + random.uniform(-0.5, 0.5), 6),
            "Billing Longitude": round(base_lng + random.uniform(-0.5, 0.5), 6),
            "Farm Size (Acres)": acres,
            "Primary Equipment": equipment,
            "Farming Region": region,
            "Certification": random.choice(["Organic", "Conventional", "GAP Certified", "None"]),
            "Water Source": random.choice(["Well", "Irrigation District", "River", "Lake", "Municipal"]),
            "Soil Type": random.choice(["Loam", "Clay", "Sandy", "Silt", "Mixed"])
        }
        
        farms.append(farm)
    
    return farms

def save_to_csv(data, filename):
    """Save data to CSV file"""
    if not data:
        return
    
    fieldnames = data[0].keys()
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    print("Generating Agriculture Farm Data...")
    
    # Generate 50 farm records
    farms = generate_farm_data(50)
    
    # Save to CSV
    filename = "data/agriculture_farms.csv"
    save_to_csv(farms, filename)
    
    print(f"✅ Generated {len(farms)} farm records")
    print(f"📁 Saved to: {filename}")
    print(f"📍 States covered: {len(set(f['Billing State'] for f in farms))}")
    print(f"🏡 Farm types: {len(set(f['Agriculture Type'] for f in farms))}")
    
    # Show sample data
    print("\n📋 Sample Records:")
    for i, farm in enumerate(farms[:3]):
        print(f"\n{i+1}. {farm['Account Name']}")
        print(f"   📍 {farm['Billing City']}, {farm['Billing State']}")
        print(f"   🏡 {farm['Agriculture Type']}")
        print(f"   📞 {farm['Phone']}")
        print(f"   🌐 {farm['Website']}")
        print(f"   📍 Coordinates: {farm['Billing Latitude']}, {farm['Billing Longitude']}")
        print(f"   🌾 Size: {farm['Farm Size (Acres)']} acres")
        print(f"   🚜 Equipment: {farm['Primary Equipment']}") 