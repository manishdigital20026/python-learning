# Day 40: Prevent Duplicate Active Vehicle Check-Ins

import csv
import os

file_name = "parking_records.csv"

# Step 1: Ensure initial sample records exist
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Vehicle_No", "Driver_Name", "Bill_Amount", "Status"])
        writer.writerow(["KA-01-AB-1111", "Amit", "60", "Pending"])
        writer.writerow(["DL-02-XY-2222", "Manish", "100", "Paid"])

# Step 2: Retrieve all currently parked (active) vehicle plates
def get_currently_parked_plates():
    active_plates = []
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row safely
            for row in reader:
                if row and len(row) >= 4:
                    plate = row[0].strip().upper()
                    status = row[3].strip()
                    # Only vehicles with 'Pending' status are still inside
                    if status == "Pending":
                        active_plates.append(plate)
    return active_plates

# Step 3: Attempt a new check-in with duplicate prevention
def register_vehicle_entry():
    print("--- Secure Gate Entry Desk ---")
    active_vehicles = get_currently_parked_plates()
    
    new_plate = input("Enter Vehicle Plate (e.g. KA-01-AB-1111): ").strip().upper()

    # Duplicate check: Is the vehicle already inside?
    if new_plate in active_vehicles:
        print(f"\n[ALERT - DUPLICATE ENTRY] Vehicle '{new_plate}' is ALREADY inside the parking area!")
        print("Please check out the vehicle before creating a new entry.")
        return

    driver = input("Enter Driver Name: ").strip()
    rate = "50"

    # Append new entry to the database
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([new_plate, driver, rate, "Pending"])

    print(f"\n[SUCCESS] Vehicle '{new_plate}' checked in successfully!")

# Run the test
register_vehicle_entry()

# Step 4: Display current status of all records
print("\n--- Current Parking Database ---")
with open(file_name, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
