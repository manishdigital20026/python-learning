# Day 20: Smart Parking Bill with Discount (def + if-else + return)

# 1. छूट का हिसाब लगाने वाला फ़ंक्शन
def calculate_bill(hours):
    rate = 20  # har ghante ka 20 rupaye
    raw_amount = hours * rate

    # agar 5 ghante ya usse zyada hai to 50 rs discount
    if hours >= 5:
        discount = 50
        final_bill = raw_amount - discount
        print("[OFFER APPLIED] 5+ ghante rehne par Rs. 50 ki chhoot mili!")
    else:
        final_bill = raw_amount
        print("[NORMAL RATE] Koi discount lagu nahi hua.")

    return final_bill  # aakhiri rakam wapas bhejna

print("--- Smart Apartment Parking Counter ---")

# 2. यूज़र से इनपुट लेना
stay_hours = input("Gaadi kitne ghante khadi rahi? (Number darj karein): ")
stay_hours = int(stay_hours)

# 3. फ़ंक्शन को कॉल करके नतीजा पाना
total_to_pay = calculate_bill(stay_hours)

# 4. रसीद दिखाना
print("\n==============================")
print("     PARKING CASH RECEIPT     ")
print("==============================")
print("Total Time :", stay_hours, "Ghante")
print("Total Bill : Rs.", total_to_pay)
print("Status     : Bill Generated")
print("==============================")
