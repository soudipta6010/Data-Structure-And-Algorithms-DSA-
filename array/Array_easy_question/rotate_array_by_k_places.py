# Rotate an array by K places
nums = [3, 9, 5, 6, 7, 2, 10, 9]
k = 9

# Brute Froce Solution

"""
print(f"Before rotation {nums}")
n = len(nums)
rotation = k % n
for i in range(0, rotation):    #Time complexity =O(r*n), Space Complexity = O(1)
    e = nums.pop()
    nums.insert(0, e)
print(f"After rotation {nums}")

"""


# Better Solution

"""
print(f"Before Rotation {nums}")
n = len(nums)
rotation = k % n
nums[:] = nums[n-k :] + nums[0:n-k]  #Time complexity =O(n), Space Complexity = O(1)
print(f"After Rotation {nums}")
"""

# Optimal Solution ()


def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


n = len(nums)
k = k % n
print(f"Before Rotation {nums}")

reverse(nums, n - k, n - 1)  # Reverse the last k elements
reverse(nums, 0, n - k - 1)  # Reverse the remaining elements
print(f"After rotation {(reverse(nums,0,n-1))}")  # Reverse Whole array

# Time complexity = O(N), Space Complexity = O(1)
