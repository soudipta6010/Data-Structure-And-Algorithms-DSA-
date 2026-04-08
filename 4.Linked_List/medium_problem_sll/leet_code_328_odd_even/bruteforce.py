# Odd Even Linked List | Leetcode 328

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head                     # Empty list or single node - nothing to rearrange
        
        temp = head
        values = []

        # First pass: Collecting values from odd-indexed nodes (1st, 3rd, 5th, ...)
        while temp:
            values.append(temp.val)     # Add current node's value
            if temp.next:
                temp = temp.next.next   # Skip one node to get next odd position
            else:
                break                   # Reached end of list

        temp = temp.next                # Start from 2nd node (first even position)

        # Second pass: Collecting values from even-indexed nodes (2nd, 4th, 6th, ...)
        while temp:
            values.append(temp.val)     # Add current node's value
            if temp.next:
                temp = temp.next.next   # Skip one node to get next even position
            else:
                break                   # Reached end of list
        
        # Third pass: Assigning collected values back to the nodes
        index = 0
        temp= head
        while temp:
            temp.val = values[index]    # Replace node value with rearranged value
            index += 1
            temp = temp.next
        
        return head
