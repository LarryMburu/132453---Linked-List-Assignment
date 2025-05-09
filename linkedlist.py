class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def insert_after_value(self, target_value, data):
        curr = self.head
        while curr:
            if curr.data == target_value:
                new_node = Node(data)
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next
        print(f"Value {target_value} not found in the list.")

    def delete_by_value(self, value):
        if not self.head:
            print("List is empty.")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next
        while curr:
            if curr.data == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        print(f"Value {value} not found in the list.")

    def display(self):
        if not self.head:
            print("The list is empty.")
            return

        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")


if __name__ == "__main__":
    llist = LinkedList()

    print("Inserting at the beginning:")
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(5)
    llist.display()

    print("\nInserting at the end:")
    llist.insert_at_end(20)
    llist.insert_at_end(25)
    llist.display()

    print("\nInserting after value 10:")
    llist.insert_after_value(10, 15)
    llist.display()

    print("\nDeleting value 20:")
    llist.delete_by_value(20)
    llist.display()

    print("\nDeleting value 5:")
    llist.delete_by_value(5)
    llist.display()

    print("\nDeleting value 100 (non-existent):")
    llist.delete_by_value(100)
    llist.display()


