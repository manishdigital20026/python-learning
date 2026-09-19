# Day 22: Continuous Visitor Register (Append Mode "a")

print("--- Daily Visitor Attendance Register ---")

# 1. यूजर से विज़िटर की जानकारी लेना
visitor_name = input("Visitor ka naam darj karein: ")
flat_no = input("Flat number likhein: ")
phone_no = input("Phone number likhein: ")

# 2. फ़ाइल को Append Mode ("a") में खोलना
# "a" ka matlab hai purana data safe rahega aur nayi entry sabse niche judegi
with open("daily_register.txt", "a") as file:
    record = "Visitor: " + visitor_name + " | Flat: " + flat_no + " | Phone: " + phone_no + "\n"
    file.write(record)

print("\n[SUCCESS] Entry 'daily_register.txt' me safalta-poorvak jud gayi!")

# 3. अब तक के सारे दर्ज रिकॉर्ड स्क्रीन पर देखना (Read Mode "r")
print("\n--- Register me abhi tak ke darj log ---")
with open("daily_register.txt", "r") as file:
    content = file.read()
    print(content)
