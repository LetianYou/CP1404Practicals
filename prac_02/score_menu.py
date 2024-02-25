

def main():
    score = float(input("Enter score: "))
    get_valid_score(score)

    print("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "G":
            score = float(input("Enter score: "))
            valid_score = get_valid_score(score)
            print(f"The valid score is: {valid_score}")
        elif menu_choice == "P":
            result = determine_score(score)
            print(f"The result is: {result}")
        elif menu_choice == "S":
            print(print_asterisks(score))

        print("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
        menu_choice = input(">>> ").upper()

    print(f"Farewell")


def get_valid_score(score):
    while score < 0 or score > 100:
        print("Please enter a valid score (0-100)")
        score = float(input("Enter score: "))
    return score


def determine_score(score):
    if score <= 0 or score >= 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_asterisks(score):
    return "*" * int(score)


main()
