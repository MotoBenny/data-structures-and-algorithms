# Breadth First Tree traversal
Traverse a binary tree and return a list of the elements in a breadth first format.

# Challenge Summary
Write a function called breadth first
Arguments: tree
Return: list of all values in the tree, in the order they were encountered
NOTE: Traverse the input tree using a Breadth-first approach

## Whiteboard Process
[Whiteboard](docs/tree_breadth_first/Blank board.png)

## Approach & Efficiency
We initially instantiate a new Queue, and an empty list,
If tree input is None, we return our empty list.
If the queue has no front value, we begin by enqueuing tree.root
While the queue has a front node,
we set our root to equal the return from our queue.dequeue
and we append that new root.value to our values list.
if there is a root.left
we enqueue it to our queue
same for if there is a root.right

Once not Breadth.front
we return our values list.

## Solution
You would run import the function and run it with your tree as a provided argument.
