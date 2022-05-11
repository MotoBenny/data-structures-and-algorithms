# K-ary Tree Fizz Buzz

Given a K-ary tree of int values, traverse the tree returning a new tree with the values passed through "fizzBuzz"

# Challenge Summary

## No funciton required for this code challenge.
### Write a function called fizz buzz tree
Arguments: k-ary tree
Return: new k-ary tree
Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

If the value is divisible by 3, replace the value with “Fizz”
If the value is divisible by 5, replace the value with “Buzz”
If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process
  [Whiteboard](docs/tree-fizz-buzz/Whiteboard.jpeg)

## Approach & Efficiency

We begin traversing our K-ary tree, at the root node, we enqueue this node, Access its value and determine its - FizzBuzzy ness
And create a new node .root on a new node with appropriate value
We now access the first of the children nodes from our root,
And repeat the process in whole, until all the nodes do not contain any children lists.

Big 0: 0(n)

## Solution
You would run import the function and run it with your tree as a provided argument.
