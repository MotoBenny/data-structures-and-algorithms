from data_structures.stack import Stack


class PseudoQueue:

    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, value):
        """
        Inserts value into the PseudoQueue, using a first-in, first-out approach
        """
        self.in_stack.push(value)

    def dequeue(self):
        """
        Extracts a value from the PseudoQueue, using a first-in, first-out approach
        If out_stack is not None, dequeue, else move all nodes from in_stack and then Pop node.
        """
        if self.out_stack.is_empty():  # if out_stack returns true, move all nodes from in_stack to out_stack
            while not self.in_stack.is_empty():  # while there are nodes in self.in_stack
                moving_node = self.in_stack.pop()
                self.out_stack.push(moving_node)
        return self.out_stack.pop()
