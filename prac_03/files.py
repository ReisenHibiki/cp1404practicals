# Task 1
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()
# Task 2
in_file = open("name.txt", "r")
name = in_file.read()
print(f"Your name is {name}")
in_file.close()
# Task 3
number_file = open("numbers.txt", "r")
result = 0
for i in range(0,2):
    result += int(number_file.readline())
print(result)
number_file.close()
# Task 4
total_file = open("numbers.txt", "r")
total = 0
for line in total_file:
    total += int(line)
print(total)
total_file.close()
