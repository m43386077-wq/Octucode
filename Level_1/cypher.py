from string import ascii_lowercase as alphabet

def encrypt(message, shift):
    encrypted_message = ""

    for letter in message:
        
        if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            new_position = (original_position + shift) % 26
            encrypted_letter = alphabet[new_position]
            if letter.isupper():
                encrypted_letter = encrypted_letter.upper()
            encrypted_message += encrypted_letter

        else:
            encrypted_message += letter

    return encrypted_message

def decrypt(message, shift):
    decrypted_message = ""

    for letter in message:
        
        if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            new_position = (original_position - shift) % 26
            decrypted_letter = alphabet[new_position]
            if letter.isupper():
                decrypted_letter = decrypted_letter.upper()
            decrypted_message += decrypted_letter

        else:
            decrypted_message += letter

    return decrypted_message

# message
message = input("Enter a message: ")
message = [char for char in message]

# Shift
shift = input("Enter a shift number: ")
if not shift.isdigit():
    print("Invalid input. Please enter a numeric value.")
    exit()
shift = int(shift)

# cypher
cypher = input("Encrypt or Decrypt: ").lower()

# print the cypherd message
if cypher == "encrypt":
    print(encrypt(message, shift))
elif cypher == "decrypt":
    print(decrypt(message, shift))
else:
    print("Invalid Choice!")
