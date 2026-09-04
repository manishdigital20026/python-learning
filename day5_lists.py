# Day 5: Python Lists (चीज़ों की सूची बनाना और संभालना)

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("--- My Fruit List ---")
print("All Fruits:", fruits)
print("पहला फल (First fruit):", fruits[0])

fruits.append("Grapes")
print("नया फल जोड़ने के बाद:", fruits)

print("\n--- लिस्ट के सभी आइटम ---")
for fruit in fruits:
    print("Fruit name:", fruit)

print("\nTotal items in list:", len(fruits))
