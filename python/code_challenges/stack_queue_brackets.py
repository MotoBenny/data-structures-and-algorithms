from data_structures.stack import Stack


def multi_bracket_validation(string):

    brackets = Stack()

    for char in string:
        if char == '[' or char == '{' or char == '(':  # if char is open bracket push to stack
            brackets.push(char)
        else:
            if brackets.is_empty():  # if stack is empty after pushing all open brackets to it, False
                return False
            else:
                compare = brackets.peek()  # get the top value save it to compare
                print(compare)
                if char == ')' and compare == '(':  # if char is close, and top of stack is pair opening
                    brackets.pop()  # we have found pair, remove from stack and move to next char
                if char == ']' and compare == '[':
                    brackets.pop()
                if char == '}' and compare == '{':
                    brackets.pop()
    if brackets.is_empty():  # If after all that brackets is empty, we have all perfect matches! return True
        return True
    else:  # there are brackets left in stack! that means we had a non match somewhere, return False!
        return False

"""
Algorithm

instantiates a stack
for char in input string, checks if char is open bracket, if so push to stack.
else move to next conditionals
if stack is empty return False
else
    save top of stack as compare value
    now compare char against compare value, to check for matched closing bracket
    if pair found, pop from stack and repeat with next char
when this is done,
    if stack is empty. all brackets had an appropriate match return True
else;
    Stack is not empty, return False
"""
