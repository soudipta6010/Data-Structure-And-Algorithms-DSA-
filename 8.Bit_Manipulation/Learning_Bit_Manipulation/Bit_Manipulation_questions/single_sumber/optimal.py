# leetcode- 136 single number - optimal solution


def singleNumber(arr):
    result = 0
    for num in arr:
        result = result ^ num
    return result

arr = [4,2,1,2,1]
x = singleNumber(arr)
print(f"Single number in the given array is {x}")