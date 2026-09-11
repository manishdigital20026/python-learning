# Day 14: Digital Visitor Logbook System

# 1. मुख्य विज़िटर रजिस्टर (List of Dictionaries)
visitor_log = [
    {"naam": "Amit", "flat": "101"},
    {"naam": "Pooja", "flat": "304"}
]

print("--- Apartment Gate Logbook ---")

# 2. नए विज़िटर की जानकारी लेना
new_name = input("Naye visitor ka naam darj karein: ")
new_flat = input("Flat number likhein: ")

# 3. नई पर्ची (डिक्शनरी) तैयार करना
new_entry = {
    "naam": new_name,
    "flat": new_flat
}

# 4. मुख्य लिस्ट में यह पर्ची जोड़ना (append)
visitor_log.append(new_entry)
print("\n[SUCCESS] Entry safalta-poorvak darj ho gayi!")

# 5. लूप चलाकर पूरा रजिस्टर साफ़-साफ़ देखना
print("\n================================")
print("     AAJ KI VISITOR LOGBOOK     ")
print("================================")

for visitor in visitor_log:
    print("Visitor:", visitor["naam"], "| Flat:", visitor["flat"])

print("================================")
print("Total Visitors:", len(visitor_log))
