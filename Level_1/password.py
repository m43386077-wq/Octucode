import random
import string

password = []

# Welcome message
print("Welcome to the password generator!")

# Get user input for password information
length = input("Enter the total number of characters in the password: ")
letters = input("Enter the number of letters in the password: ")
numbers = input("Enter the number of numbers in the password: ")
symbols = input("Enter the number of symbols in the password: ")

if not length.isdigit() or not letters.isdigit() or not numbers.isdigit() or not symbols.isdigit():
    print("Error: Please enter valid numbers for length, letters, numbers, and symbols.")
    exit()

length = int(length)
letters = int(letters)
numbers = int(numbers)
symbols = int(symbols)

if letters + numbers + symbols != length:
    print("Error: The total number of characters does not match the sum of letters, numbers, and symbols.")
    exit()

# Generate the password
password.extend(random.choices(string.ascii_letters, k=letters))
password.extend(random.choices(string.digits, k=numbers))
password.extend(random.choices(string.punctuation, k=symbols))

random.shuffle(password)
print("Your generated password is:\n" + ''.join(password))
