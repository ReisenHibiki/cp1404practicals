def main():
    """"""
    password = get_password()
    display_asterisks(password)


def display_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    while len(password) < 6:
        print("Password is too short!")
        password = input("Enter password: ")
    return password


main()
