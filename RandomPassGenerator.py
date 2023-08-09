#to generate the random
import random

#the letters, both lower and upper case
letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A","B","C","D","E",
    "F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W","X","Y","Z"
]

#the numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#the most common special characters
special_characters = [
    "!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "+", "=", "<",
    ">", "?", "/"
]

#the users input, to decide how much letters, numbers or special characters the user wants
num_letters = int(input("Enter how many letters do you want: "))
num_numbers = int(input("Enter how many numbers do you want: "))
num_special = int(input("Enter how many special characters do you want: "))

#the variable for the pass
password = ""

for x in range(num_letters):
    password += random.choice(letters)

for x in range(num_numbers):
    password += str(random.choice(numbers))

for x in range(num_special):
    password += random.choice(special_characters)

print("The generated password:", password)
