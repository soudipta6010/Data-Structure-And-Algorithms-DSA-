# leetcode- 136 single number - brute force solution

def singleNumber(arr):
    hash_map ={}
    for num in arr:
        hash_map [num] = hash_map.get(num, 0) + 1
    for key in hash_map:
        if hash_map[key] == 1:
            return key

arr = [4,2,1,2,1]

result = singleNumber(arr)
print(f"Single number in the given array is {result}")