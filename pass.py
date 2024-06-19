import random
import string

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    password += random.choices(all_characters, k=length-4)
    random.shuffle(password)
    password = ''.join(password)

    return password

def main():
    print("Password Generator")
        length = int(input("Enter the desired length of the password: "))
if length < 4:
        print("Password length should be at least 4 characters to include a mix of character types.")
        return
    password = generate_password(length)

    # Display the generated password
    print(f"Generated password: {password}")

# Run the password generator
main()
