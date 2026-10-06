# Day 41: Automated Parking Slot Assignment System

import csv
import os

file_name = "parking_slots.csv"
TOTAL_SLOTS = ["P-1", "P-2", "P-3", "P-4", "P-5"]

# Step 1: Ensure initial storage with a Slot column exists
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Slot", "Vehicle_No", "Driver_Name", "Status"])
        # P-1 is occupied, P-2 was vacated (Paid)
        writer.writerow(["P-1", "KA-01-AB-1111", "Amit", "Pending"])
        writer.writerow(["P-2", "DL-02-XY-2222", "Manish", "Paid"])

# Step 2: Find all currently occupied slots
def get_occupied_slots():
    occupied = set()
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                if row and len(row) >= 4:
                    slot = row[0].strip()
                    status = row[3].strip()
                    if status == "Pending":
                        occupied.add(slot)
    return occupied

# Step 3: Find the first available parking slot
def get_next_available_slot():
    occupied = get_occupied_slots()
    for slot in TOTAL_SLOTS:
        if slot not in occupied:
            return slot
    return None  # All slots are occupied

# Step 4: Register incoming vehicle to the assigned slot
def assign_vehicle_slot():
    print("--- Smart Slot Assignment Gate ---")
    available_slot = get_next_available_slot()

    if not available_slot:
        print("[ALERT - HOUSE FULL] All parking slots (P-1 to P-5) are currently occupied!")
        return

    plate = input("Enter Vehicle Number (e.g. MH-12-PQ-9999): ").strip().upper()
    driver = input("Enter Driver Name: ").strip()

    # Save to CSV with the assigned slot
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([available_slot, plate, driver, "Pending"])

    print(f"\n[ASSIGNED] Vehicle {plate} successfully parked in Slot: {available_slot}")

# Execute test run
assign_vehicle_slot()

# Display current database entries
print("\n--- Current Parking Slot Status ---")
with open(file_name, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
