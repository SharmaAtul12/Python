# Password Generator
# Generate strong random passwords with customizable options

import random
import string

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type must be selected!")
        return None

    password = []

    # Ensure at least one character from each selected type
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    # Fill the rest randomly
    remaining = length - len(password)
    for _ in range(remaining):
        password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)


def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    levels = {0: "Very Weak", 1: "Weak", 2: "Fair", 3: "Moderate", 4: "Strong", 5: "Very Strong", 6: "Excellent"}
    return levels[score]


def main():
    print("=" * 40)
    print("   RANDOM PASSWORD GENERATOR")
    print("=" * 40)

    while True:
        print("\n1. Generate Password")
        print("2. Check Password Strength")
        print("3. Generate Multiple Passwords")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            try:
                length = int(input("Enter password length (min 4): "))
                if length < 4:
                    print("Length must be at least 4!")
                    continue
            except ValueError:
                print("Please enter a valid number!")
                continue

            upper = input("Include uppercase? (y/n): ").lower() == "y"
            lower = input("Include lowercase? (y/n): ").lower() == "y"
            digits = input("Include digits? (y/n): ").lower() == "y"
            special = input("Include special characters? (y/n): ").lower() == "y"

            password = generate_password(length, upper, lower, digits, special)
            if password:
                print(f"\nGenerated Password: {password}")
                print(f"Strength: {check_strength(password)}")

        elif choice == "2":
            password = input("Enter a password to check: ")
            print(f"Strength: {check_strength(password)}")

        elif choice == "3":
            try:
                count = int(input("How many passwords? "))
                length = int(input("Password length (min 4): "))
                if length < 4:
                    print("Length must be at least 4!")
                    continue
            except ValueError:
                print("Please enter valid numbers!")
                continue

            print(f"\n--- {count} Generated Passwords ---")
            for i in range(count):
                pwd = generate_password(length)
                print(f"  {i + 1}. {pwd}  [{check_strength(pwd)}]")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
