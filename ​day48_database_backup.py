# Day 48: Automated Backup Creation for Critical CSV Databases

import os
import shutil
import csv
from datetime import datetime

source_file = "settled_archive.csv"
backup_folder = "backups"

# Step 1: Ensure initial sample archive exists
if not os.path.exists(source_file):
    with open(source_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Ticket_ID", "Plate_No", "Exit_Time", "Amount_Paid", "Payment_Status"])
        writer.writerow(["TKT-CAR-101", "KA-01-MJ-2026", "10-10-2026 09:30 AM", "150", "Completed"])
        writer.writerow(["TKT-BIKE-102", "KA-04-E-1234", "11-10-2026 11:15 AM", "40", "Completed"])

# Step 2: Function to create a timestamped backup
def create_database_backup():
    print("--- Automated System Backup Utility ---")

    # Verify source database exists
    if not os.path.exists(source_file):
        print(f"[ERROR] Source database '{source_file}' not found. Cannot perform backup.")
        return

    # Create backup directory if it does not already exist
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
        print(f"[SETUP] Created new backup directory: '{backup_folder}/'")

    # Generate timestamped filename (YYYYMMDD_HHMMSS)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"backup_settled_{timestamp}.csv"
    destination_path = os.path.join(backup_folder, backup_filename)

    # Perform file duplication
    try:
        shutil.copy(source_file, destination_path)
        print("\n[SUCCESS] Backup completed successfully!")
        print(f" -> Source      : {source_file}")
        print(f" -> Backup File : {destination_path}")
    except Exception as e:
        print(f"[ERROR] Failed to create backup: {e}")

# Step 3: Run backup operation
create_database_backup()

# Step 4: Verify and list all backup files created
print("\n--- Current Backups in Storage ---")
if os.path.exists(backup_folder):
    files = os.listdir(backup_folder)
    if files:
        for idx, file_name in enumerate(files, 1):
            file_path = os.path.join(backup_folder, file_name)
            file_size = os.path.getsize(file_path)
            print(f" {idx}. {file_name} ({file_size} bytes)")
    else:
        print("No backup files found.")
