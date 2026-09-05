# Day 6: Python Functions (फ़ंक्शन बनाना और इस्तेमाल करना)

# 1. एक साधारण फ़ंक्शन जो नमस्ते कहे
def greet_user(name):
    message = f"Namaste, {name}! Python sikhne me aapka swagat hai."
    return message

# 2. फ़ंक्शन को अलग-अलग नामों के साथ चलाना (Call करना)
user1 = greet_user("Manish")
user2 = greet_user("Rohan")

print("--- Function Output 1 ---")
print(user1)
print(user2)

# 3. दो नंबरों को जोड़ने वाला फ़ंक्शन
def add_numbers(a, b):
    result = a + b
    return result

# 4. कैलकुलेटर फ़ंक्शन का इस्तेमाल
sum1 = add_numbers(15, 25)
sum2 = add_numbers(100, 250)

print("\n--- Function Output 2 (Addition) ---")
print("15 + 25 =", sum1)
print("100 + 250 =", sum2)
