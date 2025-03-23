"""
You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.
Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.
Question- https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1
"""

nums = [16, 17, 17, 4, 3, 5, 2]


def array_leaders(nums):
    n = len(nums)
    result = []
    maxi = float("-inf")
    for i in range(n - 1, -1, -1):
        # e = max(nums[i], maxi)
        if nums[i] > maxi:
            e = nums[i]
        else:
            e = maxi
        if e > maxi:
            result.append(e)
            maxi = e
    result.reverse()
    return result


print(f"Orginal Array: {nums}")
print(f"Array leaders: {array_leaders(nums)}")


"""
Another Solution

def leaders(arr):
    j = []
    m = arr[-1]
    j.append(m)
    for i in range(1, len(arr) + 1):
        if m <= arr[-i]:
            m = arr[-i]
            j.append(m)
            # print(m,arr[-i])
    return j[::-1][:-1]


arr = [16, 17, 4, 3, 5, 2]

print(leaders(arr))


"""
