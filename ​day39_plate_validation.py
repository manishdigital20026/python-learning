# Day 39: Vehicle Registration Plate Format Validation

import csv
import os

file_name = "parking_records.csv"

# Function to check and standardize vehicle plate format
def get_valid_plate():
    while True:
        raw_plate = input("Enter Vehicle Plate (e.g. KA-01-AB-1234): ").strip().upper()
        
        # Remove dashes and spaces to evaluate core characters
        cleaned = raw_plate.replace("-", "").replace(" ", "")
        
        # Validation checks:
        # 1. Non-empty
        # 2. Must contain only letters and digits (isalnum)
        # 3. Standard length typically falls between 8 and 10 characters
        if not cleaned:
            print("[ERROR] Plate cannot be empty. Try again.")
        elif not cleaned.isalnum():
            print("[ERROR] Plate must only contain letters, numbers, and dashes. Try again.")
        elif not (8 <= len(cleaned) <= 10):
            print(f"[ERROR] Invalid length ({len(cleaned)} chars). Standard Indian plates have 8-10 characters.")
        else:
            # Valid plate accepted
            return raw_plate

# Function to record entry with validated plate
def register_entry():
    print("--- Vehicle Check-In Desk ---")
    plate = get_valid_plate()
    driver = input("Enter Driver Name: ").strip()
    
    # Save directly to CSV
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([plate, driver, "50", "Pending"])
        
    print(f"\n[SUCCESS] Validated vehicle plate '{plate}' saved successfully!\n")

# Run test
register_entry()

# Print current file status
if os.path.exists(file_name):
    print("--- Current Database Sample ---")
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
