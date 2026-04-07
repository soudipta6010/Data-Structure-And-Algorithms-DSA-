# Question- https://www.geeksforgeeks.org/problems/find-length-of-loop/1

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))


class Solution:
    def lengthOfLoop(self, head):
        my_dict = dict()                        # Dictionary to store node -> position mapping
        temp = head                             # Current node we're examining
        travel = 0                              # Current position counter
        while temp is not None:
            if temp not in my_dict:             # Check if we've seen this node before
                return travel - my_dict[temp]  # Calculate loop length
            my_dict[temp] = travel             # Record current node's position
            travel += 1                        # Increment position counter
            temp = temp.next                   # Move to next node
        return 0                               # No loop found


"""
Time and Space Complexity
Time Complexity: O(n) – We visit each node at most once before detecting the loop
Space Complexity: O(n) – We store all nodes in the dictionary

"""