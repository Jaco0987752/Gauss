import numpy as np

A = np.array([
    [2, -3, 5],
    [4, 5, -4],
    [6, 3, -2]
])

B = np.array([[11],
              [2],
              [6]])

def swep(A,B):
    
    joined = np.concatenate((A,B), axis=1)
    print("joined")
    print(joined)

    c = 0
    for b in range( joined.shape[0]):
        c = b-1
        if c<0: c = 0 
        if b < joined.shape[0]-1: b = b+1
        print(b,c)
        factor = joined[b][c] / joined[c][c]
        print(factor)
        for a in range(joined.shape[1]):
            joined[b][a] = joined[b][a] - factor * joined[c][a]
        print("joined after b= " + str(b) + "c=" + str(c))
        print(joined)


    # factor = joined[2][0] / joined[0][0]
    # for b in range(joined.shape[1]):
    #     print(str(joined[2][a]) + " - " + str(factor) + " * " + str(joined[0][a])) 
    #     joined[2][b] = joined[2][b] - factor * joined[0][b]


    #A[2][0] = A[2][0] - A[2][0] / A[0][0] * A[0][0]     

    #A[2][1] = A[2][1] - A[2][1] / A[1][1] * A[1][1]

    #A[2][2] = A[2][2] - A[2][2] / A[1][2] * A[1][2]

swep(A,B)