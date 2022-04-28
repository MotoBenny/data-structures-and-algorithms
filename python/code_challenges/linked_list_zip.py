from data_structures.linked_list import LinkedList, Node


def zip_lists(list1, list2):


    curr1 = list1.head
    curr2 = list2.head
    temp1 = curr1.next
    temp2 = curr2.next

    while curr1 is not None:
        curr1.next = curr2
        curr2.next = temp1
        curr1 = temp1
        curr2 = temp2






# incomplete this method calls the exsiting append value.
def zip_2(list1, list2):
    result = LinkedList()
    current_1 = list1.head
    current_2 = list2.head

    if current_1 is None:
        return list2

    if current_2 is None:
        return list1

