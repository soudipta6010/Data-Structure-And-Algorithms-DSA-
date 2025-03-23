"""
You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.
Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.
Question- https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1
"""

nums = [16, 17, 4, 3, 5, 2]

def leaders(nums):
    result = []
    n = len(nums)
    for i in range(0, n):
        e = nums[i]
        is_leader = True
        for j in range(i + 1, n):
            if nums[j] > e:
                is_leader = False
                break
        if is_leader:
            result.append(e)
    return result


print(leaders(nums))
