matrix = [
    [ 1,  2, -1, -4, -20],
    [-8, -3,  4,  2,   1],
    [ 3,  8, 10,  1,   3],
    [-4, -1,  1,  7,  -6]
]
def kadane(arr):
    curr = arr[0]
    best = arr[0]
    for i in range(1,len(arr)):
        curr = max(arr[i], arr[i] + curr)
        best = max(best, curr)
    return best
def max_sum_matrix(matrix):
    rows = len(matrix)
    col = len(matrix[0])
    max_sum = float('-inf')

    for top in range(rows):
        temp = [0]*col

        for bottom in range(top, rows):
            