import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input(f"How many symbols would you like? \n"))
nr_numbers = int(input(f"How many numbers would you like? \n"))

#Sequence("letters"+"number"+"symbols") Password Generator

password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)
for char in range(0, nr_symbols):
    password += random.choice(symbols)
for char in range(0, nr_numbers):
    password += random.choice(numbers)

print(f"Your sequential random password is : {password}")

#Random Password Generator

complex_password = []

for char in range(0,nr_letters):
    complex_password.append(random.choice(letters))
for char in range(0,nr_numbers):
    complex_password.append(random.choice(numbers))
for char in range(0,nr_symbols):
    complex_password.append(random.choice(symbols))

random.shuffle(complex_password)
complex_password_new = ""
for char in complex_password:
    complex_password_new += char
print(f"Your complex random password is : {complex_password_new}")


