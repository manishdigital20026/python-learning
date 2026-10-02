# Day 38: Bulletproof Input Validation with try-except

import csv
import os

file_name = "parking_records.csv"

# Function to safely get a positive integer input without crashing
def get_valid_fee():
    while True:
        raw_fee = input("Enter Parking Fee (Numbers only, e.g. 50): ").strip()
        try:
            fee = int(raw_fee)
            if fee >= 0:
                return fee
            else:
                print("[ERROR] Fee cannot be negative. Try again.")
        except ValueError:
            print(f"[INVALID INPUT] '{raw_fee}' is not a valid number! Please enter digits only.")

# Function to safely register a vehicle with validation
def register_vehicle():
    vehicle_plate = input("Enter Vehicle Plate (e.g., KA-05-MN-5555): ").strip().upper()
    driver_name = input("Enter Driver Name: ").strip()
    
    # Using our crash-proof numeric validator
    validated_fee = get_valid_fee()
    
    # Append safely to CSV
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([vehicle_plate, driver_name, validated_fee, "Pending"])
        
    print(f"\n[SUCCESS] Vehicle {vehicle_plate} logged safely with Fee: Rs. {validated_fee}")

# Test Run Simulation
print("--- Gate Entry: Crash-Proof Input System ---")
register_vehicle()

# Display updated contents
print("\n--- Current Parking Database ---")
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
