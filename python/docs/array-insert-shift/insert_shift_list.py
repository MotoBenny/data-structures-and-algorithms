"""
## Feature Tasks
Write a function called insertShiftArray which takes in an array and a value to be added.
Without utilizing any of the built-in methods available to your language, return an array
with the new value added at the middle index.

"""

# this function should find the halfway mark in the list, and re-assign the value at that index to the value argument
# it should then work its way through the remainder of the elements and re-assign them until the array has the new
# value inserted.
import math
nums = [0, 1, 2, 3, -6]


def insert_shift_list(list, value):
    middle_idx = int(len(list) / 2) + 1  # get middle index of list
    return list[:middle_idx] + [value] + list[middle_idx:]
