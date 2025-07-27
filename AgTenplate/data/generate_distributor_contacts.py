#!/usr/bin/env python3
"""
Generate Distributor Contact Data for Distributor Accounts
This script creates realistic distributor contact information to be associated with distributor accounts
"""

import csv
import random
from datetime import datetime, timedelta
import os

# Distributor-specific data
DISTRIBUTOR_FIRST_NAMES = [
    "Sarah", "Jennifer", "Michael", "Jessica", "David", "Amanda", "James", "Ashley", "Robert", "Stephanie",
    "John", "Nicole", "William", "Elizabeth", "Richard", "Megan", "Joseph", "Lauren", "Thomas", "Amber",
    "Christopher", "Brittany", "Charles", "Danielle", "Daniel", "Rachel", "Matthew", "Heather", "Anthony", "Michelle",
    "Mark", "Tiffany", "Donald", "Melissa", "Steven", "Christine", "Paul", "Kelly", "Andrew", "Emily",
    "Joshua", "Rebecca", "Kenneth", "Laura", "Kevin", "Shannon", "Brian", "Angela", "George", "Kimberly",
    "Edward", "Amy", "Ronald", "Crystal", "Timothy", "Natalie", "Jason", "Heidi", "Jeffrey", "Tracy",
    "Ryan", "Lisa", "Jacob", "Erica", "Gary", "Stacy", "Nicholas", "Wendy", "Eric", "Carrie",
    "Jonathan", "Dawn", "Stephen", "Carla", "Larry", "Monica", "Justin", "Eva", "Scott", "Suzanne",
    "Brandon", "Cheryl", "Benjamin", "Joyce", "Frank", "Virginia", "Gregory", "Victoria", "Raymond", "Brenda",
    "Samuel", "Cynthia", "Patrick", "Sally", "Alexander", "Katherine", "Jack", "Emma", "Dennis", "Deborah"
]

DISTRIBUTOR_LAST_NAMES = [
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

DISTRIBUTOR_TITLES = [
    "Sales Manager", "Account Executive", "Sales Representative", "Business Development Manager", "Regional Manager",
    "Sales Director", "Account Manager", "Sales Consultant", "Territory Manager", "Sales Specialist",
    "Customer Success Manager", "Sales Coordinator", "Business Development Representative", "Sales Engineer",
    "Key Account Manager", "Inside Sales Representative", "Field Sales Representative", "Sales Operations Manager"
]

DISTRIBUTOR_DEPARTMENTS = [
    "Sales", "Business Development", "Customer Success", "Account Management", "Sales Operations",
    "Territory Sales", "Inside Sales", "Field Sales", "Key Accounts", "Sales Support"
]

DISTRIBUTOR_DESCRIPTIONS = [
    "Experienced sales professional with expertise in agriculture distribution",
    "Account manager specializing in farm equipment and supplies",
    "Sales representative with strong background in agricultural products",
    "Business development professional focused on expanding market reach",
    "Territory manager with deep knowledge of local farming communities",
    "Sales specialist with expertise in precision agriculture solutions",
    "Account executive with experience in livestock equipment sales",
    "Sales consultant specializing in irrigation and crop protection",
    "Regional manager with strong relationships in the agriculture sector",
    "Customer success manager focused on long-term client partnerships"
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
        f"{first_name.lower()}.{last_name.lower()}@{clean_company}.com",
        f"{first_name.lower()}.{last_name.lower()}@company.com"
    ]
    
    return random.choice(email_patterns)

def generate_distributor_contact_data(num_records=50):
    """Generate distributor contact data"""
    contacts = []
    
    # Get existing distributor accounts to associate with
    distributor_accounts = []
    try:
        with open('data/agriculture_distributors.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                distributor_accounts.append({
                    'Account Name': row['Account Name'],
                    'Account ID': f"001{random.randint(100000000, 999999999)}"  # Mock ID
                })
    except FileNotFoundError:
        # Create sample distributor accounts if file doesn't exist
        distributor_accounts = [
            {'Account Name': 'Plains Enterprises', 'Account ID': '001KY00000E1Q82YAF'},
            {'Account Name': 'Southern Inc', 'Account ID': '001KY00000E1Q83YAF'},
            {'Account Name': 'Harvest Enterprises', 'Account ID': '001KY00000E1Q84YAF'},
            {'Account Name': 'Farm Supply Co', 'Account ID': '001KY00000E1Q89YAF'},
            {'Account Name': 'Grain Solutions', 'Account ID': '001KY00000E1Q8AYAV'}
        ]
    
    for i in range(num_records):
        # Select a distributor account
        distributor_account = random.choice(distributor_accounts)
        
        # Generate contact details
        first_name = random.choice(DISTRIBUTOR_FIRST_NAMES)
        last_name = random.choice(DISTRIBUTOR_LAST_NAMES)
        title = random.choice(DISTRIBUTOR_TITLES)
        department = random.choice(DISTRIBUTOR_DEPARTMENTS)
        
        # Generate contact info
        phone = generate_phone()
        email = generate_email(first_name, last_name, distributor_account['Account Name'])
        
        # Generate dates
        created_date = datetime.now() - timedelta(days=random.randint(30, 1000))
        last_activity = datetime.now() - timedelta(days=random.randint(1, 90))
        
        # Generate mailing address (same as distributor address with slight variations)
        states = ["California", "Texas", "Iowa", "Nebraska", "Minnesota", "Illinois", "Wisconsin", "Indiana", "Ohio", "Michigan"]
        state = random.choice(states)
        
        street_numbers = [str(random.randint(100, 9999)), str(random.randint(10000, 99999))]
        street_names = ["Main St", "Oak Ave", "Pine Blvd", "Maple Dr", "Cedar Ln", "Elm Way", "Washington St", "Jefferson Ave"]
        
        street_address = f"{random.choice(street_numbers)} {random.choice(street_names)}"
        city = f"City{random.randint(1, 50)}"
        zip_code = str(random.randint(10000, 99999))
        
        # Generate coordinates (slightly different from distributor coordinates)
        base_lat = random.uniform(25.0, 50.0)
        base_lng = random.uniform(-125.0, -65.0)
        
        contact = {
            "Account Name": distributor_account['Account Name'],
            "Account ID": distributor_account['Account ID'],
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
            "Description": random.choice(DISTRIBUTOR_DESCRIPTIONS),
            "Lead Source": random.choice(["Web", "Phone Inquiry", "Referral", "Trade Show", "Cold Call", "Partner"]),
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
    
    print(f"✅ Generated {len(data)} distributor contact records")
    print(f"📁 Saved to: {filename}")

def main():
    """Main function to generate distributor contact data"""
    print("🏢 Generating Distributor Contact Data...")
    
    # Generate distributor contacts
    distributor_contacts = generate_distributor_contact_data(50)
    
    # Save to CSV
    save_to_csv(distributor_contacts, 'data/distributor_contacts.csv')
    
    # Display statistics
    print(f"📍 States covered: {len(set(c['Mailing State'] for c in distributor_contacts))}")
    print(f"🏢 Distributor accounts associated: {len(set(c['Account Name'] for c in distributor_contacts))}")
    print(f"👔 Distributor titles: {len(set(c['Title'] for c in distributor_contacts))}")
    
    # Show sample data
    print("\n📋 Sample Distributor Contacts:")
    for i, contact in enumerate(distributor_contacts[:3]):
        print(f"\n{i+1}. {contact['First Name']} {contact['Last Name']}")
        print(f"   🏢 Distributor: {contact['Account Name']}")
        print(f"   💼 Title: {contact['Title']}")
        print(f"   📞 Phone: {contact['Phone']}")
        print(f"   📧 Email: {contact['Email']}")
        print(f"   📍 Location: {contact['Mailing City']}, {contact['Mailing State']}")

if __name__ == "__main__":
    main() 