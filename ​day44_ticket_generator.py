# Day 44: Unique Ticket ID Generation and Printable Entry Slip

import csv
import os
import random
from datetime import datetime

file_name = "issued_tickets.csv"

# Step 1: Initialize database with Ticket_ID header
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Ticket_ID", "Date_Time", "Category", "Plate_No", "Slot", "Rate"])

# Step 2: Function to generate unique ticket reference
def generate_ticket_id(category_prefix):
    # Format: TKT-<PREFIX>-<DATETIME>-<RANDOM3DIGITS>
    # Example: TKT-CAR-0910-482
    timestamp = datetime.now().strftime("%d%m")
    random_token = random.randint(100, 999)
    return f"TKT-{category_prefix}-{timestamp}-{random_token}"

# Step 3: Issue parking pass and display printable receipt
def issue_entry_pass():
    print("=== AUTOMATED PARKING TICKET DISPENSER ===")
    print("1. Two-Wheeler (Bike) - Rs. 20/hr")
    print("2. Four-Wheeler (Car)  - Rs. 50/hr")
    
    choice = input("Select Vehicle Type (1 or 2): ").strip()
    if choice == "1":
        cat_name = "BIKE"
        assigned_slot = "B-03"
        base_rate = 20
    elif choice == "2":
        cat_name = "CAR"
        assigned_slot = "C-07"
        base_rate = 50
    else:
        print("[ERROR] Invalid choice. Transaction cancelled.")
        return

    plate = input("Enter Vehicle Number (e.g. KA-05-MN-2026): ").strip().upper()
    now = datetime.now()
    time_str = now.strftime("%d-%m-%Y %I:%M %p")
    ticket_id = generate_ticket_id(cat_name)

    # Save entry to CSV
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([ticket_id, time_str, cat_name, plate, assigned_slot, base_rate])

    # Printable Customer Slip
    print("\n" + "=" * 42)
    print("         METRO PARKING MANAGEMENT         ")
    print("             CUSTOMER ENTRY PASS          ")
    print("=" * 42)
    print(f" Ticket Number : {ticket_id}")
    print(f" Check-In Time : {time_str}")
    print(f" Vehicle Plate : {plate}")
    print(f" Vehicle Type  : {cat_name}")
    print(f" Assigned Bay  : {assigned_slot}")
    print(f" Base Rate     : Rs. {base_rate} / hr")
    print("-" * 42)
    print(" Keep this slip safe for exit checkout!   ")
    print("=" * 42 + "\n")

# Run ticket issuance
issue_entry_pass()

# Display persistent CSV log
print("--- Saved Storage Snapshot ---")
with open(file_name, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
