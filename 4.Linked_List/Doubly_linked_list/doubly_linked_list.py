class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert At head [TC -> O(1), SC-> O(1)]
    def insert_at_head(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node  # First node becomes head
        else:
            new_node.next = self.head  # New node points to current head
            self.head.prev = new_node  # Current head's prev points to new node
            self.head = new_node  # Update head to new node

    #  Insert at End (Append), [TC -> O(N), SC-> O(1)]
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next  # Find the last node
            current.next = new_node  # Connect last node to new node
            new_node.prev = current  # Connect new node back to last node

    # Insert at any Position of doubly linked List, [TC -> O(N), SC-> O(1)]
    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if current is None:
            print("Position out of bounds")
            return
        
        new_node.next = current.next             # Connect new node to next node
        new_node.prev = current                  # Connect new node to current node    
        if current.next:
            current.next.prev = new_node         # Update next node's prev pointer
        current.next = new_node                  # Connect current node to new node   

"""
Task -

traversal()
delete_head()
delete_last()
delete_in_between()
"""