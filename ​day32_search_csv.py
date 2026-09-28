# Day 32: Search Vehicle Record Inside a CSV File

import csv
import os

file_name = "parking_records.csv"

# Step 1: Ensure sample data exists for testing
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Vehicle_No", "Driver_Name", "Bill_Amount", "Status"])
        writer.writerow(["KA-01-AB-1111", "Amit", "60", "Paid"])
        writer.writerow(["DL-02-XY-2222", "Manish", "100", "Paid"])
        writer.writerow(["MH-12-PQ-3333", "Pooja", "40", "Paid"])

print("--- Parking Record Lookup System ---")

# Step 2: User input for vehicle search
search_plate = input("Enter Vehicle Number to search: ")

found = False

# Step 3: Read CSV line-by-line and match column index 0 (Vehicle_No)
with open(file_name, "r") as file:
    reader = csv.reader(file)
    
    # Skip the header row
    header = next(reader)
    
    for row in reader:
        # Check if the search term matches the first column (Vehicle_No)
        if row and row[0].strip().upper() == search_plate.strip().upper():
            print("\n[MATCH FOUND]")
            print("Vehicle Plate :", row[0])
            print("Driver Name   :", row[1])
            print("Bill Amount   : Rs.", row[2])
            print("Status        :", row[3])
            found = True
            break

# Step 4: Handle search misses
if not found:
    print("\n[NOT FOUND] No record matches vehicle number:", search_plate)
