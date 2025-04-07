matrix = [
    [7, 9, 2, 3],
    [20, 8, 0, 10],
    [29, 0, -10, 5],
    [4, 14, 6, 7]
]

def mark_infinity(matrix, row, col):
    r = len(matrix)
    c =len(matrix[0])

    for i in range(0, r):
        if matrix[i][col] != 0:
            matrix[i][col]=float("inf")

    for j in range(0,c):
        if matrix[row][j] != 0:
            matrix[row][j]=float("inf")
    

def set_zeros(matrix):
    row = len(matrix)
    col=len(matrix[0])
    for i in range(0, row):
        for j in range(0, col):
            if matrix[i][j] == 0:
                mark_infinity(matrix, i, j)

    for i in range(0, row):
        for j in range(0, col):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0
        print()

# Run the function
set_zeros(matrix)

# Print the matrix - method 1
for row in matrix:
    print(row)

# Print the matrix - method 2
row=len(matrix)
col=len(matrix[0])
for i in range(0,row):
    for j in range(0,col):
        print(matrix[i][j], end=" ")
    print()