# Majority Element (Elements appears > n/2 times)

nums = [1, 3, 1, 2, 7, 3, 3, 3, 3]


def majority_element(nums):
    n = len(nums)
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1
        if count > n // 2:
            return nums[i]
    return -1


print(f"{majority_element(nums)}")
