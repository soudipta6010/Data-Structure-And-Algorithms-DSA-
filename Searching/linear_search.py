def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [2, 4, 6, 8, 1, 10, 15]
target = int(input("Enter any number: "))
result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element not found")
