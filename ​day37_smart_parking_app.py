# Day 37: Complete Interactive Smart Parking Management System

import csv
import os
from datetime import datetime

file_name = "parking_records.csv"

# Function to initialize CSV with headers if it does not exist
def setup_storage():
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Vehicle_No", "Driver_Name", "Bill_Amount", "Status"])

# Function to register vehicle check-in
def vehicle_entry():
    v_no = input("Enter Vehicle Plate (e.g., KA-05-MN-5555): ").strip().upper()
    driver = input("Enter Driver Name: ").strip()
    rate = input("Enter Estimated Parking Fee (Rs.): ").strip()
    
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([v_no, driver, rate, "Pending"])
    print(f"\n[SUCCESS] Vehicle {v_no} registered with status 'Pending'.")

# Function to settle payment on vehicle exit
def settle_payment():
    target = input("Enter Vehicle Plate to mark 'Paid': ").strip().upper()
    rows = []
    found = False

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        rows.append(next(reader))  # Keep header
        for row in reader:
            if row and row[0].strip().upper() == target:
                row[3] = "Paid"
                found = True
            rows.append(row)

    if found:
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"\n[SUCCESS] Payment completed! Status for {target} updated to 'Paid'.")
    else:
        print(f"\n[NOT FOUND] No record found for vehicle plate: {target}")

# Function to display audit metrics
def show_audit():
    total_cash = 0
    total_pending = 0
    active_records = 0

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row:
                active_records += 1
                amt = int(row[2])
                if row[3].strip() == "Paid":
                    total_cash += amt
                else:
                    total_pending += amt

    print("\n" + "=" * 32)
    print("      LIVE PARKING AUDIT        ")
    print("=" * 32)
    print("Total Logged Vehicles :", active_records)
    print("Cash Collected        : Rs.", total_cash)
    print("Pending Settlements   : Rs.", total_pending)
    print("=" * 32)

# Main Application Loop
setup_storage()

while True:
    print("\n=== SMART PARKING CONTROL PANEL ===")
    print("1. New Vehicle Entry")
    print("2. Settle Vehicle Bill (Mark Paid)")
    print("3. View Live Revenue Audit")
    print("4. Exit System")
    
    choice = input("\nSelect an option (1-4): ").strip()

    if choice == "1":
        vehicle_entry()
    elif choice == "2":
        settle_payment()
    elif choice == "3":
        show_audit()
    elif choice == "4":
        print("\nExiting system. Have a productive day!")
        break
    else:
        print("\n[INVALID] Please enter a valid option (1, 2, 3, or 4).")
