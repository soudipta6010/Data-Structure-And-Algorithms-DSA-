nums = [0, 1, 0, 3, 12]


def moveZeroes(nums) -> None:
    """
    modify nums in-place instead.
    """
    if len(nums) == 1:
        return
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            break
        i += 1
    if i == len(nums):
        return
    j = i + 1
    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    return nums


print(f"Before changes {nums}")
print(f"After changes {moveZeroes(nums)}")
