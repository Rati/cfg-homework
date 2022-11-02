"""
SEARCH IN MATRIX
--------

You are give a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""


# Here, are two different approach for the above problem
# linear search & Binary search
# since each row in the matrix is SORTED(utilizing this property of matrix) then Binary search should perform better
# let's assume we have a matrix of 1000 size the for linear search the best case complexity is O(1)
# and worst case complexity is O(1000) if the number to be search at last position


# linear search
def search_in_matrix_linear(matrix, target):
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            if matrix[m][n] == target:
                return [m, n]
    else:
       return [-1, -1]


matrix = [
[1, 4, 7, 12, 15, 1000],
[2, 5, 19, 31, 32, 1001],
[3, 8, 24, 33, 35, 1002],
[40, 41, 42, 44, 45, 1003],
[99, 100, 103, 106, 128, 1004]
]

target = 44

print(search_in_matrix_linear(matrix, target))

# If assuming the similar situation of a matrix of 1000 size the for binary search
# the best case complexity is O(1) and worst case complexity is O(log21000) = O(9.965)
# if the number to be search at last position


# Binary search
def search_in_matrix_binary(matrix, target):
    column = 0
    row = len(matrix[column]) - 1
    while (column < len(matrix)) and row >= 0:
        if matrix[column][row] == target:
            return [column, row]
        if matrix[column][row] < target:
            column += 1

        else:
            row -= 1
    return [-1, -1]

matrix = [
[1, 4, 7, 12, 15, 1000],
[2, 5, 19, 31, 32, 1001],
[3, 8, 24, 33, 35, 1002],
[40, 41, 42, 44, 45, 1003],
[99, 100, 103, 106, 128, 1004]
]

target = 44


print(search_in_matrix_binary(matrix, target))