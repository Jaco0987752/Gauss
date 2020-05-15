import numpy as np

def Add(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        print("can't add arrays of different shape")
    else:
        result =np.zeros(matrix1.shape)
        for r in range(matrix1.shape[0]):
            for c in range(matrix1.shape[0]):
                result[r][c] = matrix1[r][c] + matrix2[r][c]
        return result

def Multiply(matrix1, matrix2):
    print(matrix1.shape)
    print(matrix2.shape)

    if matrix1.shape[1] != matrix2.shape[0]:
        print("can't add arrays of different shape")
    else:
        result =np.zeros((matrix1.shape[0], matrix2.shape[1]))
        for c in range(matrix2.shape[1]):
            for b in range(matrix1.shape[0]):
                sum = 0
                for a in range(matrix1.shape[1]):
                    sum += matrix1[b][a] * matrix2[a][c]
                result[b][c] = sum
        return result

matrix1 = np.array( [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype = np.float32)
print(matrix1)
matrix2 = np.array( [ [1, 2], [3, 4], [5, 6],  [7, 8] ], dtype = np.float32)
print(matrix2)
result = Multiply(matrix1, matrix2)
print(result)