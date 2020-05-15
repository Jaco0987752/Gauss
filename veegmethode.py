# this code is written by Jaco de Jong.
import numpy as np

A = np.array([
    [2, -3, 5],
    [4, 5, -4],
    [6, 3, -2]
], dtype=float)

B = np.array([[11],
              [2],
              [6]], dtype=float)

def gauss(A,B):
    
    joined = np.concatenate((A,B), axis=1)
    print("joined")
    print(joined)

    swep(joined)
    print("swepped")
    print(joined)

    swap(joined)
    print("swapped")
    print(joined)

    swep(joined, offset=1)
    print("swepped again")
    print(joined)

    swap(joined)
    print("swapped back")
    print(joined)

    divide(joined)
    print("divided")
    print(joined)

    joined = np.around(joined,2)
    print("rounded")
    print(joined)
    
    columns = joined.shape[1]
    rows = joined.shape[0]
    result = [] 
    for r in range(rows):
            result.append(joined[r][columns-1])
    return result

        


def swep(matrix, offset = 0):
    for b in range( matrix.shape[0]):
        c = b-1
        if c<0: c = 0 
        if b < matrix.shape[0]-1: b = b+1
        factor = matrix[b][c+offset] / matrix[c][c+offset]
        print(factor)
        for a in range(matrix.shape[1]):
            matrix[b][a] = matrix[b][a] - factor * matrix[c][a]

def swap(matrix):
    toSwap = np.array(matrix, copy=True)
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    for r in range(rows):
        for c in range(columns):
            matrix[rows-1-r][columns-1-c ] = toSwap[r][c]

def divide(matrix):
    toSwap = np.array(matrix, copy=True)
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    for r in range(rows):
        sum = 0
        for c in range(columns -1):
            sum += matrix[r][c]
        matrix[r][columns-1] = matrix[r][columns-1]/sum

            

result = gauss(A,B)
print("result")
print(result)