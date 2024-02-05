import random

def get_password():
    """
    Prompts the user for desired password length and complexity,
    generates a random password based on their input, and returns it.
    """
    uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    numbers = input("Include numbers? (y/n): ").lower() == "y"
    symbols = input("Include symbols? (y/n): ").lower() == "y"

    # Create a character pool based on user-selected complexity
    characters = []
    if uppercase:
        characters.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if lowercase:
        characters.extend("abcdefghijklmnopqrstuvwxyz")
    if numbers:
        characters.extend("0123456789")
    if symbols:
        characters.extend("!@#$%^&*()_+-=[]{};:\"<>/?\\|~")

    if not characters:
        print("Error: Please choose at least one complexity option.")
        return None

    return characters

def is_valid_password(password):
    if len(password) >= 8:
        return True
    else:
        print("Password length should be 8 or more characters.")
        return False

def main():
    print("This a password generator based on yoyr desrired length.\n")
    while True:  
        length = int(input("\nEnter password length : "))
        if length >= 8:  
            break
        else:
            print("Password length should be 8 or more characters. Please try again.")
    characters = get_password()
    if characters is None:
        return

    password = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    # Track if a number has been added
    number_added = False
    
    for _ in range(length - 1):
        char = random.choice(characters)
        if '0' <= char <= '9' and not number_added:
            password += char
            number_added = True
        else:
            password += char

    if not is_valid_password(password):
        return False

    print(f"\nYour generated password: {password}\n")

if __name__ == "__main__":
    main()
