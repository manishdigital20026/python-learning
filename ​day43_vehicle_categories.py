# Day 43: Vehicle Categorization and Dynamic Rate Mapping

import csv
import os

file_name = "categorized_parking.csv"

# Dedicated slots for each category
SLOT_CONFIG = {
    "BIKE": ["B-1", "B-2", "B-3"],
    "CAR": ["C-1", "C-2", "C-3"]
}

# Standard rate card per category
RATE_CARD = {
    "BIKE": 20,
    "CAR": 50
}

# Step 1: Ensure initial CSV headers exist
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Slot", "Category", "Vehicle_No", "Fee", "Status"])
        writer.writerow(["B-1", "BIKE", "KA-04-E-1234", "20", "Pending"])
        writer.writerow(["C-1", "CAR", "KA-01-MJ-5678", "50", "Pending"])

# Step 2: Find occupied slots for a specific category
def get_occupied_slots(category):
    occupied = set()
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip table header
            for row in reader:
                if row and len(row) >= 5:
                    slot = row[0].strip()
                    row_cat = row[1].strip()
                    status = row[4].strip()
                    if row_cat == category and status == "Pending":
                        occupied.add(slot)
    return occupied

# Step 3: Check in incoming vehicle
def check_in_vehicle():
    print("--- Categorized Vehicle Gate Desk ---")
    print("Select Category:")
    print("1. Bike / Two-Wheeler (Rs. 20)")
    print("2. Car / Four-Wheeler (Rs. 50)")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        category = "BIKE"
    elif choice == "2":
        category = "CAR"
    else:
        print("[ERROR] Invalid choice selected. Entry cancelled.")
        return

    # Check for available slot in chosen category
    occupied = get_occupied_slots(category)
    available_slot = None
    for slot in SLOT_CONFIG[category]:
        if slot not in occupied:
            available_slot = slot
            break

    if not available_slot:
        print(f"[ALERT - FULL] No empty slots available for {category}s!")
        return

    plate = input("Enter Vehicle Number (e.g. KA-05-AB-9999): ").strip().upper()
    fee = RATE_CARD[category]

    # Save to CSV
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([available_slot, category, plate, fee, "Pending"])

    print(f"\n[CONFIRMED] {category} assigned to Slot: {available_slot} | Base Fee: Rs. {fee}")

# Run entry routine
check_in_vehicle()

# Display active database entries
print("\n--- Current Categorized Parking Database ---")
with open(file_name, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
