# Day 26: Complete Digital Gatekeeper App (File + Loop + Conditions)

file_name = "society_register.txt"

while True:
    print("\n==============================")
    print("   SOCIETY GATEKEEPER APP     ")
    print("==============================")
    print("1. Naye Visitor ki Entry karein")
    print("2. Aaj ka Pura Register dekhein")
    print("3. Duty Khatam (Exit)")

    choice = input("\nApna option chunein (1/2/3): ")

    # Option 1: Nayi entry file me save karna
    if choice == "1":
        name = input("Visitor ka naam: ")
        flat = input("Flat number: ")
        
        # Append mode ("a") se file me likhna
        with open(file_name, "a") as f:
            f.write("Visitor: " + name + " | Flat: " + flat + "\n")
            
        print("[SUCCESS]", name, "ka record file me save ho gaya!")

    # Option 2: File padhkar screen par dikhana
    elif choice == "2":
        print("\n--- Aaj Ka Register Record ---")
        try:
            with open(file_name, "r") as f:
                content = f.read()
                if content == "":
                    print("Abhi register khali hai!")
                else:
                    print(content)
        except:
            print("Abhi tak koi record file nahi bani hai.")

    # Option 3: App band karna
    elif choice == "3":
        print("\nDuty samapt! System band ho raha hai...")
        break

    else:
        print("\n[ALERT] Galat number! Kripya 1, 2 ya 3 dabayein.")
