# Day 11: Visitor Exit System (.remove)

# 1. सोसाइटी या ऑफिस में मौजूद एक्टिव विज़िटर्स
active_visitors = ["Amit", "Rohan", "Pooja", "Manish"]

print("--- Security Exit Gate ---")
print("Abhi building ke andar maujood log:", active_visitors)

# 2. बाहर जाने वाले का नाम पूछना
exit_person = input("\nKaun bahar ja raha hai? Naam darj karein: ")

# 3. नाम चेक करके लिस्ट से हटाना
if exit_person in active_visitors:
    active_visitors.remove(exit_person)
    print("\n[EXIT SUCCESS]", exit_person, "bhai bahar nikal chuke hain.")
    print("Unka naam active list se hata diya gaya hai.")
else:
    print("\n[ERROR] Yeh naam active register me nahi mila!")

# 4. अब अंदर बचे हुए लोगों की लिस्ट दिखाना
print("\n--- Abhi Andar Maujood Visitors ---")
print("Bache hue log:", active_visitors)
print("Kul sankhya:", len(active_visitors))
