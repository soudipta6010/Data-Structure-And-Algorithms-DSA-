nums = [100, 4, 200, 1, 3, 2]


def longest_consecutive_sequence(nums):
    nums.sort()
    n = len(nums)
    last_smaller = "-inf"
    count = 0
    longest = 0
    for i in range(0, n):
        num = nums[i]
        if num - 1 == last_smaller:
            count += 1
            last_smaller = num
        elif num != last_smaller:
            count = 1
            last_smaller = num
        longest = max(longest, count)
    return longest


print(longest_consecutive_sequence(nums))
