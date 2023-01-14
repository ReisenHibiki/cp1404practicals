import wikipedia

user_input = input(">>> ")
while user_input != "":
    try:
        page = wikipedia.page(user_input, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.WikipediaException:
        print("Error, please try again.")
    user_input = input(">>> ")

