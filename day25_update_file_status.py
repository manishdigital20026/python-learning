# Day 25: Update Visitor Status from 'In' to 'Out' in File

# 1. अभ्यास के लिए फ़ाइल में 2 विज़िटर्स का डेटा रखना
with open("daily_register.txt", "w") as file:
    file.write("Visitor: Amit | Flat: 101 | Status: In\n")
    file.write("Visitor: Manish | Flat: 202 | Status: In\n")

print("--- Visitor Exit & Status Update Desk ---")

# 2. यूज़र से पूछना कि कौन बाहर जा रहा है
exit_name = input("Kaun bahar ja raha hai? Naam darj karein: ")

# 3. फ़ाइल की सारी सामग्री पढ़ना
with open("daily_register.txt", "r") as file:
    data = file.read()

# 4. अगर नाम फ़ाइल में है, तो उसका Status: In बदलकर Status: Out करना
old_text = "Visitor: " + exit_name + " | Flat: 202 | Status: In"
new_text = "Visitor: " + exit_name + " | Flat: 202 | Status: Out"

if exit_name in data:
    # replace() purane text ko naye text se badal deta hai
    updated_data = data.replace("Status: In", "Status: Out", 1)
    
    # badli hui jankari wapas file me likhna
    with open("daily_register.txt", "w") as file:
        file.write(updated_data)
        
    print("\n[UPDATE SUCCESS]", exit_name, "ka status 'Out' kar diya gaya!")
else:
    print("\n[ERROR] Yeh naam register me nahi mila!")

# 5. अपडेट हुआ नया रजिस्टर स्क्रीन पर देखना
print("\n--- Updated File Register ---")
with open("daily_register.txt", "r") as file:
    print(file.read())
