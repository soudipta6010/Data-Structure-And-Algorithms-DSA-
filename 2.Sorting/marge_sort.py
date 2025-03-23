def merge_array(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)

    while i < n and j < m:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < n:
        result.append(left[i])
        i += 1
    if j < m:
        result.append(right[j])
        j += 1
    return result


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_arr = nums[:mid]
    right_arr = nums[mid:]

    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return merge_array(left,right)


nums=[4,3,8,12,9,10,7,1,6,2,1]
print(f"{merge_sort(nums)}")
