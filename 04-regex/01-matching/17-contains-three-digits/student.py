# Write your code here
import re


def contains_three_digits(string):
    return re.fullmatch("[0-9]{3,}", string)
