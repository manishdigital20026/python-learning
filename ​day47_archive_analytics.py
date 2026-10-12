# Day 47: Filter and Analyze Revenue from Historical Archive

import csv
import os

archive_file = "settled_archive.csv"

# Step 1: Ensure sample historical archive exists for testing
if not os.path.exists(archive_file):
    with open(archive_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Ticket_ID", "Plate_No", "Exit_Time", "Amount_Paid", "Payment_Status"])
        # Format of Exit_Time: DD-MM-YYYY hh:mm AM/PM
        writer.writerow(["TKT-CAR-101", "KA-01-MJ-2026", "10-10-2026 09:30 AM", "150", "Completed"])
        writer.writerow(["TKT-BIKE-102", "KA-04-E-1234", "11-10-2026 11:15 AM", "40", "Completed"])
        writer.writerow(["TKT-CAR-103", "DL-02-XY-2222", "12-10-2026 04:20 PM", "100", "Completed"])
        writer.writerow(["TKT-CAR-099", "MH-12-PQ-3333", "28-09-2026 02:00 PM", "80", "Completed"])

# Step 2: Function to calculate revenue filtered by Month-Year or specific Date
def generate_revenue_report(filter_query):
    total_revenue = 0
    match_count = 0
    matched_records = []

    with open(archive_file, "r") as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip header row

        for row in reader:
            if row and len(row) >= 5:
                t_id = row[0].strip()
                plate = row[1].strip()
                exit_time = row[2].strip()
                amount = int(row[3].strip())
                status = row[4].strip()

                # Check if search pattern (e.g. "10-2026" or "12-10-2026") is inside the timestamp
                if filter_query in exit_time and status == "Completed":
                    total_revenue += amount
                    match_count += 1
                    matched_records.append((t_id, plate, exit_time, amount))

    # Step 3: Print formatted audit breakdown
    print("\n" + "=" * 46)
    print(f"   FINANCIAL SETTLEMENT AUDIT: {filter_query}")
    print("=" * 46)
    
    if match_count == 0:
        print("[INFO] No transactions found matching this period.")
    else:
        for rec in matched_records:
            print(f" {rec[0]} | {rec[1]} | {rec[2]} | Rs. {rec[3]}")
        print("-" * 46)
        print(f" Total Settled Vehicles : {match_count}")
        print(f" Total Revenue Collected: Rs. {total_revenue}")
    
    print("=" * 46 + "\n")

# Step 4: Interactive prompt for accounting
print("--- Historical Parking Accounting Console ---")
print("Enter period filter:")
print(" - For a specific month: MM-YYYY (e.g., 10-2026)")
print(" - For a specific day  : DD-MM-YYYY (e.g., 12-10-2026)")

query = input("\nEnter query to analyze: ").strip()
generate_revenue_report(query)
