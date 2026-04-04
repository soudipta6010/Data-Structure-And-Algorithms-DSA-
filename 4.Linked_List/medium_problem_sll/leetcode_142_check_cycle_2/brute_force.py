# Linked List Cycle II | Leetcode 142 |
class Solution:
    def detectCycle(self, head):
        temp = head                 # Current node we're examining
        my_set = set()              # Set to store visited nodes

        while temp is not None:
            if temp in my_set:      # Check if we've seen this node before
                return temp         # This is where the cycle starts!
            my_set.add(temp)        # Remember this node for future
            temp = temp.next        # Move to the next node

        return None                 # Reached end, no cycle found
    


"""
Time Complexity: O(n) – We visit each node at most once before detecting the cycle start
Space Complexity: O(n) – In worst case, we store all nodes in the set
"""