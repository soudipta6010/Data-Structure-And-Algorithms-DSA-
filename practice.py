nums = [4,8,5,3,1,4,7,8]
n = len(nums)
temp = nums[n-1]
for i in range(n-2, -1,-1):
    nums[i+1]=nums[i]
nums[0]=temp

print(nums)