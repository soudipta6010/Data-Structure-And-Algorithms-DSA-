# Moore's voting Algorithm

nums = [1, 3, 1, 2, 7, ]


def majority_element(nums):
    n = len(nums)
    element = None
    count = 0

    for i in range(0, n):
        if count == 0:
            element = nums[i]
            count += 1
        elif nums[i] == element:
            count += 1
        else:
            count -= 1
    # return element

    count = 0
    for i in range(0,n):
        if nums[i]==element:
            count +=1
    if count > n//2:
        return element
    return -1

print(f"{majority_element(nums)}")
