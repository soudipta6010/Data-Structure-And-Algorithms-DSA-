nums = [1, 3, 1, 2, 7, 3, 3, 3, 3]


def majority_element(nums):
    n = len(nums)
    my_dict = {}
    # for i in range(0, n):
    #     my_dict[nums[i]] = my_dict.get(nums[i], 0) + 1

    for num in nums:
        my_dict[num] = my_dict.get(num, 0) + 1

    for num, freq in my_dict.items():
        if freq > n // 2:
            return num
    return -1


print(f"{majority_element(nums)}")
