from data_structures.linked_list import LinkedList


def zip_lists(a, b):
    current_a = a.head
    current_b = b.head

    while current_b and current_a:
        a.insert_after(current_a.value, current_b.value)
        current_a = current_a.next
        if current_a.next:
            current_a = current_a.next
        current_b = current_b.next

    if current_a is None or current_b is None:
        if current_b:
            return b
        if current_a:
            return a

    return a

# def zip_lists(a, b=None):
#     result = LinkedList()
#     current_a = a.head
#     current_b = b.head
#
#     if current_a is None:
#         return b
#
#     elif current_b is None:
#         return a
#
#     while current_a and current_b:
#         result.append(current_a.value)
#         current_a = current_a.next
#         result.append(current_b.value)
#         current_b = current_b.next
#
#     while current_b:
#         result.append(current_b.value)
#         current_b = current_b.next
#
#     while current_a:
#         result.append(current_a.value)
#         current_a = current_a.next
#
#     return result
