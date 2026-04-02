# Tortoise hare approach to find the middle of a linked list
# leetcode question- 786


class Solution:
    """
    # Brute Force Solution
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head
    # First pass: count the total number of nodes
        while temp:
            n += 1    # increment counter
            temp = temp.next  # move to next node

        temp = head
    # Second pass: move to the middle position
        for i in range(0, n // 2):
            temp = temp.next  # move forward n//2 steps
        return temp   # return the middle node

    # TC-> O(N+N/2), Sc-> o(1)

    """

    # OPTIMAL SOLUTION -> Tortoise and Hare method (Two Pointers / Fast and Slow)
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head                             # slow pointer starts at head
        fast = head                             # slow pointer starts at head
        while fast and fast.next :
            slow = slow.next                    # slow moves 1 step
            fast=fast.next.next                 # fast moves 2 steps
        return slow                             # slow is now at the middle
