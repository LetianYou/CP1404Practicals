

def main():
    emails_names = {}

    email = input("Email: ")

    while email != "":
        name = extract_name(email)
        check_name = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if check_name == "" or check_name == "y":
            emails_names[email] = name
        else:
            name = input("Name: ").strip().title()
            emails_names[email] = name
        email = input("Email: ")

    for email, name in emails_names.items():
        print(f"{name} ({email})")


def extract_name(email):
    user_name = email.split("@")[0]
    name_part = user_name.split(".")
    return " ".join(name_part).title()


main()
