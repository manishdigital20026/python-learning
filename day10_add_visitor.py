# Day 10: Automatic Visitor Registration System

# 1. पहले से मौजूद रजिस्टर
visitors = ["Amit", "Rohan", "Pooja"]

print("--- Welcome to Security Entry Desk ---")
print("Shuruat me register:", visitors)

# 2. आने वाले का नाम पूछना
name = input("\nApna naam darj karein: ")

# 3. नाम चेक करना और नया नाम जोड़ना
if name in visitors:
    print("Welcome back", name, "bhai! Aapka naam pehle se darj hai.")
else:
    print("Aap naye visitor hain. Aapka naam register me joda ja raha hai...")
    # naya naam list me add karna
    visitors.append(name)
    print("Safaltapoorvak jod diya gaya!")

# 4. अपडेट हुआ रजिस्टर देखना
print("\n--- Update Hua Register ---")
print("Kul visitors:", visitors)
print("Total count:", len(visitors))
