menu = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(menu)
choice = input(">>> ").lower()
while choice != "q":
    if choice == "h":
        print(f"Hello {name}")
    elif choice == "g":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(menu)
    choice = input(">>> ").lower()

print("Finished")
