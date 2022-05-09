# Trees
Binary Tree Max.

## Challenge
Write the following method for the Binary Tree class

find maximum value
Arguments: none
Returns: number
Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## WhiteBoard
[whiteboard](docs/tree_max/Blank board (1).png)

## Approach & Efficiency
Function begins by defining a climb function
If there is no root, we return none.
We then compare our root value against a temp Max variable. we procced to climb through the tree recursively calling our climb function. If root.value > max value re reassign max value to root.value


The Big O time and space is O(n) since we need to check every node in the tree
## API

