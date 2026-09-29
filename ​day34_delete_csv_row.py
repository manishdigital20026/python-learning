# Day 34: Remove Completed Parking Record from CSV File

import csv
import os

file_name = "parking_records.csv"

# Step 1: Ensure initial sample records exist
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Vehicle_No", "Driver_Name", "Bill_Amount", "Status"])
        writer.writerow(["KA-01-AB-1111", "Amit", "60", "Paid"])
        writer.writerow(["DL-02-XY-2222", "Manish", "100", "Paid"])
        writer.writerow(["MH-12-PQ-3333", "Pooja", "40", "Pending"])

print("--- Active Parking Checkout Counter ---")

# Step 2: Accept vehicle number to remove
target_vehicle = input("Enter Vehicle Number to remove/checkout: ")

retained_rows = []
deleted = False

# Step 3: Read CSV and keep rows that do NOT match the target vehicle
with open(file_name, "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    retained_rows.append(header)  # Preserve the table header

    for row in reader:
        if row:
            # If the row matches target vehicle, skip it (do not append)
            if row[0].strip().upper() == target_vehicle.strip().upper():
                deleted = True
                print("\n[REMOVED] Vehicle", row[0], "checked out and cleared from active register.")
            else:
                retained_rows.append(row)

# Step 4: Overwrite the CSV with the filtered list
if deleted:
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(retained_rows)
    print("[SUCCESS] Active parking list updated.")
else:
    print("\n[NOT FOUND] No record matched vehicle number:", target_vehicle)

# Step 5: Display the updated spreadsheet contents
print("\n--- Remaining Active Vehicles ---")
with open(file_name, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
