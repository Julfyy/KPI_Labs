#Лабораторна робота Шибецький Б. ІС-92

import numpy as np
import matplotlib.pyplot as plt
import math

#Задана функція
f = lambda x, y: 1 + (2.6)*y*math.sin(x) - y**2


def RungeKuttaMethod(f, xo, yo, tEnd, h):
    def deltaY(f, x, y, h):
        k1 = h * f(x,y)
        k2 = h * f(x+h/2,y+k1/2)
        k3 = h * f(x+h/2,y+k2/2)
        k4 = h * f(x+h, y + k3)
        #theta = abs((k2 - k3)/(k1 - k2))
        #print(theta)
        return (k1 + 2*k2 + 2*k3 + k4) / 6
    
    x = []
    y = []
    x.append(xo)
    y.append(yo)
     
    while xo < xEnd:
        h = min(h, xEnd - xo)
        yo += deltaY(f, xo, yo, h)
        xo += h
        x.append(xo)
        y.append(yo)
    return x, y

def AdamsMethod(a, b, yo, n):
    y = np.zeros(n)
    y[0] = yo
    h = (b - a)/(n - 1)
    X = [a + i*h for i in range(n)]
    
    get_f = lambda i: f(X[i], y[i])#Лямбда вираз для спрощення
    
    for i in range(1, 4):#Метод Ранге Кутта для визначення перших 4ьох коренів
        q1 = h*get_f(i-1)
        q2 = h*f(X[i-1] + h/2, y[i-1] + q1/2)
        q3 = h*f(X[i-1] + h/2, y[i-1] + q2/2)
        q4 = h*f(X[i-1] + h, y[i-1] + q3)
        y[i] = y[i-1] + (q1 + 2*q2 + 2*q3 + q4)/6
        
    for i in range(4, n): #Хід екстраполяційного методу Адамса
        y[i] = y[i-1] + h*(55*get_f(i-1) - 59*get_f(i-2) + 37*get_f(i-3) - 9*get_f(i-4))/24
        #print(abs(y[i-1] + h*(9*get_f(i) + 19*get_f(i-1) - 5*get_f(i-2) + 1*get_f(i-3))/24 - y[i]))
    return X, y

xo = 0 #Початок проміжку
xEnd = 6 #Кінець проміжку
yo = 0 #Умова для задачі Коші

h = 0.1 #Крок
X, Y = RungeKuttaMethod(f, xo, yo, xEnd, h)

n = 62
x, y = AdamsMethod(xo,xEnd, yo, n)


plt.figure()
plt.plot(X, Y,label='Метод Рунге—Кутта')
plt.legend()
plt.grid(True)

#plt.figure()
plt.plot(x, y, label='Метод Адамса')
plt.legend()
plt.grid(True)
plt.show()

'''
#Обчислення похибок

RKerror = []
Aerror= []
for i in range(62):
    RKerror.append((abs(Y[i]**h - Y[i]**(h/2))) / 15)
    Aerror.append((abs(y[i]**h - y[i]**(h/2))) / 15)
    
plt.figure()
plt.plot(x, RKerror, label='Похибка Рунге-Кутта')
plt.plot(x, Aerror, label='Похибка Адамса')
plt.legend()
plt.grid(True)
plt.show()

'''
#Виведення всіх дискретних значень та похибок, отриманих двома методами
print("Х\tРунге-Кутта\tАдамса\t\tПохибка Р.К.\tПохибка А.")
for i in range(62):
    if i == 31:
        print("Х\tРунге-Кутта\tАдамса\t\tПохибка Р.К.\tПохибка А.")
    print("{0:02.1f}\t{1:2f}\t{2:2f}\t{3:2f}\t{4:2f}".format(x[i], Y[i], y[i], RKerror[i], Aerror[i]))
