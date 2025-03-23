nums = [55, 32, -97, 99, 3, 67]

# Brute Froce
"""
n = len(nums)
nums.sort()
print(nums[-2])  # OR print(nums[n-2])

"""

# Best Solution
"""
def second_largest(nums):
    n = len(nums)
    largest = float("-inf")
    s_largest = float("-inf")

    for i in range(0, n):
        largest = max(largest, nums[i])
    for i in range(0, n):
        if nums[i] > s_largest and nums[i] != largest:
            s_largest = nums[i]
    print(s_largest)

"""

#OPTIMAL SOLUTION
n = len(nums)
largest = float("-inf")
s_largest = float("-inf")
for i in range(0,n):
    if nums[i]>largest:
        s_largest = largest
        largest= nums[i]
    elif nums[i]>s_largest and nums[i]!=largest:
        s_largest=nums[i]
print(s_largest)