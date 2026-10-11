# Day 46: Archive Migration System (Active to Historical Storage)

import csv
import os
from datetime import datetime

active_file = "active_parking.csv"
archive_file = "settled_archive.csv"

# Step 1: Ensure initial sample records exist
def initialize_files():
    if not os.path.exists(active_file):
        with open(active_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Ticket_ID", "Category", "Plate_No", "Slot"])
            writer.writerow(["TKT-CAR-101", "CAR", "KA-01-MJ-2026", "C-01"])
            writer.writerow(["TKT-BIKE-102", "BIKE", "KA-04-E-1234", "B-02"])

    if not os.path.exists(archive_file):
        with open(archive_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Ticket_ID", "Plate_No", "Exit_Time", "Amount_Paid", "Payment_Status"])

# Step 2: Migrate settled vehicle from active register to archive
def checkout_and_archive(ticket_id, amount_paid):
    remaining_active = []
    migrated_record = None

    # Read active file
    with open(active_file, "r") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        remaining_active.append(header)

        for row in reader:
            if row:
                if row[0].strip().upper() == ticket_id.strip().upper():
                    migrated_record = row
                else:
                    remaining_active.append(row)

    if not migrated_record:
        print(f"[ERROR] Ticket '{ticket_id}' not found in active parking!")
        return

    # 1. Write remaining vehicles back to active register
    with open(active_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(remaining_active)

    # 2. Append completed transaction to archive log
    exit_stamp = datetime.now().strftime("%d-%m-%Y %I:%M %p")
    t_id, _, plate, _ = migrated_record
    archive_row = [t_id, plate, exit_stamp, amount_paid, "Completed"]

    with open(archive_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(archive_row)

    print(f"\n[SUCCESS] Ticket {t_id} checked out!")
    print(f" -> Cleared from {active_file}")
    print(f" -> Permanently archived to {archive_file}")

# Run test simulation
initialize_files()

print("--- Automated Checkout & Archiving Gate ---")
ticket_to_close = input("Enter Ticket ID to checkout (e.g., TKT-CAR-101): ").strip().upper()
fee = input("Enter Collected Amount (Rs.): ").strip()

checkout_and_archive(ticket_to_close, fee)

# Step 3: Print current state of both files
print("\n--- Remaining in active_parking.csv ---")
with open(active_file, "r") as f:
    for r in csv.reader(f):
        print(r)

print("\n--- Saved in settled_archive.csv ---")
with open(archive_file, "r") as f:
    for r in csv.reader(f):
        print(r)
