"""CP1404 score menu"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """display menu and get user choice"""
    print(MENU)
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "g":
            score = get_valid_score()
        elif choice == "p":
            result = determine_result(score)
            print(result)
        elif choice == "s":
            star = calculate_star(score)
            print(star)
        else:
            print("Invalid choice")
        choice = input(">>>").lower()

    print("Farewell")


def calculate_star(score):
    """calculate star"""
    star = "*" * score
    return star


def get_valid_score():
    """get valid score"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


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
