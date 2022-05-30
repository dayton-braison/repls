# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Dayton's Password Generator!!")

number_of_letters = int(input("How many letters would you like in your password?\n"))

number_of_symbols = int(input("How many symbols would you like?\n"))

how_many_numbers = int(input("How many numbers would you like?\n"))

random_letters = random.choices(letters, k = number_of_letters)
random_symbols = random.choices(symbols, k = number_of_symbols)
random_numbers = random.choices(numbers, k = how_many_numbers)

my_password = random_letters + random_symbols + random_numbers
random.shuffle(my_password)
my_password = "".join(my_password)

print(my_password)
