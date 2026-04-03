# Linked List Cycle | Leetcode 141 | Floyd’s Cycle Detection

class Solution:
    def checkCycle(self, head: Optional[ListNode])->bool:
        temp=head                       # Current node we're examining
        node_set=set()                  # Set to store visited nodes
        while temp is not None:
            if temp in node_set:        # Check if we've seen this node before
                return True             # Found a cycle!
            node_set.add(temp)          # Remember this node for future
            temp=temp.next              # Move to the next node
        return False                    # Reached end, no cycle found
    
# has_cycle = Solution()
# has_cycle.checkCycle(head)



# TC-> O(N), SC->O(N)
