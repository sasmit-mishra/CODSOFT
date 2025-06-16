import random
import string

def generate_password(length):
    if length < 4:
        return "Password should be at least 4 characters long."

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = lowercase + uppercase + digits + symbols

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Main loop
while True:
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")
        continue

    choice = input("Enter 1 to generate another password or any other key to exit: ")
    if choice != '1':
        print("Exiting the password generator. Goodbye!")
        break
