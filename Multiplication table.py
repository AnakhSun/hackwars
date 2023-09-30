def multiplication_table(size):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for n in range(1, size+1):
        matrix[0][n-1] = n
        matrix[n-1][0] = n
    for i in range(1, size):
        for j in range(1, size):
            matrix[i][j] = matrix[i][0] * matrix[0][j]
    return matrix


print(multiplication_table(3))