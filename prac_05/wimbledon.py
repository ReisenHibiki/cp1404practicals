"""
Word Occurrences
Estimate: 20 minutes
Actual:   35 minutes
"""

FILE_NAME = "wimbledon.csv"
texts = []
names = []
name_to_count = {}
countries = []


def main():
    open_files()

    get_names_countries()

    display_names_counts()

    display_countries()


def display_countries():
    print()
    print("These 12 countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


def display_names_counts():
    for name in names:
        name_to_count[name] = name_to_count.get(name, 0) + 1
    for j in name_to_count:
        print(f"{j} {name_to_count[j]}")


def open_files():
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            # print(repr(line))
            line = line.strip().split(",")
            texts.append(line)


def get_names_countries():
    for i in range(2, len(texts)):
        names.append(texts[i][2])
        country_name = str(texts[i][1])
        if country_name not in countries:
            countries.append(country_name)


main()
