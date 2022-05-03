# Zip Linked List
Given two seperate linked lists, zip them together to form a single linked list.

# Challenge Summary
Write a function called zip lists
Arguments: 2 linked lists
Return: New Linked List, zipped as noted below
Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped list.
Try and keep additional space down to O(1)
You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Whiteboard Process
[Whiteboard](docs/linked_list_zip/Linkedlistzip.png)
## Approach & Efficiency
Args: Two linked lists
 if list1.head is None return B
if list2.head is None return A
Set heads of Current and check for next value
current A next becomes reference to old next value of A
current B next becomes reverence to old next value of B
set head of a.next to head of b
repeat until next = None

Time: 0(n)
Space 0(1)

## Solution
You would run linked_list_zip.py in the terminal calling the methods within.
its not currently an executable code base.
