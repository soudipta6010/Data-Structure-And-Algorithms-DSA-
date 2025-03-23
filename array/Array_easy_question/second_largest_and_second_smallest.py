nums = [8, 6, 7, 2, 1, 5, 3]
def find_second_largest_smallest(a):
    largest = float("-inf")
    s_largest = float("-inf")
    smallest = float("inf")
    s_smallest = float("inf")

    for x in a:  # Use 'a' (the input array) consistently
        if x > largest:
            s_largest = largest
            largest = x
        elif x > s_largest and x != largest:
            s_largest = x

    for x in a:  # Use 'a' consistently
        if x < smallest:
            s_smallest = smallest
            smallest = x
        elif x < s_smallest and x != smallest:
            s_smallest = x

    return [s_largest, s_smallest]


print(find_second_largest_smallest(nums))
