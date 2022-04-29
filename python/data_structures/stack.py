class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self, element):
        self.top = Node(element, self.top)  # set the head of the Stack to our new node
        self.size += 1  # increment the size by 1

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        result = self.top.value  # get the element to remove from the stack
        self.top = self.top.next  # set the new head of the stack
        self.size -= 1  # decrement the size by one
        return result  # return the elem we just removed from the list

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value  # return the element at the top of the stack

    def some_method(self):
        # method body here
        pass


class Node(Stack):
    def __init__(self, element, next_):
        self.value = element
        self.next = next_


class InvalidOperationError(Exception):
    pass

