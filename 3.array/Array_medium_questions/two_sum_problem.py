nums = [5, 9, 1, 2, 4, 15, 6, 3]  # target = 13
target = 13


# BRUTE FORCE
"""
def two_sum(nums,target):
    n = len(nums)
    for i in range(0,n-1):
        for j in range(1,n):
            if nums[i] +nums[j] == target:
                return [i, j]
            
print(f"{two_sum(nums,target)}")

"""

# OPTIMAL SOLUTION


def two_sum(nums, target):
    n = len(nums)
    hash_map = {}

    for i in range(0, n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
        hash_map[nums[i]] = i


print(f"{two_sum(nums,target)}")
