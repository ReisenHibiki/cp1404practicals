password = input("Enter password: ")
while len(password) < 6:
    print("Password is too short!")
    password = input("Enter password: ")
print("*" * len(password))
