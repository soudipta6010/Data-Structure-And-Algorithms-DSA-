arr = [-1, 0, 1, 2, -1, -4]


def three_sum(arr):
    n = len(arr)
    result = set()
    for i in range(0, n):
        my_set = set()
        for j in range(i + 1, n):
            third = -(arr[i] + arr[j])
            if third in my_set:
                temp = [arr[i], arr[j], third]
                temp.sort()
                result.add(tuple(temp))
            my_set.add(arr[j])
    return [list(ans) for ans in result]


x = three_sum(arr)
print(x)

