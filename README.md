# 132453---Linked-List-Assignment - Larry Mburu

So first things first, we have to create a representation for each of the nodes on the list. 
This will be done using the `Node` class, where each node stores the value of the data in the `data` attribute and also contains a reference to the next node using the `next` attribute, initially set to `None`. 

After defining the node, we define a `LinkedList` class to manage the sequence of nodes. 

The linked list starts with a `head` pointer that keeps track of the first node in the list. 

The `insert_at_beginning()` method adds a new node at the start of the list by setting its `next` pointer to the current head and then updating the head to this new node. 

The `insert_at_end()` method traverses the list until it reaches the last node and then appends a new node at the end by updating the last node’s `next` pointer. 

The `insert_after_value()` method searches for a node with a specified value and inserts a new node right after it by adjusting pointers. If the value is not found, it prints an error message. 

The `delete_by_value()` method is responsible for removing the first node that matches the given value, carefully updating pointers to remove the node without breaking the list. 
If the value isn’t found or the list is empty, appropriate messages are shown. 

Finally, the `display()` method traverses the list and prints out each node’s value in order, showing the flow from head to tail with arrows (`->`). 

The `__main__` block at the end demonstrates how each method works step-by-step: inserting nodes at the beginning and end, inserting after a specific value, and deleting nodes based on value, including an attempt to delete a non-existent value.
