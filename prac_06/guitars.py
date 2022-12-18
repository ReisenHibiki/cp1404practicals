"""
Estimate: 25 minutes
Actual:   35 minutes
"""

from prac_06.guitar import Guitar

guitars = []


def main():
    get_guitar_input()

    print("\n... snip ...\n")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def get_guitar_input():
    guitar_name = input("Name: ")
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: $"))
    guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
    print(f"{guitar_name} ({guitar_year}) : ${guitar_cost} added.\n")
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        print(f"{guitar_name} ({guitar_year}) : ${guitar_cost} added.\n")
        guitar_name = input("Name: ")


main()
