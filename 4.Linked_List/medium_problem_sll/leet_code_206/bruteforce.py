class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        stack = []

        # First pass: Store all values in stack
        while temp is not None:
            stack = stack.append(temp.val)         # Push current node's value to stack
            temp = temp.next                       

        temp = head                                # Reset temp to head for second pass

        # Second pass: Pop values from stack and update nodes
        while temp is not None:
            temp.val = stack.pop()                 # Replace current value with stack's top
            temp = temp.next
        return head



# TC-> O(2N)~O(N), SC->O(N)
