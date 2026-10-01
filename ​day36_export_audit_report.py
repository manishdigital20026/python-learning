# Day 36: Export Daily Audit Summary to a Text File

import csv
import os
from datetime import datetime

csv_file = "parking_records.csv"
report_file = "audit_summary.txt"

# Step 1: Ensure initial sample data exists
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Vehicle_No", "Driver_Name", "Bill_Amount", "Status"])
        writer.writerow(["KA-01-AB-1111", "Amit", "60", "Paid"])
        writer.writerow(["DL-02-XY-2222", "Manish", "100", "Paid"])
        writer.writerow(["MH-12-PQ-3333", "Pooja", "40", "Paid"])
        writer.writerow(["HR-26-BR-4444", "Rahul", "80", "Pending"])

# Step 2: Read CSV data and calculate metrics
total_collected = 0
total_pending = 0
paid_count = 0
pending_count = 0

with open(csv_file, "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        if row:
            amount = int(row[2])
            status = row[3].strip()

            if status == "Paid":
                total_collected += amount
                paid_count += 1
            elif status == "Pending":
                total_pending += amount
                pending_count += 1

# Step 3: Format the audit report with a live timestamp
current_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

report_content = f"""========================================
     DAILY PARKING AUDIT REPORT
========================================
Generated On        : {current_time}
Total Settled Cars  : {paid_count}
Total Pending Cars  : {pending_count}
----------------------------------------
Total Cash Received : Rs. {total_collected}
Outstanding Dues    : Rs. {total_pending}
Projected Revenue   : Rs. {total_collected + total_pending}
========================================
Status              : Audit Complete
"""

# Step 4: Write the report content to the text file
with open(report_file, "w") as file:
    file.write(report_content)

print("[SUCCESS] Audit report successfully generated and saved to 'audit_summary.txt'!\n")

# Step 5: Read and display the generated report in terminal
with open(report_file, "r") as file:
    print(file.read())
