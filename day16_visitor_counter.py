# Day 16: Visitor Counter by Flat Number

# 1. विज़िटर लॉगबुक
visitor_log = [
    {"naam": "Amit", "flat": "101"},
    {"naam": "Pooja", "flat": "304"},
    {"naam": "Manish", "flat": "101"},
    {"naam": "Rahul", "flat": "202"},
    {"naam": "Suresh", "flat": "101"}
]

print("--- Apartment Visitor Counter Desk ---")

# 2. यूज़र से फ्लैट नंबर पूछना
target_flat = input("Kaun se Flat number ki ginti karni hai? : ")

# 3. गिनती शुरू करने वाला डिब्बा (Counter)
count = 0

print("\n--- Visitors ki List ---")

# 4. लूप चलाकर चेक करना और गिनती बढ़ाना
for visitor in visitor_log:
    if visitor["flat"] == target_flat:
        print("-", visitor["naam"])
        count = count + 1  # har baar ek visitor milne par count 1 badhega

# 5. कुल नतीजा दिखाना
print("------------------------")
if count > 0:
    print("Flat", target_flat, "me kul", count, "visitors aaye hain.")
else:
    print("Flat", target_flat, "ke liye koi visitor nahi mila.")
