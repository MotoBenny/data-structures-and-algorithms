# Code Challenge 02 InsertShiftArray

## Feature Tasks
Write a function called insertShiftArray which takes in an array and a value to be added.
Without utilizing any of the built-in methods available to your language, return an array
with the new value added at the middle index.

## Example
Input	                   Output
[2,4,6,-8], 5	       |   [2,4,5,6,-8] \
[42,8,15,23,42], 16	 |  [42,8,15,16,23,42]

## Whiteboard image

[Whiteboard Image](data-structures-and-algorithms/python/docs/array-insert-shift/Blank diagram.jpeg)


```python
import  math

list_1 = [2, 4, 6, -8]
list_2 = [42, 8, 15, 23, 42]

def insert_shift_list(list, value):
    middle_idx = int(len(list) / 2) + 1  # get middle index of list
    return list[:middle_idx] + [value] + list[middle_idx:]

insert_shift_list(list_1, 5)
insert_shift_list(list, 16)
```
