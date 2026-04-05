import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    if strength <= 2:
        return "Weak ❌"
    elif strength == 3 or strength == 4:
        return "Medium ⚠️"
    else:
        return "Strong ✅"

def main():
    while True:
        print("\n1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            length = int(input("Enter password length: "))
            password = generate_password(length)
            print("Generated Password:", password)

        elif choice == '2':
            password = input("Enter password to check: ")
            print("Strength:", check_strength(password))

        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
