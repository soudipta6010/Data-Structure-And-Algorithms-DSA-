# SORT AN ARRAY OF 0'S, 1'S, AND 2'S

nums = [1, 0, 0, 2, 1, 2, 2, 0, 1, 2]

def sort_0s_1s_2s(nums):
    n = len(nums)
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for i in range(0, n):
        if nums[i] == 0:
            count_0 += 1

        if nums[i] == 1:
            count_1 += 1

        if nums[i] == 2:
            count_2 += 1

    for i in range(0, count_0 + 1):
        nums[i] = 0
    for i in range(count_0, count_0 + count_1):
        nums[i] = 1
    for i in range(count_0+count_1, n):
        nums[i]=2
    return nums

print(f"Before: {nums}")
print(f"After: {sort_0s_1s_2s(nums)}")
