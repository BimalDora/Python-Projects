# PyPassword Generator
import random
print("Welcome to PyPassword Generator!")
letters_count = int(input("How many letters would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
password = ""

for i in range(letters_count):
    random_index = random.randint(0, len(letters) - 1)
    random_letter = letters[random_index]
    password += random_letter

for j in range(symbols_count):
    random_index = random.randint(0, len(symbols) - 1)
    random_symbol = symbols[random_index]
    password += random_symbol


for k in range(numbers_count):
    random_index = random.randint(0, len(numbers) - 1)
    random_number = numbers[random_index]
    password += str(random_number)

hard_password = ""
for c in range(len(password)):
    random_index = random.randint(0, len(password) - 1)
    random_char = password[random_index]
    hard_password += random_char
print(hard_password)
