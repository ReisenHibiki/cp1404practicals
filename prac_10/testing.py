"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between.
    >>> repeat_string("hi", 2)
    'hi hi'
    """
    words = []
    for i in range(n):
        words.append(s)
    return " ".join(words)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    False
    """
    return len(word) > length


def format_sentence(phrase):
    """format a phrase to be a sentence
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("saul goodman")
    'Saul goodman.'
    """
    sentence = str(phrase[0]).title()
    for i in range(1, len(phrase)):
        sentence += phrase[i]
    if phrase[-1] != ".":
        return sentence + "."
    return sentence


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"


    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"


    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel == 10
    test_car = Car(fuel=30)
    assert test_car.fuel == 30


run_tests()


# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()


# (don't change the tests, change the function!)


# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
# 'hello' -> 'Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (one that is valid!)
# test this and watch the tests fail
# then write the body of the function so that the tests pass