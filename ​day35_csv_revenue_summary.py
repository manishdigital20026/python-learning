# Day 35: Calculate Total Revenue from Parking CSV

import csv
import os

file_name = "parking_records.csv"

# Step 1: Ensure initial sample records exist with payments
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Vehicle_No", "Driver_Name", "Bill_Amount", "Status"])
        writer.writerow(["KA-01-AB-1111", "Amit", "60", "Paid"])
        writer.writerow(["DL-02-XY-2222", "Manish", "100", "Paid"])
        writer.writerow(["MH-12-PQ-3333", "Pooja", "40", "Paid"])
        writer.writerow(["HR-26-BR-4444", "Rahul", "80", "Pending"])

print("--- End of Shift Revenue Audit ---")

total_collected = 0
total_pending = 0
paid_count = 0

# Step 2: Read CSV and calculate sums
with open(file_name, "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    for row in reader:
        if row:
            amount = int(row[2])  # Convert string to integer for arithmetic
            status = row[3].strip()

            if status == "Paid":
                total_collected += amount
                paid_count += 1
            elif status == "Pending":
                total_pending += amount

# Step 3: Print structured audit report
print("\n==============================")
print("     DAILY REVENUE REPORT     ")
print("==============================")
print("Total Paid Vehicles :", paid_count)
print("Total Cash Collected: Rs.", total_collected)
print("Outstanding Pending : Rs.", total_pending)
print("Projected Total     : Rs.", total_collected + total_pending)
print("==============================")
