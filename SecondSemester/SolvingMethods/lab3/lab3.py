#Bohdan Shybetskyi, 4th variant

import functions as fn


koef = 0.25 *   3
a = [[5.18 + koef, 1.12, 0.95, 1.32, 0.83],
     [1.12, 4.28 - koef, 2.12, 0.57, 0.91],
     [0.95, 2.12, 6.13 + koef, 1.29, 1.57],
     [1.32, 0.57, 1.29, 4.57 - koef, 1.25],
     [0.83, 0.91, 1.57, 1.25, 5.21 + koef]]
        
koef2 = 0.35 * 3 
b = [6.19 + koef2,
     3.21,
     4.28 - koef2,
     6.25,
     4.95 + koef2]



print("Input matrix:")
fn.print_matr(a, b)

print(fn.condition_check(a))
new_a, new_b = fn.make_diagonal(a, b)

fn.print_matr(new_a, new_b)
print(fn.condition_check(new_a))



print(fn.iteration_method(new_a, new_b))


