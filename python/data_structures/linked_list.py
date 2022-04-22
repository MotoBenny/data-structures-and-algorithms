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


class Node:
    """
    next in this case is not exactly a reserved term, but it is used, so without the _ the linter got real angry
    we asked JB about the linter error, and were taught about adding _ to the end of the variable name.
    """

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class TargetError:
    pass
