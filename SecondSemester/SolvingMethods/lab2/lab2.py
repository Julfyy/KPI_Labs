#Bohdan Shybetskyi, 4th variant

import functions as fn


koef = 0.5*3
a = [[3.81, 0.25, 1.28, 0.75+koef],
     [2.25, 1.32, 4.58+koef, 0.49],
     [5.31, 6.28+koef, 0.98, 1.04],
     [9.39+koef, 2.45, 3.35, 2.28]]
        
b = [4.21,
     6.47+koef,
     2.38,
     10.48+koef]

fn.print_matr(a, b)
print(fn.gauss(a, b))







