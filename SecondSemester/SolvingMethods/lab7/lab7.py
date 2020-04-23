#Богдан Шибецький ІС-92
#Варіант 4

import math
import numpy as np

def function(x):
    return math.cos(x) / (x + 1)

a = -0.7
b = 1.2


def trapezoid_integration(func, a, b, n):
    indices = np.linspace(a, b, n)
    
    summ = 0
    for i in range(1, n-1):
        summ += func(indices[i])
        
    return ((b - a) / (2 * n)) * (func(a) + 2 * summ + func(b))

def gaussian_integration(func, a, b, n):
    
    c = [0.129485, 0.279705, 0.381830, 0.417960, 0.381830, 0.279705, 0.129485]
    t = [-0.949108, -0.741531, -0.405845,0, 0.405845, 0.741531, 0.949108]
    #Заміняємо межі інтегрування
    z = [((b+a)/2) + (((b-a) / 2) * x) for x in t]
    integr_sum = 0
    for i in range(n):
        integr_sum += c[i] * func(z[i])
        
    return ((b-a)/2) * integr_sum
        
integral0 = 1.72230813698


integral1 = trapezoid_integration(function, a, b, 512)
integral2 = gaussian_integration(function, a, b, 7)

error1 = integral1 - integral0
error2 = integral2 - integral0

print('Похибка методу трапецій %0.5f' % error1)
print('Похибка методу Гауса %0.5f' % error2)

