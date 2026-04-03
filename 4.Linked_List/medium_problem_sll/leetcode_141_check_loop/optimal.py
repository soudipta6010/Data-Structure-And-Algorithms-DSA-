# Linked List Cycle | Leetcode 141 | Floyd’s Cycle Detection
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head  # Slow pointer (tortoise) - moves 1 step
        fast = head  # Fast pointer (hare) - moves 2 steps

        while fast is not None and fast.next is not None:
            slow = slow.next  # Move slow pointer 1 step
            fast = fast.next.next  # Move fast pointer 2 steps

            if slow == fast:  # Pointers met - cycle detected!
                return True

        return False  # Fast reached end - no cycle


# TC-> O(N), SC->O(1)
