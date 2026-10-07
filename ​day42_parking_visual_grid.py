# Day 42: Visual Parking Lot Map and Status Dashboard

import csv
import os

file_name = "parking_slots.csv"
ALL_SLOTS = ["P-1", "P-2", "P-3", "P-4", "P-5", "P-6"]

# Step 1: Ensure initial sample records exist
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Slot", "Vehicle_No", "Driver_Name", "Status"])
        writer.writerow(["P-1", "KA-01-AB-1111", "Amit", "Pending"])
        writer.writerow(["P-2", "DL-02-XY-2222", "Manish", "Paid"])
        writer.writerow(["P-3", "MH-12-PQ-3333", "Pooja", "Pending"])
        writer.writerow(["P-5", "KA-04-MB-3456", "Ramesh", "Pending"])

# Step 2: Build slot occupancy dictionary from CSV
def get_slot_status():
    # Initialize all slots as Free
    slot_map = {slot: "EMPTY" for slot in ALL_SLOTS}

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip table header safely
            for row in reader:
                if row and len(row) >= 4:
                    slot = row[0].strip()
                    plate = row[1].strip()
                    status = row[3].strip()
                    
                    # If vehicle is currently inside, assign plate number to slot
                    if status == "Pending" and slot in slot_map:
                        slot_map[slot] = plate
                    # If Paid, ensure slot remains marked empty
                    elif status == "Paid" and slot_map.get(slot) == plate:
                        slot_map[slot] = "EMPTY"
    return slot_map

# Step 3: Render visual layout in terminal
def display_parking_lot():
    slots = get_slot_status()
    total_bays = len(ALL_SLOTS)
    occupied_count = sum(1 for status in slots.values() if status != "EMPTY")
    available_count = total_bays - occupied_count

    print("==================================================")
    print("         FACILITY PARKING OCCUPANCY MAP           ")
    print("==================================================")
    print(f"Total Slots: {total_bays} | Occupied: {occupied_count} | Free: {available_count}\n")

    # Render each bay card
    for slot in ALL_SLOTS:
        current_status = slots[slot]
        if current_status == "EMPTY":
            print(f"  [{slot}] --> [  FREE / AVAILABLE  ]")
        else:
            print(f"  [{slot}] --> [OCCUPIED: {current_status}]")

    print("==================================================")

# Execute dashboard render
display_parking_lot()
