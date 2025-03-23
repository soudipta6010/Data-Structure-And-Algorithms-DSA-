# considering the array is sorted

nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]
"""
#Brute force
def remove_dupicate(nums):
    n= len(nums)
    freq_map ={}
    for i in range(0,n):
        freq_map[nums[i]]=0 #explain this line just
    j=0
    for k in freq_map:
        nums[j]=k
        j +=1
    return j

x=remove_dupicate(nums)
print(nums)
print(x)
"""

#Optimal
def remove_dupicate(nums):
    n= len(nums)
    if n==1:
        return 1
    i=0
    j=i+1
    while j<n:
        if nums[j]!= nums[i]:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
        j+=1
    return i+1 # i gives the index and +1 with it give the total no. f unique elements

x= remove_dupicate(nums)
print(f"Number of unique element present in the array : {x}")
print(nums)
