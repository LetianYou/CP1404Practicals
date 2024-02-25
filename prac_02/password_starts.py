PASSWORD_MINIMUM_LENGTH = 6


def main():
    password = get_password()
    password = error_check_password_len(password)
    print_asterisks(password)


def get_password():
    return input("Please enter the password: ")


def error_check_password_len(password):
    while len(password) < PASSWORD_MINIMUM_LENGTH:
        print(f"Please enter at least {PASSWORD_MINIMUM_LENGTH} characters")
        password = input("Please enter the password: ")
    return password


def print_asterisks(password):
    print("*" * len(password))


main()
