# Day 19: Function with Return Value (Parking Fee Calculation)

# 1. पार्किंग चार्ज का हिसाब लगाने वाला फ़ंक्शन
def hisaab_lagao(ghante):
    rate_per_hour = 20  # har ghante ka 20 rupaye
    total_bill = ghante * rate_per_hour
    return total_bill  # nateeja wapas bhejo

print("--- Apartment Parking Billing Desk ---")

# 2. यूज़र से पूछना कि गाड़ी कितने घंटे खड़ी रही
hours_parked = input("Gadi kitne ghante khadi rahi? (Number likhein): ")

# इनपुट को नंबर (int) में बदलना
hours_parked = int(hours_parked)

# 3. फ़ंक्शन को बुलाना और उसका नतीजा एक डिब्बे में पकड़ना
final_amount = hisaab_lagao(hours_parked)

# 4. रसीद दिखाना
print("\n==============================")
print("     PARKING FEE RECEIPT      ")
print("==============================")
print("Total Samay :", hours_parked, "Ghante")
print("Total Bill  : Rs.", final_amount)
print("Status      : Payment Due")
print("==============================")
