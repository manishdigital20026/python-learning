# Day 13: Visitor ID Card System (Dictionary)

print("--- Digital Visitor Pass Entry ---")

# 1. यूजर से जानकारी लेना
v_name = input("Visitor ka naam likhein: ")
v_flat = input("Kaun se Flat number me jana hai: ")
v_phone = input("Mobile number darj karein: ")

# 2. डिक्शनरी {} में पूरा रिकॉर्ड एक साथ बांधना
visitor_pass = {
    "naam": v_name,
    "flat": v_flat,
    "phone": v_phone
}

# 3. एंट्री पास प्रिंट करना
print("\n==============================")
print("     VISITOR ENTRY PASS       ")
print("==============================")
print("Naam   :", visitor_pass["naam"])
print("Flat No:", visitor_pass["flat"])
print("Phone  :", visitor_pass["phone"])
print("Status : Approved (Andar jane ki anumati hai)")
print("==============================")
