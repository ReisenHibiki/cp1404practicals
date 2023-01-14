import wikipedia

user_input = input(">>> ")
while user_input != "":
    page = wikipedia.page(user_input, auto_suggest=False)
    print(page.title)
    print(page.summary)
    print(page.url)

    user_input = input(">>> ")

