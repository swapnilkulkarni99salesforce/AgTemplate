#!/usr/bin/env python3
"""
Generate Farmer Contact Data for Farm Accounts
This script creates realistic farmer contact information to be associated with farm accounts
"""

import csv
import random
from datetime import datetime, timedelta
import os

# Farmer-specific data
FARMER_FIRST_NAMES = [
    "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Christopher", "Charles",
    "Daniel", "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua", "Kenneth",
    "Kevin", "Brian", "George", "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob",
    "Gary", "Nicholas", "Eric", "Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon", "Benjamin",
    "Frank", "Gregory", "Raymond", "Samuel", "Patrick", "Alexander", "Jack", "Dennis", "Jerry", "Tyler",
    "Aaron", "Jose", "Adam", "Nathan", "Henry", "Douglas", "Zachary", "Peter", "Kyle", "Walter",
    "Ethan", "Jeremy", "Harold", "Carl", "Keith", "Roger", "Gerald", "Christian", "Terry", "Sean",
    "Arthur", "Austin", "Noah", "Lawrence", "Jesse", "Joe", "Bryan", "Billy", "Jordan", "Albert",
    "Dylan", "Bruce", "Willie", "Gabriel", "Alan", "Juan", "Logan", "Wayne", "Roy", "Ralph",
    "Randy", "Eugene", "Vincent", "Russell", "Elijah", "Louis", "Bobby", "Philip", "Johnny"
]

FARMER_LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
    "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
    "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
    "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
    "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez"
]

FARMER_TITLES = [
    "Owner", "Farm Manager", "Operations Manager", "General Manager", "President", "CEO", "Proprietor",
    "Managing Partner", "Director", "Supervisor", "Lead Farmer", "Senior Manager", "Executive Director"
]

FARMER_DEPARTMENTS = [
    "Operations", "Management", "Production", "Field Operations", "Farm Management", "General Management"
]

FARMER_DESCRIPTIONS = [
    "Experienced farmer with over 20 years in agriculture",
    "Multi-generational farmer specializing in sustainable practices",
    "Farm owner with expertise in modern farming techniques",
    "Agricultural professional with focus on crop management",
    "Seasoned farmer with deep knowledge of local farming conditions",
    "Farm manager with strong background in livestock operations",
    "Agricultural specialist with expertise in organic farming",
    "Farm owner with experience in precision agriculture",
    "Senior farmer with knowledge of irrigation systems",
    "Agricultural professional with focus on soil management"
]

def generate_phone():
    """Generate a realistic phone number"""
    area_codes = ["319", "515", "641", "712", "563"]
    area_code = random.choice(area_codes)
    prefix = str(random.randint(200, 999))
    suffix = str(random.randint(1000, 9999))
    return f"({area_code}) {prefix}-{suffix}"

def generate_email(first_name, last_name, company_name):
    """Generate a realistic email address"""
    email_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    domain = random.choice(email_domains)
    
    # Clean company name for email
    clean_company = company_name.replace(" ", "").replace(",", "").replace(".", "").lower()
    
    email_patterns = [
        f"{first_name.lower()}.{last_name.lower()}@{domain}",
        f"{first_name.lower()}{last_name.lower()}@{domain}",
        f"{first_name.lower()}_{last_name.lower()}@{domain}",
        f"{first_name.lower()}{random.randint(1, 99)}@{domain}",
        f"{first_name.lower()}.{last_name.lower()}@{clean_company}.com"
    ]
    
    return random.choice(email_patterns)

def generate_farmer_contact_data(num_records=50):
    """Generate farmer contact data"""
    contacts = []
    
    # Get existing farm accounts to associate with
    farm_accounts = []
    try:
        with open('data/agriculture_farms.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                farm_accounts.append({
                    'Account Name': row['Account Name'],
                    'Account ID': f"001{random.randint(100000000, 999999999)}"  # Mock ID
                })
    except FileNotFoundError:
        # Create sample farm accounts if file doesn't exist
        farm_accounts = [
            {'Account Name': 'Miller Big Valley', 'Account ID': '001KY00000E1Q8CYAV'},
            {'Account Name': 'Cedar Estates', 'Account ID': '001KY00000E1Q8DYAV'},
            {'Account Name': 'Elm Fields', 'Account ID': '001KY00000E1Q8EYAV'},
            {'Account Name': 'Mountain Hills', 'Account ID': '001KY00000E1Q8FYAV'},
            {'Account Name': 'Birch Produce', 'Account ID': '001KY00000E1Q8GYAV'}
        ]
    
    for i in range(num_records):
        # Select a farm account
        farm_account = random.choice(farm_accounts)
        
        # Generate contact details
        first_name = random.choice(FARMER_FIRST_NAMES)
        last_name = random.choice(FARMER_LAST_NAMES)
        title = random.choice(FARMER_TITLES)
        department = random.choice(FARMER_DEPARTMENTS)
        
        # Generate contact info
        phone = generate_phone()
        email = generate_email(first_name, last_name, farm_account['Account Name'])
        
        # Generate dates
        created_date = datetime.now() - timedelta(days=random.randint(30, 1000))
        last_activity = datetime.now() - timedelta(days=random.randint(1, 90))
        
        # Generate mailing address (same as farm address with slight variations)
        states = ["California", "Texas", "Iowa", "Nebraska", "Minnesota", "Illinois", "Wisconsin", "Indiana", "Ohio", "Michigan"]
        state = random.choice(states)
        
        street_numbers = [str(random.randint(100, 9999)), str(random.randint(10000, 99999))]
        street_names = ["Farm Road", "Rural Route", "County Road", "Dirt Road", "Spring Road", "Valley Road"]
        
        street_address = f"{random.choice(street_numbers)} {random.choice(street_names)}"
        city = f"Rural City {random.randint(1, 50)}"
        zip_code = str(random.randint(10000, 99999))
        
        # Generate coordinates (slightly different from farm coordinates)
        base_lat = random.uniform(25.0, 50.0)
        base_lng = random.uniform(-125.0, -65.0)
        
        contact = {
            "Account Name": farm_account['Account Name'],
            "Account ID": farm_account['Account ID'],
            "First Name": first_name,
            "Last Name": last_name,
            "Title": title,
            "Department": department,
            "Phone": phone,
            "Email": email,
            "Mailing Street": street_address,
            "Mailing City": city,
            "Mailing State": state,
            "Mailing Postal Code": zip_code,
            "Mailing Country": "United States",
            "Mailing Latitude": round(base_lat + random.uniform(-0.1, 0.1), 6),
            "Mailing Longitude": round(base_lng + random.uniform(-0.1, 0.1), 6),
            "Description": random.choice(FARMER_DESCRIPTIONS),
            "Lead Source": random.choice(["Web", "Phone Inquiry", "Referral", "Trade Show", "Cold Call"]),
            "Status": "Active",
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
    
    print(f"✅ Generated {len(data)} farmer contact records")
    print(f"📁 Saved to: {filename}")

def main():
    """Main function to generate farmer contact data"""
    print("🌾 Generating Farmer Contact Data...")
    
    # Generate farmer contacts
    farmer_contacts = generate_farmer_contact_data(50)
    
    # Save to CSV
    save_to_csv(farmer_contacts, 'data/farmer_contacts.csv')
    
    # Display statistics
    print(f"📍 States covered: {len(set(c['Mailing State'] for c in farmer_contacts))}")
    print(f"🏢 Farm accounts associated: {len(set(c['Account Name'] for c in farmer_contacts))}")
    print(f"👨‍🌾 Farmer titles: {len(set(c['Title'] for c in farmer_contacts))}")
    
    # Show sample data
    print("\n📋 Sample Farmer Contacts:")
    for i, contact in enumerate(farmer_contacts[:3]):
        print(f"\n{i+1}. {contact['First Name']} {contact['Last Name']}")
        print(f"   🏢 Farm: {contact['Account Name']}")
        print(f"   💼 Title: {contact['Title']}")
        print(f"   📞 Phone: {contact['Phone']}")
        print(f"   📧 Email: {contact['Email']}")
        print(f"   📍 Location: {contact['Mailing City']}, {contact['Mailing State']}")

if __name__ == "__main__":
    main() 