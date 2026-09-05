# Day 7: Python Dictionary (Key-Value का जोड़ा)

# 1. एक छात्र (Student) की जानकारी का डिक्शनरी बनाना
student = {
    "name": "Manish",
    "course": "Python Basics",
    "day": 7,
    "is_learning": True
}

print("--- Student Profile ---")
print("Full Data:", student)

# 2. किसी एक ख़ास जानकारी को निकालना (Key के ज़रिए)
print("\nStudent Name:", student["name"])
print("Current Course:", student["course"])

# 3. नई जानकारी जोड़ना
student["city"] = "Delhi"
print("City jodne ke baad:", student)

# 4. पुरानी जानकारी बदलना (Update)
student["day"] = 8
print("Day update hone ke baad:", student["day"])

# 5. लूप से सारी जानकारी एक-एक करके देखना
print("\n--- All Details (Key-Value) ---")
for key, value in student.items():
    print(f"{key}: {value}")
