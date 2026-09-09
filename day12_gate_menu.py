# Day 12: Continuous Visitor Gate Menu System

# 1. शुरूआती विज़िटर रजिस्टर
visitors = ["Amit", "Rohan"]

# 2. लगातार चलने वाला लूप
while True:
    print("\n--- Digital Security Menu ---")
    print("1. Nayi Entry karein")
    print("2. Bahar Exit karein")
    print("3. Register dekhein")
    print("4. Duty khatam (Exit App)")

    choice = input("\nApna option chunein (1/2/3/4): ")

    # Option 1: Entry
    if choice == "1":
        name = input("Aane wale ka naam likhein: ")
        visitors.append(name)
        print("[SUCCESS]", name, "ka naam register me jud gaya!")

    # Option 2: Exit
    elif choice == "2":
        name = input("Bahar jane wale ka naam likhein: ")
        if name in visitors:
            visitors.remove(name)
            print("[SUCCESS]", name, "bahar ja chuke hain.")
        else:
            print("[ERROR] Yeh naam register me nahi hai!")

    # Option 3: List
    elif choice == "3":
        print("\nAbhi andar maujood log:", visitors)
        print("Total log:", len(visitors))

    # Option 4: Loop todna (Break)
    elif choice == "4":
        print("Duty khatam! Gate system band ho raha hai...")
        break

    # Galat button dabane par
    else:
        print("[INVALID] Kripya 1, 2, 3 ya 4 me se chunein!")
