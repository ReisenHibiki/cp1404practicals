"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the input is not a valid number.

2. When will a ZeroDivisionError occur?
When the denominator is 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, I could use a while loop to ensure that the input is only accepted when it's not zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Invalid input")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")