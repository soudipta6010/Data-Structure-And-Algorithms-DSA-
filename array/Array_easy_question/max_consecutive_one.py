nums = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]


def count_consecutive_ones(nums):
    max_count = 0
    count = 0
    n = len(nums)

    for i in range(0, n):
        if nums[i] == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    max_count = max(max_count, count)
    return max_count


print(f"{count_consecutive_ones(nums)}")
