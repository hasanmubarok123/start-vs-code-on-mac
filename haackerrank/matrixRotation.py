def matrixRotation(matrix, r):
    for time in range(r):
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix)):
                if i == len(matrix)-1 and j != len(matrix[i])-1:
                    matrix[j][i] = matrix[j+1][i]
            for j in range(len(matrix[i])-1, -1, -1):
                if i == len(matrix)-1 and j != 0:
                    matrix[i][j] = matrix[i][j-1]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])-1, -1, -1):
                if i == 0 and j != 0:
                    matrix[j][i] = matrix[j-1][i]
            for j in range(len(matrix[i])):
                if i == 0 and j != len(matrix[i])-1:
                    matrix[i][j] = matrix[i][j+1]


                print(matrix[i][j], end=" ")
            print()
        print()



matrixRotation([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]], 2)
