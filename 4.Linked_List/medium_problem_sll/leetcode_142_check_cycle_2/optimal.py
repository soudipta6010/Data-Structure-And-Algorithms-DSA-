# Linked List Cycle II | Leetcode 142 |


class Solution:
    def detectCycle(self, head):
        slow = head                                 # Slow pointer (tortoise)
        fast = head                                 # Fast pointer (hare)

        # Phase 1: Detect if cycle exists
        while fast and fast.next is not None:
            slow = slow.next                         # Move slow pointer 1 step
            fast = fast.next.next                    # Move fast pointer 2 steps

            if slow == fast:                         # Cycle detected!
                # Phase 2: Find cycle start
                while slow != fast:                 # Reset slow to head
                    slow = slow.next                # Move both pointers 1 step each
                    fast = fast.next
                return slow                         # They meet at cycle start
        return None                                 # No cycle found
