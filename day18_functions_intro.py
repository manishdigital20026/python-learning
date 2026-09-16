# Day 18: Reusable Security Functions (def)

# 1. फ़ंक्शन बनाना (काम तय करना)
def gate_pass(naam, flat):
    print("\n------------------------------")
    print("      VISITOR ENTRY SLIP      ")
    print("------------------------------")
    print("Visitor Name :", naam)
    print("Flat Number  :", flat)
    print("Entry Status : Approved")
    print("------------------------------")

# 2. अब जब भी ज़रूरत हो, सिर्फ 1 लाइन में फ़ंक्शन को बुलाएँ (Call)
print("--- Gate Pass Generator Desk ---")

# पहली पर्ची
gate_pass("Amit", "101")

# दूसरी पर्ची
gate_pass("Pooja", "304")

# तीसरी पर्ची (यूज़र इनपुट के साथ)
user_naam = input("\nNaye aane wale ka naam likhein: ")
user_flat = input("Flat number darj karein: ")

# अपने बनाए फ़ंक्शन को इनपुट देकर चलाना
gate_pass(user_naam, user_flat)
