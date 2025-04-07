# Leetcode-73 Set Matrix Zeroes 
"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""

matrix = [
    [7, 9, 2, 3], 
    [20, 8, 0, 10], 
    [29, 0, -10, 5], 
    [4, 14, 6, 7]
]


def set_zeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    row_track = [0 for i in range(rows)]
    col_track = [0 for i in range(cols)]

    # Another way without using list comprehension
    # row_track = [0]*(rows-1)
    # col_track = [0]*(rows-1)

    for i in range(0, rows):
        for j in range(0, cols):
            if matrix[i][j] == 0:
                row_track[i] = -1
                col_track[j] = -1

    for i in range(0, rows):
        for j in range(0, cols):
            if row_track[i] == -1 or col_track[j] == -1:
                matrix[i][j] = 0


set_zeros(matrix)
row=len(matrix)
col=len(matrix[0])
for i in range(0,row):
    for j in range(0,col):
        print(matrix[i][j], end=" ")
    print()
