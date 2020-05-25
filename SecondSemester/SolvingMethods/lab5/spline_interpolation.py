import math
import numpy as np
import matplotlib.pyplot as plt
import functions as fn



def cubic_spline(x, y):
    x = np.array(x)
    y = np.array(y)
    
    if np.any(np.diff(x) < 0):
        idx = np.argsort(x)
        x = x[idx]
        y = y[idx]

    size = len(x)
    delta_x = np.diff(x)
    delta_y = np.diff(y)
    
    A = np.zeros(shape = (size,size))
    b = np.zeros(shape=(size,1))
    A[0,0] = 1
    A[-1,-1] = 1
    
    for i in range(1,size-1):
        A[i, i-1] = delta_x[i-1]
        A[i, i+1] = delta_x[i]
        A[i,i] = 2*(delta_x[i-1]+delta_x[i])
        b[i,0] = 3*(delta_y[i]/delta_x[i] - delta_y[i-1]/delta_x[i-1])
        
    c = fn.iteration_method(A, b)  #Використовую метод з попередньої лаби
    
    d = np.zeros(shape = (size-1,1))
    b = np.zeros(shape = (size-1,1))
    for i in range(0,len(d)):
        d[i] = (c[i+1] - c[i]) / (3*delta_x[i])
        b[i] = (delta_y[i]/delta_x[i]) - (delta_x[i]/3)*(2*c[i] + c[i+1])    
    
    return b, c, d


#Задана функція
def function(x):
    return math.sin(x) + (x*2) ** 1/3

#Вузли інтерполяції
x_i = [-2, 0, 2, 4, 6]
y = [function(i) for i in x_i]

plt.scatter(x_i, y)
    
b,c,d = cubic_spline(x_i, y)
a = y

c = np.array(c[:-1])


def spline(x, j):
    return a[j] + b[j]*(x - x_i[j]) + c[j]*((x - x_i[j])**2) + d[j]*((x - x_i[j])**3)

#Будуємо графік інтерпольованої функції
y_interp = [[] for i in range(len(x_i))]
for j in range(0, len(x_i) - 1):
    x_interp = np.arange(x_i[j], x_i[j+1], 0.01)
    for i in x_interp:
        y_interp[j].append(spline(i, j))
    plt.plot(x_interp, y_interp[j], label='Графік сплайн функції S_{}'.format(j+1))


#Графік заданої функції
x_plot = np.arange(-2, 6, 0.01)
y_plot = [function(i) for i in x_plot]
plt.plot(x_plot, y_plot,label='Задана функція')
plt.title('Порівняльний графік')
plt.legend()
plt.show()

'''
y_error = []
#Визначення похибки
for j in range(len(x_i)-1):
    for i in range(len(y_interp[0])):
        y_error.append(abs(y_interp[j][i] - y_plot[len(y_interp[0]) * j + i]))
        

plt.plot(x_plot, y_error,label='Функція похибки для спла')
plt.legend()
plt.show()
'''       


