# Day 23: Read File Line by Line & Count Visitors

# 1. पहले अभ्यास के लिए फ़ाइल में 3 रिकॉर्ड लिख देते हैं
with open("daily_register.txt", "w") as file:
    file.write("Visitor: Amit | Flat: 101 | Status: In\n")
    file.write("Visitor: Pooja | Flat: 304 | Status: In\n")
    file.write("Visitor: Manish | Flat: 202 | Status: In\n")

print("--- Daily Register Audit Desk ---")

# 2. फ़ाइल को Read Mode ("r") में खोलना
with open("daily_register.txt", "r") as file:
    # sari lines ko ek list ke roop me padhna
    all_lines = file.readlines()

# 3. लूप चलाकर हर लाइन को नंबर के साथ दिखाना
print("\n--- Register Entries (Line by Line) ---")
serial_no = 1
for line in all_lines:
    # line.strip() se extra enter ya space hat jata hai
    print(str(serial_no) + ".", line.strip())
    serial_no = serial_no + 1

# 4. कुल एंट्रीज (लाइनों) की गिनती बताना
total_visitors = len(all_lines)

print("---------------------------------------")
print("Total Visitors Registered:", total_visitors)
