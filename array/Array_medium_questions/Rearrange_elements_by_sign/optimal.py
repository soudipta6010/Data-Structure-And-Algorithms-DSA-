#Question link- https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

nums = [3, -2, 1, -5, 2, -4]  # result = [3, -2, 1, -5, 2, -4]


def rearrange_elements_by_sign(nums):
    n = len(nums)
    result = [0] * n
    pos_index=0
    neg_index=1
    for i in range(0,n):
        if nums[i]>=0:
            result[pos_index]=nums[i]
            pos_index+=2
        else:
            result[neg_index]=nums[i]
            neg_index+=2
    return result
print(f"Before: {nums}")
print(f"After: {rearrange_elements_by_sign(nums)}")