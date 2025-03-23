nums = [3, 1, -2, -5, 2, -4]  # result = [3, -2, 1, -5, 2, -4]


def rearrange_elements_by_sign(nums):
    n = len(nums)
    pos = []
    neg = []
    for i in range(n):
        if nums[i] >= 0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])

    for i in range(0, len(pos)):
        nums[2 * i] = pos[i]
        nums[(2 * i) + 1] = neg[i]
    return nums


print(f"Before: {nums}")
print(f"After: {rearrange_elements_by_sign(nums)}")
