# Code Challenge 02
# InsertShiftArray
Feature Tasks

Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. \
Without utilizing any of the built-in methods available to your language,\
return the index of the array’s element that is equal to the value\
of the search key, or -1 if the element is not in the array.

## Collaborators
- Roger Wells

## Example
\
Input __________________________________	Output\
[4, 8, 15, 16, 23, 42], 15 _____________________	2 \
[-131, -82, 0, 27, 42, 68, 179], 42______________ 4 \
[11, 22, 33, 44, 55, 66, 77], 90	_______________ -1 \
[1, 2, 3, 5, 6, 7], 4	_________________________-1

## Whiteboard image
[Whiteboard Image](array-binary-search/Binary Search.jpeg)

# Code
```python
def binary_search(sorted_list, search_key):

  begin_index = 0
  end_index = len(sorted_list) -1

  while begin_index <= end_index:
    midpoint = begin_index + (end_index - begin_index) // 2
    midpoint_value = sorted_list[midpoint]

    if midpoint_value == search_key:
      return midpoint

    elif search_key < midpoint_value:
      end_index = midpoint - 1

    else:
      begin_index = midpoint + 1

  return int(-1)
```
