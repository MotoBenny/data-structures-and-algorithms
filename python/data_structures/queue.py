class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        new = Node(element, None)  # this will be the new tail node hence the None for the next_ prop
        if self.is_empty():  # if the Queue is empty our new node is the new head
            self.front = new  # our new node becomes the new Head of the list.
        else:
            self.tail.next = new  # if the queue isnt empty our new node becomes the new tail (back of the queue)
        self.tail = new  # out new tail (or back of the queue) is our new node, that weve just added.
        self.size += 1  # we increase our size by 1

    def dequeue(self):
        if self.is_empty():  # nothing to remove!
            raise InvalidOperationError()  # nothing to remove as list is empty
        result = self.front.value  # grab the element we are going to remove from the queue
        self.front = self.front.next  # sets the new head element
        self.size -= 1  # maintains the size value of the queue
        if self.is_empty():  # of the queue is now empty, we need to set the tail to None
            self.tail = None
        return result  # gives us the element we just removed from the queue.

    def peek(self):  # show me the node at the front of the queue
        if self.is_empty():  # if the queue is empty you cant show the node!
            raise InvalidOperationError()
        return self.front.value  # return the element at the front of the queue

    def some_method(self):
        # method body here
        pass


class Node:
    def __init__(self, element, next_):
        self.value = element
        self.next = next_


class InvalidOperationError(Exception):
    pass
