#Лабораторна робота Шибецький Богдан ІС-92 Варіант 29 (4)
import math
import matplotlib.pyplot as plt
import numpy as np

def calculate_product(i, value, x): 
	pro = 1; 
	for j in range(i): 
		pro = pro * (value - x[j]); 
	return pro; 

def divided_differences(x, y, n): 
	for i in range(1, n): 
		for j in range(n - i): 
			y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) / (x[j] - x[i + j])); 
	return y; 

def Newton_interpolation(value, x, y, n): 
	sum = y[0][0]; 
	for i in range(1, n): 
		sum = sum + (calculate_product(i, value, x) * y[0][i]); 	
	return sum; 


#Задана функція
def function(x):
    return math.sin(x) + (x*2) ** 1/3


n = 5; 
y = [[0 for i in range(10)] for j in range(10)]; 
x = [-2, 0, 2, 4, 6]

for i in range(len(x)):
    y[i][0] = function(x[i])
    
y = divided_differences(x, y, n);

#Графік інтерпольованої функції
interpolated_x_plot = np.arange(-2, 6, 0.001)
interpolated_y_plot = [Newton_interpolation(i, x, y, n) for i in interpolated_x_plot]
plt.plot(interpolated_x_plot, interpolated_y_plot, label='Інтерпольована функція')

#Графік заданої функції
x_plot = np.arange(-2, 6, 0.001)
y_plot = [function(i) for i in x_plot]
plt.plot(x_plot, y_plot, label='Задана функція')

'''
#Визначення похибки
y_error = [abs(interpolated_y_plot[i] - y_plot[i]) for i in range(len(y_plot))]
plt.plot(x_plot, y_error, label='Функція похибки методу Ньютона')
plt.legend()
plt.show()
'''

#Вузли інтерполяції
x_i = [-2, 0, 2, 4, 6]
y = [function(i) for i in x_i]

plt.scatter(x_i, y)
plt.legend()
plt.show()





