import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

def generate_password():
    print("\nWelcome to the Password Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    password_list = []

    # Generate random letters
    password_list.extend(random.choices(letters, k=nr_letters))

    # Generate random symbols
    password_list.extend(random.choices(symbols, k=nr_symbols))

    # Generate random numbers
    password_list.extend(random.choices(numbers, k=nr_numbers))

    # Shuffle the password list
    random.shuffle(password_list)

    # Join the characters to form the password
    password = ''.join(password_list)

    print(f"Your password is: {password}")
    return password

def ask_questions():
    while True:
        like_password = input("Did you like your password? (yes/no): ").lower()
        if like_password == "yes":
            print("Great! Enjoy your password!")
            break
        elif like_password == "no":
            print("Let's generate a new password.")
            return True
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    while True:
        password = generate_password()
        if not ask_questions():
            break

if __name__ == "__main__":
    main()
