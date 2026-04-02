class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # To append anything at end, TC-> O(N), SC-> O(1)
    def append(self, val):
        new_node = Node(val)

        # If linked list is empty
        if self.head == None:
            self.head = new_node

        else:
            # If Linked list is not empty
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    # Traversing a singly linked list
    def traverse(self):

        # If linked list is empty
        if self.head == None:
            print("Singly Linked List is empty")

        else:
            # If Linked list is not empty
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    # Insert at any specfic position, TC->O(N), SC->O(1)
    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while count is not None:
                prev_node = current
                current = current.next
                count += 1
            prev_node.next = new_node
            new_node.next = current

    # Deleting a node from linked list
    def delete(self, val):
        temp=self.head
        if temp.next is not None:
            if temp.val==val:
                self.head=temp.next
                return
            else:
                found=False
                prev=None
                while temp is not None:
                    if temp.val==val:
                        found=True
                        break
                    prev=temp
                    temp=temp.next
                
                if found:
                    prev.next=temp.next
                    return
                else:
                    print("Node not found")



sll = SinglyLinkedList()
sll.append(10)
sll.append(30)
sll.append(5)
sll.append(40)
sll.traverse()
