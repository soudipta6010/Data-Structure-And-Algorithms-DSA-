nums = [-1, 0, 1, 2, -1, -4]


def three_sum(nums):
    nums.sort()
    ans = []
    n = len(nums)
    for i in range(0, n):
        if i != 0 and nums[i] == nums[i - 1]:
            continue
        # Moving the 2nd pointer
        j = i + 1
        k = n - 1
        while j < k:
            total_sum = nums[i] + nums[j] + nums[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                temp = [nums[i], nums[j], nums[k]]
                ans.append(temp)
                j += 1
                k -= 1

                # Skips the duplicates if occured
                while j<k and nums[j]==nums[j-1]:
                    j += 1
                while j<k and nums[k]==nums[j+1]:
                    k -=1
    return ans
    
x = three_sum(nums)
print(x)
