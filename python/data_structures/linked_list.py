class LinkedList:
    """
    This is a linked list class structure.
    I followed the readings we had on linked lists as reference.
    Reference Links included below
    https://www.educative.io/edpresso/how-to-create-a-linked-list-in-python
    https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-05/resources/singly_linked_list.html

    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def __str__(self):
        # Take in a response and return a string of the current nodes while traversing
        response = ""
        current = self.head
        while current:
            response += f"{{ {str(current.value)} }} -> "
            current = current.next
        return response + "NULL"

    def includes(self, value):
        """
        source https://realpython.com/linked-lists-python/
        In our use case we dont want to use a yield here since we dont need to return anything other than a
        Boolean value.
        True if value in linked list
        False if value not in linked list
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, new_value):
        """
        Append stores passed in element value as new_value, and calls new_node method with new_value as arg
        If self.head == None we are at the end of the linked list, and can save our new node here.
        Else we save the value of self.head as held_value, so we dont lose the element stored there.
        while we have values in the nodes, or .next does not = None, reassign held_value to held_value.next
        and traverse to the next node, until we have self.node == None.
        """
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        else:
            held_value = self.head
            while held_value.next is not None:
                held_value = held_value.next
            held_value.next = new_node

    def insert_before(self, value, new_value):
        """
        make and store our new node
        iterate through our list, looking for our before. Storing the element previous to it each time.
        once we found the elem which equals our before, we can iterate through the list until we find its
        previous elem, from there we can reassign next to our new node, and insert our new node, with a .next
        equal to the before elem.

        """
        new_node = Node(new_value)  # new node
        current = self.head

        if self.head is None:
            raise TargetError

        if self.includes(value) is False:
            raise TargetError

        if current.value is value:  # if we are at the node we want to insert before
            new_node.next = self.head  # new_node.next = the current node
            self.head = new_node  # set our new node as head

        while current.next is not None:
            if current.next.value is value:  # if the next node is what we want to insert before
                new_node.next = current.next  # reassign next pointer of new node, to the item to insert before
                current.next = new_node  # reassign our current node as our newly formatted new node
                return
            else:
                current = current.next  # traverse to the next node

    def insert_after(self, value, new_value):
        """
        inserts a node after a given value
        """

        if self.head is None:
            raise TargetError

        if self.includes(value) is False:
            raise TargetError

        new_node = Node(new_value)
        current = self.head
        while current:
            if current.value is value:
                new_node.next = current.next
                current.next = new_node
                break

    def kth_from_end(self, k):
        """
        Method finds the kth node from the end of a linked list, and returns its value
        input:
            k < the value from the end we want to find Type: int
        output:
            The value stored at that node within the linked list. exp: "apple"
        """
        length = 0
        current = self.head
        # count the total number of nodes in the linked list
        while current:
            current = current.next
            length = length + 1

        if k >= length:  # If K is greater than the length of our list > Error
            raise TargetError
        if k < 0:  # If k arg is negative number > Error
            raise TargetError

        if length >= k:
            current = self.head
            for i in range(length - k - 1):  # this minus one had me for a while... thanks replit.
                current = current.next

        return current.value

    def zip_lists(self):
        pass


class Node:
    """
    next in this case is not exactly a reserved term, but it is used, so without the _ the linter got real angry
    we asked JB about the linter error, and were taught about adding _ to the end of the variable name.
    """

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class TargetError(Exception):
    pass
