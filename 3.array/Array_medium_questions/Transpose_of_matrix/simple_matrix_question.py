nums = [
    [5, 1, 8],
    [7, 6, 3],
    [2, 1, 9]
]
# Printing the upper diagonal of the matrix
print("Printing the upper diagonal of the matrix")
rows = len(nums)
cols = len(nums[0])

for i in range(0,rows):
    for j in range(0,cols):
        if j>=i:
            print(nums[i][j], end=" ")
        else:
            print("*",end=" ")
    print()


# Printing the lower diagonal of the matrix
print("Printing the lower diagonal of the matrix:")
for j in range(0,cols):
    for i in range(0,rows):
        if j >= i:
            print(nums[j][i], end=" ")
        else:
            print("*",end = " ")
    print()

# Printing the diagonals only
print("Printing the diagonals only")
for j in range(0,cols):
    for i in range(0,rows):
        if j == i:
            print(nums[j][i], end=" ")
        else:
            print("*", end=" ")
    print()