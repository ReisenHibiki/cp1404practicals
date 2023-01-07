from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

Menu = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator"""
    current_taxi = None
    bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(Menu)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            for i, taxi in enumerate(taxis, 0):
                print(f"{i} - {taxi}")
            current_taxi = get_valid_taxi(taxis)
            print(f"Bill to date: ${bill}")

        elif choice == "d":
            distance = int(input("Drive how far? "))
            current_taxi.drive(distance)
            print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare()}")
            bill += current_taxi.get_fare()
            print(f"Bill to date: ${bill}")

        else:
            print("Invalid option")
        print(Menu)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis, 0):
        print(f"{i} - {taxi}")


def get_valid_taxi(taxis):
    """get valid choice for taxi"""
    is_valid = False
    while not is_valid:
        try:
            choose_taxi = int(input("Choose taxi: "))
            current_taxi = taxis[choose_taxi]
            is_valid = True
        except IndexError:
            print("Invalid taxi choice")
        except ValueError:
            print("Invalid taxi choice")

    return current_taxi


main()
