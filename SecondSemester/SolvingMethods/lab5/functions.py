import numpy as np
import copy


def print_matr(a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print("%0.3f" % a[i][j], end = "\t")
        print("| %0.3f" % b[i])
    print()
    
def print_one_matr(a, it):
    for i in range(len(a)):
        for j in range(it,len(a[0])):
            if(a[i][j] != 0):
                print("%0.3f" % a[i][j], end = "\t")
        print()
    
    

def condition_check(a):
    flag = [0] * len(a)
    row_sum = [0] * len(a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            if j != i:
                row_sum[i] += abs(a[i][j])
            if row_sum[i] < abs(a[i][i]):
                flag[i] = True
            else:
                flag[i] = False
    print("Condition check:")
    return flag


def make_diagonal(arg_a, arg_b):
    a = copy.deepcopy(arg_a)
    b = copy.deepcopy(arg_b)
    k = 0
  
    n = len(a)
    m = len(a[0])
    
    #Finding a_main the max element in the whole matrix
    a_main = a[k][k] #Suppose that a_main is the element [0][0]
    main_line = k
    main_column = k
    
   
    #Finding all koeficients m for not main lines
    m_arr = [1 for x in range(n)]
    # m_arr contain a 0 for the main line
    for i in range(n):
        if i > main_line:
            m_arr[i] = a[i][main_column] / a_main
    #print(m_arr)
  
    
    #First step to make zeros in main_column in not main lines
    for i in range(n):
        if i > main_line:
            for j in range(m):
                a[i][j] -= m_arr[i] * a[main_line][j]
            b[i] -= m_arr[i] * b[main_line]
  
    return a, b


def iteration_method(arg_a,arg_b):
    a = copy.deepcopy(arg_a)
    b = copy.deepcopy(arg_b)
   
    n = len(a)
    m = len(a[0])
    
    iteration_counter = 0;
    epsilon = 0.000001

    x_matr = [[0 for i in range(100)] for j in range(len(a))] 
    alpha = [[0 for i in range(len(a))] for j in range(len(a[0]))]
    beta = [0 for i in range(len(a))]
    row_x_sum = 0
    
    #Making alpha end beta matrices
    for i in range(n):
        for j in range(m):
            if i != j:
                alpha[i][j] = -a[i][j]/a[i][i]
                beta[i] = b[i]/a[i][i]
    #print("\n Alpha and beta matrices:")
    #print_matr(alpha, beta)
   
    while(True):
        for i in range(n):
            row_x_sum = 0
            for j in range(m):
                row_x_sum += (alpha[i][j] * x_matr[j][iteration_counter])
            x_matr[i][iteration_counter + 1] = beta[i] + row_x_sum
        
        
        '''
        if iteration_counter < 4 or iteration_counter > 35:
            #print("\n ====== {} iteration ======".format(iteration_counter))
            print_one_matr(x_matr, iteration_counter)
            print("\n Difference vector:")
            for i in range(n):
                print("%0.6f" %difference_vector(a, b, x_matr, iteration_counter)[i])
        '''
        
        maxx = 0;
        for i in range(n):
            temp = x_matr[i][iteration_counter + 1] - x_matr[i][iteration_counter]
            if abs(temp) > maxx:
                maxx = abs(temp)
        
        output = [0]*n
        if (maxx < epsilon):
            for i in range(n):
                output[i] = x_matr[i][iteration_counter] 
            #print("\nX values are:")
            return output
            
        iteration_counter += 1
    
    
    
def difference_vector(a, b, x, it):
    r = [0]*len(a)
    for i in range(len(a)):
        row_x_sum = 0
        for j in range(len(a[0])):
            row_x_sum += (a[i][j] * x[j][it])
        r[i] = b[i] - row_x_sum
    return r



        
    
    
    

    
    
              
    

    




