# Day 29: Automated Parking Billing by Duration

from datetime import datetime
import time

print("--- Automated Parking Toll System ---")

# Step 1: Vehicle Entry
vehicle_number = input("Enter vehicle number (e.g., DL-01-AB-1234): ")
entry_time = datetime.now()
print("Entry Time:", entry_time.strftime("%I:%M:%S %p"))

# Step 2: Simulating parking stay (Wait 4 seconds)
print("\nVehicle is parked inside... (Please wait)")
time.sleep(4)

# Step 3: Vehicle Exit
exit_time = datetime.now()
print("Exit Time :", exit_time.strftime("%I:%M:%S %p"))

# Step 4: Calculate duration in seconds
duration = exit_time - entry_time
seconds_spent = int(duration.total_seconds())

# Step 5: Rate Calculation (Rs. 10 per second for simulation)
rate_per_unit = 10
total_bill = seconds_spent * rate_per_unit

# Step 6: Print Final Receipt
print("\n==============================")
print("     PARKING CASH RECEIPT     ")
print("==============================")
print("Vehicle No :", vehicle_number)
print("Total Time :", seconds_spent, "seconds")
print("Rate       : Rs.", rate_per_unit, "/ second")
print("Total Due  : Rs.", total_bill)
print("Payment    : Pending")
print("==============================")
