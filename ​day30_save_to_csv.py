# Day 30: Save Parking Records in CSV Format (Excel Compatible)

import csv

file_name = "parking_records.csv"

print("--- Automated Parking CSV Logger ---")

# 1. यूजर से एंट्री लेना
vehicle_no = input("Vehicle Number likhein (e.g. DL-01-AB-1234): ")
owner_name = input("Driver/Owner ka naam: ")
bill_amount = input("Total Bill Amount (Rs.): ")

# 2. नया रिकॉर्ड लिस्ट के रूप में तैयार करना
new_record = [vehicle_no, owner_name, bill_amount, "Paid"]

# 3. CSV फ़ाइल में लिखना (Append Mode "a")
# newline='' lagane se beech me extra khali line nahi banti
with open(file_name, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_record)

print("\n[SUCCESS] Record 'parking_records.csv' me jud gaya!")

# 4. CSV फ़ाइल को पढ़कर टेबल की तरह देखना
print("\n--- Current CSV Register Content ---")
with open(file_name, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print("Vehicle:", row[0], "| Owner:", row[1], "| Bill: Rs.", row[2], "| Status:", row[3])
