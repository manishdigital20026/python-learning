# Day 27: Visitor Entry with Real Date & Time Stamp

# 1. पायथन की इनबिल्ट घड़ी को बुलाना
from datetime import datetime

print("--- Smart Gate Entry with Live Timestamp ---")

# 2. चालू तारीख और समय निकालना
ab_ka_samay = datetime.now()

# समय को सुंदर रूप में बदलना (तारीख-महीना-साल और घंटा:मिनट)
# %d = Din, %m = Mahina, %Y = Saal, %I = Ghanta (12-hour), %M = Minute, %p = AM/PM
formatted_time = ab_ka_samay.strftime("%d-%m-%Y %I:%M %p")

# 3. विज़िटर की जानकारी इनपुट लेना
visitor_name = input("Visitor ka naam darj karein: ")
flat_no = input("Flat number likhein: ")

# 4. पूरा रिकॉर्ड तैयार करना (तारीख और समय के साथ)
entry_record = "Time: " + formatted_time + " | Name: " + visitor_name + " | Flat: " + flat_no + "\n"

# 5. फ़ाइल में समय के साथ सुरक्षित करना (Append Mode)
with open("timestamp_register.txt", "a") as file:
    file.write(entry_record)

print("\n[SUCCESS] Entry safalta-poorvak darj ho gayi!")

# 6. फ़ाइल का ताज़ा रिकॉर्ड स्क्रीन पर देखना
print("\n--- Register Entries (With Real Timestamp) ---")
with open("timestamp_register.txt", "r") as file:
    print(file.read())
