# Day 24: Search Visitor Record in Text File

# 1. अभ्यास के लिए रजिस्टर फ़ाइल में कुछ रिकॉर्ड तैयार करना
with open("daily_register.txt", "w") as file:
    file.write("Visitor: Amit | Flat: 101 | Status: In\n")
    file.write("Visitor: Pooja | Flat: 304 | Status: In\n")
    file.write("Visitor: Manish | Flat: 202 | Status: In\n")
    file.write("Visitor: Rohan | Flat: 101 | Status: In\n")

print("--- Register Record Search Desk ---")

# 2. यूज़र से पूछना कि किसका नाम खोजना है
target_name = input("Kisko search karna hai? Naam likhein: ")

found = False

# 3. फ़ाइल खोलकर लाइन-बाय-लाइन खोजना
with open("daily_register.txt", "r") as file:
    for line in file:
        # Check karna ki kya naam is line ke andar maujood hai
        if target_name in line:
            print("\n[RECORD FOUND] Record mil gaya!")
            print("Puri Detail:", line.strip())
            found = True
            break  # milte hi loop rok do

# 4. अगर नाम फ़ाइल में नहीं मिला
if not found:
    print("\n[NOT FOUND] Maaf kijiye,", target_name, "ka koi record nahi mila.")
