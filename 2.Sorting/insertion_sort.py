nums = [10, 8, 15, 3, 1, 6, 5]

def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

        print(nums) # To understand the iteration and changeing of the position of the elements
    return nums


print(f"Final amswer {insertion_sort(nums)}")