# A program that generates strong passwords.
import string
import random

print("Welcome to the password generator")
nr_letters = int(input("How many letters would you like in  your passowrd ?\n"))
nr_symbols = int(input("How many symbols would you like ?\n"))
nr_numbers = int(input("How many numbers would you like ?\n"))

# List of alphabets, numbers and symbols.
list_alpha = list(string.ascii_lowercase+string.ascii_uppercase)
list_num = list(range(0,10))
list_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ''

# Getting the letters.
letters = ''
for i in range(nr_letters):
#    letters += list_alpha[random.randint(0,51)] - alt. to random.choice() method.
    letters += random.choice(list_alpha)

# Getting the symbols.
symbols = ''
for i in range(nr_symbols):
    symbols += random.choice(list_symbols)

# Getting the digits.
numbers = ''
for i in range(nr_numbers):
    numbers += str(random.choice(list_num))

# Setting the unshuffled password.
password = list(letters+symbols+numbers)

# This is me avoiding to use the random.shuffle() method. Remove the ( )
#(shuffledPassword = '')
#(for i in range(len(password)):)
#(    shuffledPassword += password[random.randint(0,len(password)-1)])

# Shuffling the password.
random.shuffle(password)

# Converting passowrd back to a string.
#shuffled_password = ''.join(password)
shuffled_password = ''
for char in password:
    shuffled_password += char
print(shuffled_password)
