"""
Estimate: 10 minutes
Actual:   6 minutes
"""

from prac_06.guitar import Guitar

test_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)

print("Expected 100.")
print(test_guitar.get_age())
print("Expected True.")
print(test_guitar.is_vintage())
