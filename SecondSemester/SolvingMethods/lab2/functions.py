import copy
import numpy as np


def print_matr(a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print("%0.3f" % a[i][j], end = "\t")
        print("| %0.3f" % b[i])
    print("\n")
 

def gauss(arg_a, arg_b):
    a = copy.deepcopy(arg_a)
    b = copy.deepcopy(arg_b)
    
    #Initialize triangle matrix
    triangle_matr = [[a[n][m] for m in range(len(a[0]))] for n in range(len(a))] 
    
    #Initialize x matrix
    x_matr = [0 for i in range(len(a))]
    
    while(len(a) > 0):
        n = len(a)
        m = len(a[0])
        #Finding a_main the max element in the whole matrix
        a_main = a[0][0] #Suppose that a_main is the element [0][0]
        main_line = 0
        main_column = 0
        

        for i in range(n):
            for j in range(m):
                if a[i][j] > a_main:
                    a_main = a[i][j]
                    main_line = i
                    main_column = j
    
        
        if(len(a) > 1):
            #Finding all koeficients m for not main lines
            m_arr = [1 for x in range(n)]
            # m_arr contain a 0 for the main line
            for i in range(n):
                if i != main_line:
                    m_arr[i] = a[i][main_column] / a_main
            
            
            #First step to make zeros in main_column in not main lines
            for i in range(n):
                if i != main_line:
                    for j in range(m):
                        a[i][j] -= m_arr[i] * a[main_line][j]
                    b[i] -= m_arr[i] * b[main_line]
        
        #Remove main line and column and replace it to another array
        triangle_matr[main_line] = a[main_line]        
        a = np.delete(a, (main_line), axis = 0)
        
        print("Step #{}".format(len(triangle_matr) - n + 1))
        print_matr(triangle_matr, b)
    
    #Sort triangle matrix to triangle look
    if triangle_matr[0][0] == 0:
        for i in range(len(triangle_matr)):
            last = len(triangle_matr) - i - 1
            if i > last:
                break
            triangle_matr[i], triangle_matr[last] = triangle_matr[last], triangle_matr[i]
            b[i], b[last] = b[last], b[i]
            
    
    print("Step #{}".format(len(triangle_matr) - n + 2))
    print_matr(triangle_matr, b)
    #Find x
    for k in range(len(triangle_matr)):
        for i in range(len(triangle_matr)):
            for j in range(len(triangle_matr[0])):
                if j != i and triangle_matr[i][i] != 0:
                    x_matr[i] = b[i] / triangle_matr[i][i] - (triangle_matr[i][j] * x_matr[j]) / triangle_matr[i][i]
                        
    
    return x_matr


  


    
  
    
    
    
    
    
