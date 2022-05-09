# Trees
Binary Tree Max.

## Challenge
Write the following method for the Binary Tree class

find maximum value
Arguments: none
Returns: number
Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Approach & Efficiency
The algorithms for the Binary Trees, Begin with the root node, If the new node is greater than root.value
and a root.left exists we recursively call the algorithm on that new left node,
Otherwise that left node becomes our new value.

The Big O is: Log(N)
## API

