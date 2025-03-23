nums = [55, 32, -97, 99, 3, 67]

def find_Largest(nums):
    n= len(nums)
    largest = float("-inf")

    for i in range (0,n):
        largest = max(largest,nums[i])
    return largest

print(find_Largest(nums))