# Day 9: Interactive Gate Pass System

# 1. पहले से स्वीकृत लोगों की सूची
allowed_list = ["Amit", "Rohan", "Pooja", "Manish"]

print("--- Welcome to Digital Security Gate ---")

# 2. यूजर से नाम पूछना (input)
guest_name = input("Apna naam type kijiye: ")

# 3. नाम की जांच (in और if-else)
if guest_name in allowed_list:
    print("\n[SUCCESS] Namaste", guest_name, "bhai! Aap andar ja sakte hain.")
else:
    print("\n[ALERT] Maaf kijiye", guest_name, "ji, aapka naam list me nahi hai.")
    print("Kripya security desk par sampark karein.")
