# Challenge Summary
Implement a Queue using two Stacks.

## Whiteboard Process
[Whiteboard](docs/stack_queue_pseudo/Blank_board_(1).jpeg)

## Approach & Efficiency
Algorithm
We create two instances of the Stack class
an in_stack and an out_stack
To enqueue, we call the .push method, passing it the value as arg on our in_stack
To dequeue, we must first check out_stack.is_empty
if return is True(Bool) we use a while loop to move all nodes from in_stack to out_stack, until in_stack.is_empty returns True(Bool)
We then call out_stack.pop which returns the Node on the top of our out_stack.
#### This solution is
BigO Time: O(N) \
BigO Space: O(1)
## Solution
Data structure class is not executable, it should be imported than used as needed.
