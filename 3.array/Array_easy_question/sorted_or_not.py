nums = [8, 6, 7, 2, 1, 5, 3]
# nums = [1,2,3,4,5,6]

def sorted_or_not(nums):
    n = len(nums)
    for i in range(0,n-2):
        if nums[i]>nums[i+1]:
            return False
    return True

print(sorted_or_not(nums))
