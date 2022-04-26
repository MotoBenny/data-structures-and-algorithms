# Challenge Summary
Expand on the linked list challenge from last week,
adding three different methods to insert nodes.

* Append: Adds a new node to the end of the linked list
* Insert Before: Adds a new node just before a provided node in the list
* Insert After: Adds a new node just after a provided node in the list

## Whiteboard Process
[Whiteboard](python/docs/linked_list_insertions/White Board.png)
## Approach & Efficiency
* Append: Append stores passed in element value as new_value, and calls new_node method with new_value as arg
        If self.head == None we are at the end of the linked list, and can save our new node here.
        Else we save the value of self.head as held_value, so we dont lose the element stored there.
        while we have values in the nodes, or .next does not = None, reassign held_value to held_value.next
        and traverse to the next node, until we have self.node == None.
* Insert Before: make and store our new node
        iterate through our list, looking for our before. Storing the element previous to it each time.
        once we found the elem which equals our before, we can iterate through the list until we find its
        previous elem, from there we can reassign next to our new node, and insert our new node, with a .next
        equal to the before elem.
* Insert After: Make and store our new node, and our current. then continue to reset our
new_node.next to our current.next until current.value equals the value we are searching for.
then assign our new node to current.next, to insert our new Node after the given val.


## Solution
You would run Linked_list.py in the terminal calling the methods within.
its not currently an executable code base.
