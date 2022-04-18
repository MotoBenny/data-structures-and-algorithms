# Code Challenge #1 Reverse Array

  Whiteboard out your process for reversing an array. Include pseudocode,
  or a whiteboard that details the steps.

Challenge: To reverse the elements in an array(list in python)

Example: [1, 2, 3, 4, 5] should become [5, 4, 3, 2, 1]

### Steps
1) initialize a new empty list
2) Access the value in index 0 of the original list.
3) remove it from the original list (now the value in index 0 is 2)
4) add that value to our new list in at index 0 of our new list.
5) continue accessing the next index from the original list,
and placing it in the new list at index 0, pushing the old value at index zero into index 1 and so on
6) Do this for every value in the original list, and your new list is now a reverse of the original.


## Whiteboard process
![WhiteBoard](https://github.com/MotoBenny/data-structures-and-algorithms/python/docs/array-reverse/Code_Challenge_#1_Reverse_Array.png)


## Approach and Efficiency
- This is a very simple way to go about this problem without the use of built in python methods, other than say pop.
- Its certainly a brute force method, but will produce a revered dataset every time. There would absolutely be more
efficient ways to perform this.
