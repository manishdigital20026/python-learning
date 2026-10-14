# Day 49: Disaster Recovery and Snapshot Restoration System

import os
import shutil
import csv

live_file = "settled_archive.csv"
backup_folder = "backups"

# Step 1: Ensure sample backup directory and snapshots exist
def setup_mock_environment():
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    sample_backup_1 = os.path.join(backup_folder, "backup_settled_20261013_100000.csv")
    sample_backup_2 = os.path.join(backup_folder, "backup_settled_20261014_041500.csv")

    if not os.path.exists(sample_backup_1):
        with open(sample_backup_1, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Ticket_ID", "Plate_No", "Exit_Time", "Amount_Paid", "Payment_Status"])
            w.writerow(["TKT-CAR-101", "KA-01-MJ-2026", "13-10-2026 10:00 AM", "120", "Completed"])

    if not os.path.exists(sample_backup_2):
        with open(sample_backup_2, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Ticket_ID", "Plate_No", "Exit_Time", "Amount_Paid", "Payment_Status"])
            w.writerow(["TKT-CAR-101", "KA-01-MJ-2026", "13-10-2026 10:00 AM", "120", "Completed"])
            w.writerow(["TKT-BIKE-205", "KA-04-E-1234", "14-10-2026 04:10 AM", "30", "Completed"])

# Step 2: Function to inspect backups and restore production database
def restore_database():
    print("=== DISASTER RECOVERY: DATABASE RESTORATION ===")

    if not os.path.exists(backup_folder):
        print(f"[ERROR] No backup directory '{backup_folder}' found.")
        return

    # List all available backup files
    available_backups = sorted([f for f in os.listdir(backup_folder) if f.endswith(".csv")])

    if not available_backups:
        print("[ERROR] No valid CSV snapshots found in backup repository.")
        return

    print("\nAvailable Snapshots:")
    for index, filename in enumerate(available_backups, start=1):
        full_path = os.path.join(backup_folder, filename)
        size_bytes = os.path.getsize(full_path)
        print(f" [{index}] {filename} ({size_bytes} bytes)")

    # Step 3: Accept operator selection with input validation
    selection = input("\nEnter snapshot number to restore (or '0' to cancel): ").strip()

    if selection == "0":
        print("[CANCELLED] Recovery aborted by user.")
        return

    if not selection.isdigit() or not (1 <= int(selection) <= len(available_backups)):
        print("[ERROR] Invalid selection number. Operation aborted.")
        return

    selected_file = available_backups[int(selection) - 1]
    source_path = os.path.join(backup_folder, selected_file)

    # Step 4: Overwrite live file with selected snapshot
    try:
        shutil.copy(source_path, live_file)
        print("\n[SUCCESS] Production database successfully restored!")
        print(f" -> Restored from: {selected_file}")
        print(f" -> Active file  : {live_file}")
    except Exception as error:
        print(f"[FATAL] Restoration failed: {error}")

# Run setup and execute restoration prompt
setup_mock_environment()
restore_database()

# Step 5: Verify restored production file content
print("\n--- Current Production Database Content ---")
if os.path.exists(live_file):
    with open(live_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
