for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""a. count in 10s from 0 to 100:"""

for j in range(0, 101, 10):
    print(j, end=" ")
print()

"""b. count down from 20 to 1:"""

for k in range(20, 0, -1):
    print(k, end=" ")
print()

"""c. print n stars."""

number = int(input("Number of stars: "))
for p in range(0, number):
    print("*", end="")
print()

"""d. print n lines of increasing stars."""

for y in range(1, number + 1):
    print("*" * y)
