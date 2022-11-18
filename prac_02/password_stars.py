def main():
    """get password and display asterisks"""
    password = get_password()
    display_asterisks(password)


def display_asterisks(password):
    """display asterisks"""
    print("*" * len(password))


def get_password():
    """get valid password"""
    password = input("Enter password: ")
    while len(password) < 6:
        print("Password is too short!")
        password = input("Enter password: ")
    return password


main()
