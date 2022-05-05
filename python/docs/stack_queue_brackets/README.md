# Challenge Summary
Validate a string for matching bracket pairs, in valid pythonic order.

## Whiteboard Process
[Whiteboard](docs/stack_queue_brackets/WhiteBoard.png)

## Approach & Efficiency
Algorithm
instantiates a stack for char in input string, checks if char is open bracket, if so push to stack. else move to next conditionals if stack is empty return False else     save top of stack as compare value     now compare char against compare value, to check for matched closing bracket     if pair found, pop from stack and repeat with next char when this is done,     if stack is empty. all brackets had an appropriate match return True else;     Stack is not empty, return False
#### This solution is
BigO Time: O(N) \
BigO Space: O(N)
## Solution
Data structure class is not executable, it should be imported than used as needed.
