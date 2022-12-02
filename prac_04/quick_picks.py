import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBER_EVERY_LINE = 6

number_of_lines = int(input("How many quick picks: "))
for line in range(number_of_lines):
    numbers = []
    for i in range(NUMBER_EVERY_LINE):
        random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while random_number in numbers:
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        numbers.append(random_number)
    numbers = sorted(numbers)
    for j in numbers:
        print(f"{j:2}", end=" ")
    print()
