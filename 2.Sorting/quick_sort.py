nums = [9, 6, 7, 2, 10, 1, 16, 55, 14]


def partition(nums, low, high):
    i = low
    j = high
    pivot = nums[low]
    while i < j: #explain me this line why i< j in the loop
        while nums[i] <= pivot and i <= high - 1:
            i += 1
        while nums[j] >= pivot and j >= low + 1:
            j -= 1
        if i < j: # also explain before swapping why I need to check for i<j
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j


def quick_sort(nums, low, high):
    if low < high:
        p_idx = partition(nums, low, high)
        quick_sort(nums, low, p_idx - 1)
        quick_sort(nums, p_idx + 1, high)


n = len(nums)
low = 0
high = n - 1
quick_sort(nums, low, high)
print(nums)
