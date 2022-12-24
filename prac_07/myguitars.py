from prac_06.guitar import Guitar
guitars = []

in_file = open("guitars.csv", "r")
in_file.readline()

for line in in_file:
    parts = line.strip().split(",")
    guitar = Guitar(parts[0], int(parts[1]), parts[2])
    guitars.append(guitar)

guitars.sort()
for i in guitars:
    print(i)
