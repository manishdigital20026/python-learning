# Day 15: Search Visitor by Flat Number

# 1. पहले से मौजूद विज़िटर लॉगबुक
visitor_log = [
    {"naam": "Amit", "flat": "101"},
    {"naam": "Pooja", "flat": "304"},
    {"naam": "Manish", "flat": "202"},
    {"naam": "Rohan", "flat": "101"}
]

print("--- Apartment Security Search Desk ---")

# 2. यूज़र से पूछना कि किस फ्लैट की जानकारी चाहिए
search_flat = input("Kaun se Flat number ke visitor ko khojna hai? : ")

found = False

print("\n--- Search Results ---")

# 3. एक-एक करके हर विज़िटर की जांच करना
for visitor in visitor_log:
    if visitor["flat"] == search_flat:
        print("Mila! Visitor Naam:", visitor["naam"])
        found = True

# 4. अगर उस फ्लैट के लिए कोई विज़िटर नहीं मिला
if not found:
    print("Is Flat ke liye koi visitor andar darj nahi hai.")
