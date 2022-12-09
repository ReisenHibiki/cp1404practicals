"""
Word Occurrences
Estimate: 15 minutes
Actual:   25 minutes
"""
email_to_name = {}
names = []
user_email = input("Email: ")

while user_email != "":
    names = user_email.split("@")
    full_names = names[0].split(".")
    try:
        user_choice = input(f"Is your name {full_names[0].title()} {full_names[1].title()}? (Y/n)").lower()
    except IndexError:
        user_choice = input(f"Is your name {full_names[0].title()}? (Y/n)").lower()
    if user_choice == "" or user_choice == "y":
        email_to_name[user_email] = names[0]
    else:
        user_name = input("Name: ")
        email_to_name[user_email] = user_name
    user_email = input("Email: ")

for i in email_to_name:
    print(f"{email_to_name[i]} {i}")
