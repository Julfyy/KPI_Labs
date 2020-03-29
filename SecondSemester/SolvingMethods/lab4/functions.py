import numpy as np


    
def print_one_matr(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print("%0.6f" % a[i][j], end = "\t")
        print()
    print()
    
def frobeus_normalization(A):
    m = len(A)

    
    M = np.array([np.eye(m) for i in range(m-1)])
    M_r = np.array([np.eye(m) for i in range(m-1)])
    S = np.eye(m)
    
    for i in reversed(range(m-1)): #  i = 2,1,0
        for j in range(m):
            if j == i:
                M[i][i][j] = 1 / A[i+1][i]
            else:
                M[i][i][j] = -A[i+1][j] / A[i+1][i]
                
            M_r[i][i][j] = A[i+1][j]
        
        A = M_r[i].dot(A).dot(M[i])
        
        S = S.dot(M[i])
    
    return A, S
            
            



