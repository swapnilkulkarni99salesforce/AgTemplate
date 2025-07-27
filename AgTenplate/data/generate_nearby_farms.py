#!/usr/bin/env python3
"""
Generate Farm Records Near Sunny Estates
This script creates farm records within 10km radius of Sunny Estates and associated farmer contacts
"""

import csv
import random
import math
from datetime import datetime, timedelta
import os

# Sunny Estates coordinates
SUNNY_ESTATES_LAT = 36.026995
SUNNY_ESTATES_LNG = -100.695679

# Farm names for nearby farms
NEARBY_FARM_NAMES = [
    "Sunny Valley Farm", "Golden Meadows", "Prairie View Ranch", "Sunset Fields", "Morning Star Farm",
    "Green Valley Estates", "Blue Sky Ranch", "Silver Creek Farm", "Red River Valley", "Clear Water Farm",
    "High Plains Ranch", "Windy Meadows", "Rocky Ridge Farm", "Sweet Grass Ranch", "Lone Star Farm",
    "Texas Prairie Farm", "Oklahoma Valley", "Panhandle Ranch", "Wheat Field Farm", "Corn Belt Ranch"
]

# Farmer names for nearby farms
FARMER_FIRST_NAMES = [
    "James", "Robert", "John", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Christopher",
    "Charles", "Daniel", "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua",
    "Kenneth", "Kevin", "Brian", "George", "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan"
]

FARMER_LAST_NAMES = [
    "Anderson", "Wilson", "Taylor", "Johnson", "White", "Martin", "Anderson", "Thompson", "Garcia", "Martinez",
    "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "King",
    "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter"
]

FARM_TYPES = [
    "Cattle Ranch", "Grain Farm", "Corn Farm", "Wheat Farm", "Mixed Crop Farm", "Dairy Farm",
    "Soybean Farm", "Cotton Farm", "Hay Farm", "Organic Farm"
]

EQUIPMENT_TYPES = [
    "Tractors", "Irrigation Systems", "Harvesters", "Planters", "Fertilizer Equipment", "Livestock Equipment",
    "Grain Storage", "Precision Agriculture", "Hay Equipment", "Dairy Equipment"
]

FARMING_REGIONS = [
    "Panhandle Region", "High Plains", "Red River Valley", "Wheat Belt", "Corn Belt", "Prairie Region",
    "Central Plains", "Northern Plains", "Southern Plains", "Eastern Plains"
]

def calculate_distance(lat1, lng1, lat2, lng2):
    """Calculate distance between two points in kilometers"""
    R = 6371  # Earth's radius in kilometers
    
    lat1, lng1, lat2, lng2 = map(math.radians, [lat1, lng1, lat2, lng2])
    dlat = lat2 - lat1
    dlng = lng2 - lng1
    
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    return R * c

def generate_nearby_coordinates(base_lat, base_lng, max_distance_km=10):
    """Generate coordinates within specified radius"""
    # Convert km to degrees (approximate)
    # 1 degree latitude ≈ 111 km
    # 1 degree longitude ≈ 111 km * cos(latitude)
    
    max_lat_offset = max_distance_km / 111.0
    max_lng_offset = max_distance_km / (111.0 * math.cos(math.radians(base_lat)))
    
    # Generate random offset within the circle
    angle = random.uniform(0, 2 * math.pi)
    distance = random.uniform(0, max_distance_km)
    
    lat_offset = (distance / 111.0) * math.cos(angle)
    lng_offset = (distance / (111.0 * math.cos(math.radians(base_lat)))) * math.sin(angle)
    
    new_lat = base_lat + lat_offset
    new_lng = base_lng + lng_offset
    
    return new_lat, new_lng

def generate_phone():
    """Generate a realistic phone number"""
    area_codes = ["580", "405", "918"]  # Oklahoma area codes
    area_code = random.choice(area_codes)
    prefix = str(random.randint(200, 999))
    suffix = str(random.randint(1000, 9999))
    return f"({area_code}) {prefix}-{suffix}"

def generate_email(first_name, last_name, farm_name):
    """Generate a realistic email address"""
    email_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    domain = random.choice(email_domains)
    
    clean_farm = farm_name.replace(" ", "").replace(",", "").replace(".", "").lower()
    
    email_patterns = [
        f"{first_name.lower()}.{last_name.lower()}@{domain}",
        f"{first_name.lower()}{last_name.lower()}@{domain}",
        f"{first_name.lower()}_{last_name.lower()}@{domain}",
        f"{first_name.lower()}.{last_name.lower()}@{clean_farm}.com"
    ]
    
    return random.choice(email_patterns)

def generate_nearby_farm_data(num_farms=15):
    """Generate farm data within 10km of Sunny Estates"""
    farms = []
    
    for i in range(num_farms):
        # Generate coordinates within 10km radius
        lat, lng = generate_nearby_coordinates(SUNNY_ESTATES_LAT, SUNNY_ESTATES_LNG, 10)
        
        # Calculate actual distance
        distance = calculate_distance(SUNNY_ESTATES_LAT, SUNNY_ESTATES_LNG, lat, lng)
        
        # Generate farm details
        farm_name = random.choice(NEARBY_FARM_NAMES)
        farm_type = random.choice(FARM_TYPES)
        equipment = random.choice(EQUIPMENT_TYPES)
        region = random.choice(FARMING_REGIONS)
        
        # Generate address
        street_numbers = [str(random.randint(100, 9999)), str(random.randint(10000, 99999))]
        street_names = ["Farm Road", "Rural Route", "County Road", "Dirt Road", "Spring Road", "Valley Road"]
        street_address = f"{random.choice(street_numbers)} {random.choice(street_names)}"
        
        # Use Oklahoma cities near the area
        cities = ["Guymon", "Hooker", "Goodwell", "Texhoma", "Turpin", "Hardesty", "Adams", "Balko", "Beaver"]
        city = random.choice(cities)
        
        zip_code = str(random.randint(73900, 73999))  # Oklahoma panhandle zip codes
        
        # Generate business data
        annual_revenue = random.randint(500000, 5000000)
        employees = random.randint(2, 25)
        
        # Generate dates
        created_date = datetime.now() - timedelta(days=random.randint(30, 1000))
        last_activity = datetime.now() - timedelta(days=random.randint(1, 90))
        
        farm = {
            "Account Name": farm_name,
            "Record Type": "Farm",
            "Record Type ID": "012KY0000001OFfYAM",
            "Agriculture Type": farm_type,
            "Industry": "Agriculture",
            "Billing Street": street_address,
            "Billing City": city,
            "Billing State": "Oklahoma",
            "Billing Postal Code": zip_code,
            "Billing Country": "United States",
            "Phone": generate_phone(),
            "Website": f"www.{farm_name.lower().replace(' ', '')}.com",
            "Annual Revenue": annual_revenue,
            "Number of Employees": employees,
            "Description": f"Family-owned {farm_type.lower()} located {distance:.1f}km from Sunny Estates",
            "Rating": random.choice(["Hot", "Warm", "Cold"]),
            "Customer Priority": random.choice(["High", "Medium", "Low"]),
            "SLA": random.choice(["Gold", "Silver", "Bronze"]),
            "Upsell Opportunity": random.choice(["Maybe", "No", "Yes"]),
            "Active": "Yes",
            "Created Date": created_date.strftime("%Y-%m-%d"),
            "Last Activity Date": last_activity.strftime("%Y-%m-%d"),
            "Billing Latitude": round(lat, 6),
            "Billing Longitude": round(lng, 6),
            "Farm Size (Acres)": random.randint(500, 5000),
            "Primary Equipment": equipment,
            "Farming Region": region,
            "Certification": random.choice(["Organic", "Conventional", "GAP Certified", "None"]),
            "Water Source": random.choice(["Well", "Irrigation District", "River", "Lake", "Municipal"]),
            "Soil Type": random.choice(["Loam", "Clay", "Sandy", "Silt", "Mixed"]),
            "Distance from Sunny Estates (km)": round(distance, 2)
        }
        
        farms.append(farm)
    
    return farms

def generate_nearby_farmer_contacts(farms):
    """Generate farmer contacts for the nearby farms"""
    contacts = []
    
    for farm in farms:
        # Generate farmer details
        first_name = random.choice(FARMER_FIRST_NAMES)
        last_name = random.choice(FARMER_LAST_NAMES)
        
        # Generate contact info
        phone = generate_phone()
        email = generate_email(first_name, last_name, farm['Account Name'])
        
        # Generate dates
        created_date = datetime.now() - timedelta(days=random.randint(30, 1000))
        last_activity = datetime.now() - timedelta(days=random.randint(1, 90))
        
        # Use same coordinates as farm with slight variation
        lat = farm['Billing Latitude'] + random.uniform(-0.01, 0.01)
        lng = farm['Billing Longitude'] + random.uniform(-0.01, 0.01)
        
        contact = {
            "Account Name": farm['Account Name'],
            "Account ID": f"001{random.randint(100000000, 999999999)}",  # Mock ID
            "First Name": first_name,
            "Last Name": last_name,
            "Title": random.choice(["Owner", "Farm Manager", "Operations Manager", "General Manager", "President"]),
            "Department": random.choice(["Operations", "Management", "Production", "Field Operations"]),
            "Phone": phone,
            "Email": email,
            "Mailing Street": farm['Billing Street'],
            "Mailing City": farm['Billing City'],
            "Mailing State": farm['Billing State'],
            "Mailing Postal Code": farm['Billing Postal Code'],
            "Mailing Country": "United States",
            "Mailing Latitude": round(lat, 6),
            "Mailing Longitude": round(lng, 6),
            "Description": f"Farmer at {farm['Account Name']}, {farm['Distance from Sunny Estates (km)']}km from Sunny Estates",
            "Lead Source": random.choice(["Web", "Phone Inquiry", "Referral", "Trade Show", "Cold Call"]),
            "Created Date": created_date.strftime("%Y-%m-%d"),
            "Last Activity Date": last_activity.strftime("%Y-%m-%d")
        }
        
        contacts.append(contact)
    
    return contacts

def save_to_csv(data, filename):
    """Save data to CSV file"""
    if not data:
        print("❌ No data to save")
        return
    
    fieldnames = data[0].keys()
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"✅ Generated {len(data)} records")
    print(f"📁 Saved to: {filename}")

def main():
    """Main function to generate nearby farm data"""
    print("🌾 Generating Farm Records Near Sunny Estates...")
    print(f"📍 Sunny Estates Location: {SUNNY_ESTATES_LAT}, {SUNNY_ESTATES_LNG}")
    print(f"🎯 Target Radius: 10km")
    
    # Generate farm data
    farms = generate_nearby_farm_data(15)
    
    # Generate farmer contacts
    farmer_contacts = generate_nearby_farmer_contacts(farms)
    
    # Save to CSV files
    save_to_csv(farms, 'data/nearby_farms.csv')
    save_to_csv(farmer_contacts, 'data/nearby_farmer_contacts.csv')
    
    # Display statistics
    print(f"\n📊 STATISTICS:")
    print(f"   🏢 Farms generated: {len(farms)}")
    print(f"   👨‍🌾 Farmer contacts: {len(farmer_contacts)}")
    print(f"   📍 Average distance: {sum(f['Distance from Sunny Estates (km)'] for f in farms) / len(farms):.1f}km")
    print(f"   🗺️  Max distance: {max(f['Distance from Sunny Estates (km)'] for f in farms):.1f}km")
    print(f"   🗺️  Min distance: {min(f['Distance from Sunny Estates (km)'] for f in farms):.1f}km")
    
    # Show sample data
    print(f"\n📋 SAMPLE FARMS:")
    for i, farm in enumerate(farms[:3]):
        print(f"\n{i+1}. {farm['Account Name']}")
        print(f"   🏡 Type: {farm['Agriculture Type']}")
        print(f"   📍 Location: {farm['Billing City']}, {farm['Billing State']}")
        print(f"   📏 Distance: {farm['Distance from Sunny Estates (km)']}km from Sunny Estates")
        print(f"   🌾 Size: {farm['Farm Size (Acres)']} acres")
        print(f"   🚜 Equipment: {farm['Primary Equipment']}")
        print(f"   📞 Phone: {farm['Phone']}")

if __name__ == "__main__":
    main() 