# Day 21: Save Visitor Pass to Text File (File Handling)

print("--- Digital Visitor Pass Generator ---")

# 1. यूजर से विज़िटर की जानकारी लेना
visitor_name = input("Visitor ka naam darj karein: ")
flat_no = input("Flat number likhein: ")
purpose = input("Aane ka kaaran (Meeting/Delivery/Personal): ")

# 2. फ़ाइल खोलना और उसमें लिखना (Write Mode "w")
# agar file pehle se nahi hai, to Python ise apne aap bana dega
with open("visitor_pass.txt", "w") as file:
    file.write("==============================\n")
    file.write("     OFFICIAL VISITOR PASS    \n")
    file.write("==============================\n")
    file.write("Name    : " + visitor_name + "\n")
    file.write("Flat No : " + flat_no + "\n")
    file.write("Purpose : " + purpose + "\n")
    file.write("Status  : Approved\n")
    file.write("==============================\n")

print("\n[SUCCESS] Visitor Pass safalta-poorvak 'visitor_pass.txt' me save ho gaya!")
print("Aap apne phone ke file manager me ise dekh sakte hain.")
