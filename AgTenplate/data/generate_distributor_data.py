#!/usr/bin/env python3
"""
Generate Agriculture Company Distributor Data for Salesforce Account Object
Creates realistic distributor data with US addresses and geo coordinates
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

# Major cities in agriculture states with approximate coordinates
CITIES_DATA = {
    "California": [
        ("Fresno", 36.7378, -119.7871),
        ("Bakersfield", 35.3733, -119.0187),
        ("Modesto", 37.6391, -120.9969),
        ("Stockton", 37.9577, -121.2908),
        ("Sacramento", 38.5816, -121.4944)
    ],
    "Iowa": [
        ("Des Moines", 41.5868, -93.6250),
        ("Cedar Rapids", 41.9779, -91.6656),
        ("Davenport", 41.5236, -90.5776),
        ("Sioux City", 42.4963, -96.4049),
        ("Waterloo", 42.4928, -92.3426)
    ],
    "Illinois": [
        ("Chicago", 41.8781, -87.6298),
        ("Springfield", 39.7817, -89.6501),
        ("Peoria", 40.6936, -89.5890),
        ("Rockford", 42.2711, -89.0940),
        ("Champaign", 40.1164, -88.2434)
    ],
    "Texas": [
        ("Houston", 29.7604, -95.3698),
        ("Dallas", 32.7767, -96.7970),
        ("Austin", 30.2672, -97.7431),
        ("San Antonio", 29.4241, -98.4936),
        ("Fort Worth", 32.7555, -97.3308)
    ],
    "Florida": [
        ("Miami", 25.7617, -80.1918),
        ("Orlando", 28.5383, -81.3792),
        ("Tampa", 27.9506, -82.4572),
        ("Jacksonville", 30.3322, -81.6557),
        ("Tallahassee", 30.4383, -84.2807)
    ]
}

# Agriculture company types
COMPANY_TYPES = [
    "Seed Distributor", "Fertilizer Supplier", "Equipment Dealer", 
    "Crop Protection", "Irrigation Systems", "Grain Handler",
    "Feed Supplier", "Chemical Distributor", "Machinery Parts",
    "Organic Products", "Precision Agriculture", "Livestock Equipment"
]

# Company name prefixes and suffixes
COMPANY_PREFIXES = [
    "Agri", "Farm", "Crop", "Green", "Harvest", "Grow", "Seed", "Grain",
    "Valley", "River", "Prairie", "Plains", "Midwest", "Southern", "Western"
]

COMPANY_SUFFIXES = [
    "Supply Co.", "Distributors", "Services", "Solutions", "Partners",
    "Enterprises", "Group", "Inc.", "LLC", "Corp.", "Company"
]

# Street names
STREET_NAMES = [
    "Main", "Oak", "Maple", "Pine", "Cedar", "Elm", "Washington", "Lincoln",
    "Jefferson", "Adams", "Madison", "Monroe", "Jackson", "Van Buren",
    "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce"
]

STREET_TYPES = ["St", "Ave", "Blvd", "Dr", "Ln", "Rd", "Way", "Pl", "Ct"]

def generate_phone():
    """Generate a realistic US phone number"""
    area_codes = ["515", "319", "563", "712", "641", "319", "515", "712", "641", "319"]
    area = random.choice(area_codes)
    prefix = str(random.randint(200, 999))
    suffix = str(random.randint(1000, 9999))
    return f"({area}) {prefix}-{suffix}"

def generate_website(company_name):
    """Generate a website URL based on company name"""
    clean_name = company_name.replace(" ", "").replace(".", "").replace(",", "").lower()
    return f"www.{clean_name}.com"

def generate_distributor_data(num_records=50):
    """Generate distributor data for Salesforce Account object"""
    
    distributors = []
    
    for i in range(num_records):
        # Generate company name
        prefix = random.choice(COMPANY_PREFIXES)
        suffix = random.choice(COMPANY_SUFFIXES)
        company_name = f"{prefix} {suffix}"
        
        # Select state and city
        state = random.choice(US_STATES)
        if state in CITIES_DATA:
            city, lat, lng = random.choice(CITIES_DATA[state])
        else:
            # Generate approximate coordinates for other states
            lat = random.uniform(25.0, 49.0)  # US latitude range
            lng = random.uniform(-125.0, -66.0)  # US longitude range
            city = f"City{i+1}"
        
        # Generate address
        street_num = random.randint(100, 9999)
        street_name = random.choice(STREET_NAMES)
        street_type = random.choice(STREET_TYPES)
        street_address = f"{street_num} {street_name} {street_type}"
        
        # Generate zip code
        zip_code = str(random.randint(10000, 99999))
        
        # Generate phone and website
        phone = generate_phone()
        website = generate_website(company_name)
        
        # Generate other fields
        company_type = random.choice(COMPANY_TYPES)
        annual_revenue = random.randint(1000000, 50000000)
        employees = random.randint(10, 500)
        
        # Generate dates
        created_date = datetime.now() - timedelta(days=random.randint(1, 365*3))
        last_activity = datetime.now() - timedelta(days=random.randint(1, 90))
        
        distributor = {
            "Account Name": company_name,
            "Record Type": "Distributor",
            "Record Type ID": "012KY0000001OFdYAM",
            "Agriculture Type": company_type,
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
            "Description": f"Leading {company_type.lower()} serving the {state} region",
            "Rating": random.choice(["Hot", "Warm", "Cold"]),
            "Customer Priority": random.choice(["High", "Medium", "Low"]),
            "SLA": random.choice(["Gold", "Silver", "Bronze"]),
            "Upsell Opportunity": random.choice(["Maybe", "No", "Yes"]),
            "Active": "Yes",
            "Created Date": created_date.strftime("%Y-%m-%d"),
            "Last Activity Date": last_activity.strftime("%Y-%m-%d"),
            "Billing Latitude": round(lat + random.uniform(-0.1, 0.1), 6),
            "Billing Longitude": round(lng + random.uniform(-0.1, 0.1), 6)
        }
        
        distributors.append(distributor)
    
    return distributors

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
    print("Generating Agriculture Distributor Data...")
    
    # Generate 50 distributor records
    distributors = generate_distributor_data(50)
    
    # Save to CSV
    filename = "data/agriculture_distributors.csv"
    save_to_csv(distributors, filename)
    
    print(f"✅ Generated {len(distributors)} distributor records")
    print(f"📁 Saved to: {filename}")
    print(f"📍 States covered: {len(set(d['Billing State'] for d in distributors))}")
    print(f"🏢 Company types: {len(set(d['Agriculture Type'] for d in distributors))}")
    
    # Show sample data
    print("\n📋 Sample Records:")
    for i, dist in enumerate(distributors[:3]):
        print(f"\n{i+1}. {dist['Account Name']}")
        print(f"   📍 {dist['Billing City']}, {dist['Billing State']}")
        print(f"   🏢 {dist['Agriculture Type']}")
        print(f"   📞 {dist['Phone']}")
        print(f"   🌐 {dist['Website']}")
        print(f"   📍 Coordinates: {dist['Billing Latitude']}, {dist['Billing Longitude']}") 