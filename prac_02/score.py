"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    """ask the user for their score and print the result."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    random_score = random.randint(0,100)
    result = determine_result(random_score)
    print(result)


def determine_result(score):
    """determine score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
