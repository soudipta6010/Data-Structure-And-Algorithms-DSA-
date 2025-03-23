nums = [4, 8, 7, 1, 3, 9, 10, 5, 6, 15]

# Sorting in ascending order
def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i],nums[min_idx] = nums[min_idx], nums[i]
    return nums
print("Sortinng in ascending order")
x = selection_sort(nums)
print (x)


# Sorting in decending order
def selection_sort_decending(nums):
    n = len(nums)
    for i in range(0, n):
        max_idx = i
        for j in range(i + 1, n):
            if nums[j] > nums[max_idx]:
                max_idx = j
        nums[i],nums[max_idx] = nums[max_idx], nums[i]
    return nums
print("Sorting in decending order")
print(f"{selection_sort_decending(nums)}")