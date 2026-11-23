# Generate all subsequences

def func(index, subset, nums, result):

    # Base case
    if index >= len(nums):
        result.append(subset.copy())
        return

    # Pick the current element
    subset.append(nums[index])
    func(index + 1, subset, nums, result)

    # Backtrack
    subset.pop()

    # Do not pick the current element
    func(index + 1, subset, nums, result)


def subsets(nums: list[int]) -> list[list[int]]:
    result = []
    func(0, [], nums, result)
    return result


nums = [5, 9, 7]
x = subsets(nums)

print(f"All subsequences are: {x}")