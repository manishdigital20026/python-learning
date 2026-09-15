# Day 17: Unique Visited Flats Summary

# 1. पूरे दिन की विज़िटर लॉगबुक
visitor_log = [
    {"naam": "Amit", "flat": "101"},
    {"naam": "Pooja", "flat": "304"},
    {"naam": "Manish", "flat": "101"},
    {"naam": "Rahul", "flat": "202"},
    {"naam": "Suresh", "flat": "101"},
    {"naam": "Neha", "flat": "304"}
]

print("--- Daily Apartment Report ---")

# 2. सिर्फ अलग-अलग फ्लैट नंबर रखने के लिए खाली लिस्ट
visited_flats = []

# 3. लूप चलाकर बिना दोहराए फ्लैट जोड़ना
for entry in visitor_log:
    flat_no = entry["flat"]
    # अगर यह फ्लैट नंबर पहले से लिस्ट के 'अंदर नहीं' है
    if flat_no not in visited_flats:
        visited_flats.append(flat_no)

# 4. रिपोर्ट दिखाना
print("\n--- Jin Flats Me Aaj Visitors Aaye ---")
for f in visited_flats:
    print("Flat Number:", f)

print("--------------------------------------")
print("Kul Visited Flats (Unique):", len(visited_flats))
