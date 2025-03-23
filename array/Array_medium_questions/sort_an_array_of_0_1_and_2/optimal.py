# SORT AN ARRAY OF 0'S, 1'S, AND 2'S
"""
Sort Using one pass solution- Dutch National Flag method
"""
nums = [1, 0, 0, 2, 1, 2, 2, 0, 1, 2]


def sort_0s_1s_2s(nums):
    n = len(nums)
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


print(f"Before {nums}")
print(f"After {sort_0s_1s_2s(nums)}")
