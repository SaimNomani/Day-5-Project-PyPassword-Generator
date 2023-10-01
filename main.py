# Develop a Python program for generating secure and random passwords. The program should combine uppercase letters,
# lowercase letters, symbols, and digits to create
# strong and unique passwords with varying lengths.
###########################################################################
import random

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                     'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                     'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
           '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("Welcome to the PyPassword Generator: ")
###########################################
# Randomly determine the number of uppercase letters, lowercase letters,
# special characters, and symbols to include in the password.
random_no_uppercase_letter = random.randint(3, 7)
random_no_lowercase_letter = random.randint(3, 6)
random_no_symbols = random.randint(3, 5)
random_no_digits = random.randint(3, 4)
###############################################
password_list = []
password = ""
for char in range(0, random_no_uppercase_letter):
    # Randomly generate uppercase letters and add them to the list.
    random_uppercase_letters = random.choice(uppercase_letters)
    password_list.append(random_uppercase_letters)
for char in range(0, random_no_lowercase_letter):
    # Randomly generate lowercase letters and add them to the list.
    random_lowercase_letters = random.choice(lowercase_letters)
    password_list.append(random_lowercase_letters)
for char in range(0, random_no_symbols):
    # Randomly generate symbols and add them to the list.
    random_symbols = random.choice(symbols)
    password_list.append(random_symbols)
for char in range(0, random_no_digits):
    # Randomly generate digits and add them to the list.
    random_digits = random.choice(digits)
    password_list.append(random_digits)
    # shuffling list to create more randomness in password
random.shuffle(password_list)
for char in password_list:
    password += char
print(f"\npassword: {password}")
