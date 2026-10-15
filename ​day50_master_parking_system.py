# Day 50 Milestone: Master Smart Parking Management System (v1.0)

import csv
import os
import shutil
import math
from datetime import datetime

# Database files and paths
ACTIVE_FILE = "active_parking.csv"
ARCHIVE_FILE = "settled_archive.csv"
BACKUP_DIR = "backups"

# Configuration
SLOTS = {
    "BIKE": ["B-1", "B-2", "B-3"],
    "CAR": ["C-1", "C-2", "C-3"]
}

RATES = {
    "BIKE": 20,  # Rs. 20/hr
    "CAR": 50    # Rs. 50/hr
}

# --- 1. SYSTEM INITIALIZATION ---
def init_system():
    if not os.path.exists(ACTIVE_FILE):
        with open(ACTIVE_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Ticket_ID", "Category", "Plate_No", "Slot", "Entry_Time"])

    if not os.path.exists(ARCHIVE_FILE):
        with open(ARCHIVE_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Ticket_ID", "Plate_No", "Category", "Entry_Time", "Exit_Time", "Fee_Paid"])

    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

# --- 2. VISUAL OCCUPANCY GRID ---
def view_parking_map():
    occupied_slots = {}
    with open(ACTIVE_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row:
                occupied_slots[row[3].strip()] = row[2].strip()

    print("\n" + "=" * 48)
    print("         LIVE PARKING OCCUPANCY MAP             ")
    print("=" * 48)
    for cat, slot_list in SLOTS.items():
        print(f"\n[{cat} SECTION]")
        for s in slot_list:
            if s in occupied_slots:
                print(f"  {s} : [ OCCUPIED - {occupied_slots[s]} ]")
            else:
                print(f"  {s} : [ FREE / EMPTY ]")
    print("=" * 48)

# --- 3. VEHICLE ENTRY & TICKET ISSUANCE ---
def check_in():
    print("\n--- VEHICLE CHECK-IN DESK ---")
    print("1. Two-Wheeler (Bike - Rs. 20/hr)")
    print("2. Four-Wheeler (Car  - Rs. 50/hr)")
    choice = input("Select Category (1 or 2): ").strip()

    cat = "BIKE" if choice == "1" else "CAR" if choice == "2" else None
    if not cat:
        print("[ERROR] Invalid vehicle category.")
        return

    # Check for empty slot in section
    occupied = set()
    with open(ACTIVE_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row:
                occupied.add(row[3].strip())

    free_slot = next((s for s in SLOTS[cat] if s not in occupied), None)
    if not free_slot:
        print(f"[ALERT] Sorry, all {cat} slots are fully occupied!")
        return

    # Plate Input Validation
    plate = input("Enter Vehicle Plate (e.g. KA-01-AB-1234): ").strip().upper()
    cleaned = plate.replace("-", "").replace(" ", "")
    if not (cleaned.isalnum() and 8 <= len(cleaned) <= 10):
        print("[ERROR] Invalid vehicle plate format.")
        return

    # Generate Ticket
    now = datetime.now()
    time_str = now.strftime("%d-%m-%Y %I:%M %p")
    tkt_id = f"TKT-{cat}-{now.strftime('%d%H%M')}"

    with open(ACTIVE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([tkt_id, cat, plate, free_slot, time_str])

    print("\n" + "*" * 40)
    print(f" TICKET ISSUED: {tkt_id}")
    print(f" Vehicle: {plate} | Bay: {free_slot}")
    print(f" Entry  : {time_str}")
    print("*" * 40)

# --- 4. CHECKOUT & ARCHIVE MIGRATION ---
def check_out():
    print("\n--- VEHICLE EXIT & BILLING COUNTER ---")
    search_tkt = input("Scan or Enter Ticket ID: ").strip().upper()

    active_rows = []
    target_record = None

    with open(ACTIVE_FILE, "r") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        active_rows.append(header)
        for row in reader:
            if row and row[0].strip().upper() == search_tkt:
                target_record = row
            else:
                active_rows.append(row)

    if not target_record:
        print(f"[ERROR] Ticket ID '{search_tkt}' not found in active parking.")
        return

    t_id, cat, plate, slot, entry_str = target_record

    # Time and Billing Calculation
    entry_time = datetime.strptime(entry_str, "%d-%m-%Y %I:%M %p")
    exit_time = datetime.now()
    exit_str = exit_time.strftime("%d-%m-%Y %I:%M %p")

    minutes = int((exit_time - entry_time).total_seconds() / 60)
    billable_hours = max(1, math.ceil(minutes / 60))
    total_fee = billable_hours * RATES[cat]

    # Print Receipt
    print("\n" + "=" * 40)
    print("         EXIT PAYMENT RECEIPT           ")
    print("=" * 40)
    print(f" Ticket : {t_id}")
    print(f" Plate  : {plate} ({cat}) | Bay: {slot}")
    print(f" Hours  : {billable_hours} hr(s) | Total: Rs. {total_fee}")
    print("=" * 40)

    # 1. Update Active File
    with open(ACTIVE_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(active_rows)

    # 2. Append to Historical Archive
    with open(ARCHIVE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([t_id, plate, cat, entry_str, exit_str, total_fee])

    print("[SUCCESS] Payment settled. Bay cleared and transaction archived.")

# --- 5. AUDIT SUMMARY ---
def view_audit():
    total_rev = 0
    tx_count = 0
    with open(ARCHIVE_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row and len(row) >= 6:
                total_rev += int(row[5].strip())
                tx_count += 1

    print("\n" + "=" * 40)
    print("      SETTLED REVENUE AUDIT             ")
    print("=" * 40)
    print(f" Total Settled Transactions : {tx_count}")
    print(f" Total Revenue Collected    : Rs. {total_rev}")
    print("=" * 40)

# --- 6. DATABASE BACKUP ---
def backup_database():
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(BACKUP_DIR, f"backup_archive_{ts}.csv")
    try:
        shutil.copy(ARCHIVE_FILE, dest)
        print(f"\n[BACKUP OK] Database saved to: {dest}")
    except Exception as e:
        print(f"[ERROR] Backup failed: {e}")

# --- MAIN MENU LOOP ---
def main():
    init_system()
    while True:
        print("\n==========================================")
        print("    SMART PARKING ERP - MASTER CONTROL    ")
        print("==========================================")
        print("1. View Live Parking Map")
        print("2. Check-In Vehicle (Issue Ticket)")
        print("3. Check-Out Vehicle (Payment & Clear)")
        print("4. View Financial Audit Summary")
        print("5. Create Instant Database Backup")
        print("6. Exit")

        choice = input("\nEnter option (1-6): ").strip()
        if choice == "1":
            view_parking_map()
        elif choice == "2":
            check_in()
        elif choice == "3":
            check_out()
        elif choice == "4":
            view_audit()
        elif choice == "5":
            backup_database()
        elif choice == "6":
            print("\nShutting down system. Excellent job reaching Day 50!")
            break
        else:
            print("[ERROR] Invalid choice. Select 1 to 6.")

if __name__ == "__main__":
    main()
