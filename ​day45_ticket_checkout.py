# Day 45: Ticket ID Lookup and Automated Exit Billing

import csv
import os
import math
from datetime import datetime, timedelta

file_name = "issued_tickets.csv"

# Step 1: Ensure sample tickets exist for testing
if not os.path.exists(file_name):
    # Simulate a ticket issued 2 hours and 15 minutes ago
    simulated_entry = (datetime.now() - timedelta(hours=2, minutes=15)).strftime("%d-%m-%Y %I:%M %p")
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Ticket_ID", "Date_Time", "Category", "Plate_No", "Slot", "Rate"])
        writer.writerow(["TKT-CAR-1010-501", simulated_entry, "CAR", "KA-01-MJ-2026", "C-07", "50"])
        writer.writerow(["TKT-BIKE-1010-742", simulated_entry, "BIKE", "KA-04-E-1234", "B-03", "20"])

# Step 2: Exit processing by scanning/entering Ticket ID
def process_ticket_checkout():
    print("=== AUTOMATED EXIT BARRIER SCANNER ===")
    search_id = input("Scan or Enter Ticket ID (e.g. TKT-CAR-1010-501): ").strip().upper()

    ticket_found = None

    # Step 3: Lookup Ticket ID in storage
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header
        for row in reader:
            if row and row[0].strip().upper() == search_id:
                ticket_found = row
                break

    if not ticket_found:
        print(f"\n[ERROR] Ticket ID '{search_id}' not found in records. Check with security.")
        return

    # Extract stored fields
    t_id, entry_str, category, plate, slot, rate_str = ticket_found
    hourly_rate = int(rate_str)

    # Step 4: Parse stored string back into a datetime object
    # Format: %d-%m-%Y %I:%M %p (matches Day 44 output)
    entry_datetime = datetime.strptime(entry_str, "%d-%m-%Y %I:%M %p")
    exit_datetime = datetime.now()

    # Calculate duration
    duration = exit_datetime - entry_datetime
    total_minutes = int(duration.total_seconds() / 60)
    
    # Billable hours (ceil rounds up: 2 hours 15 mins -> 3 billable hours)
    billable_hours = math.ceil(total_minutes / 60)
    if billable_hours < 1:
        billable_hours = 1  # Minimum 1 hour charge

    total_amount = billable_hours * hourly_rate

    # Step 5: Render final exit receipt
    print("\n" + "=" * 42)
    print("        METRO PARKING EXIT RECEIPT        ")
    print("=" * 42)
    print(f" Ticket ID     : {t_id}")
    print(f" Vehicle Plate : {plate} ({category})")
    print(f" Bay Cleared   : {slot}")
    print(f" Entry Time    : {entry_str}")
    print(f" Exit Time     : {exit_datetime.strftime('%d-%m-%Y %I:%M %p')}")
    print("-" * 42)
    print(f" Total Duration: {total_minutes} Minutes")
    print(f" Billable Units: {billable_hours} Hour(s) @ Rs. {hourly_rate}/hr")
    print(f" Total Payable : Rs. {total_amount}")
    print("=" * 42)
    print(" Gate barrier opening... Drive safely!")
    print("=" * 42 + "\n")

# Run test checkout
process_ticket_checkout()
