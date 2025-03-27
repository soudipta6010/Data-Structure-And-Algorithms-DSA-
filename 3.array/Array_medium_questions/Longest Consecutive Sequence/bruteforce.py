"""
Leet code- 128. Longest Consecutive Sequence

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
Therefore its length is 4.
"""
nums = [100, 4, 200, 1, 3, 2]


def longest_consecutive_sequence(nums):
    n = len(nums)
    max_count = float("-inf")
    for i in range(0, n):
        num = nums[i]
        count = 1
        while num + 1 in nums:
            count += 1
            num += 1
        max_count = max(max_count, count)
    return max_count


print(longest_consecutive_sequence(nums))
