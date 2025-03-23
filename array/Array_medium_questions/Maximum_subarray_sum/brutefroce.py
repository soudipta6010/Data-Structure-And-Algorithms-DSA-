# Maximum SubArray Sum
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def maximum_subarray_sum(nums):
    n = len(nums)
    maxi = float("-inf")
    start = end = 0

    for i in range(0, n):
        total = 0
        temp_start = i
        for j in range(i, n):
            total = total + nums[j]
            # maxi = max(maxi, total)
            if total > maxi:
                maxi = total
                start = temp_start
                end = j
    return maxi, start, end


max_sum, start_idx, end_idx = maximum_subarray_sum(nums)

print(f"Before: {nums}")
print(f"Maximum Subarray Sum: {max_sum}")
print(f"Start Index: {start_idx}, End Index: {end_idx}")
print(f"Subarray: {nums[start_idx:end_idx+1]}")
# print(f"After: {maximun_subarray_sum(nums)}")
