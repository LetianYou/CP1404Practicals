"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = determine_score(score)
    print(f"The result is: {result}")

    random_score = random.randint(0, 100)
    random_result = determine_score(random_score)
    print(f"The random result is: {random_result}")


def determine_score(score):
    if score <= 0 or score >= 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
