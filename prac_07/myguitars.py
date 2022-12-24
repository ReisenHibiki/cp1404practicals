from prac_06.guitar import Guitar
guitars = []

in_file = open("guitars.csv", "r")
in_file.readline()

for line in in_file:
    parts = line.strip().split(",")
    guitar = Guitar(parts[0], int(parts[1]), parts[2])
    guitars.append(guitar)

in_file.close()
guitars.sort()

guitar_name = input("Name: ")
guitar_year = int(input("Year: "))
guitar_cost = float(input("Cost: $"))
guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
print(f"{guitar_name} ({guitar_year}) : ${guitar_cost} added.\n")

out_file = open("guitars.csv", "w")
for i in guitars:
    print(f"{i.name}, {i.year}, {i.cost},", file=out_file)
out_file.close()
