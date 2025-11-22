import random

def generate_password():
    length = int(input("Enter password length (minimum 6): "))

    while length < 6:
        print("Password must be at least 6 characters.")
        length = int(input("Enter password length again: "))

    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"

    characters = lowercase + uppercase + numbers

    password_list = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers)
    ]

    for i in range(length - 3):
        password_list.append(random.choice(characters))

    random.shuffle(password_list)

    password = "".join(password_list)
    print("Generated Password →", password)


play_again = "yes"

while play_again.lower() in ["yes", "y"]:
    generate_password()
    play_again = input("Generate another password? (yes/no): ")

print("Program Ended.")