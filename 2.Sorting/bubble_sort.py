nums = [4, 8, 7, 1, 3, 9, 10, 5, 6, 15, 2]


# Worst case / Average case solution(TC-> O(n^2), SC -> O(1))
def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 2, 0, -1):
        for j in range(0, i + 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


print(f"Before sorting: {nums}")
print(bubble_sort(nums))


# Best case solution(TC-> O(n), SC -> O(1))
def bubble_sort_2(nums):
    n = len(nums)
    for i in range(n - 2, 0, -1):
        is_swap = False
        for j in range(0, i + 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swap = True
        if is_swap == False:
            break
    return nums


print(f"Before sorting: {nums}")
print(bubble_sort_2(nums))
