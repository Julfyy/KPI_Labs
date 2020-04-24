#Лаб №6 Шибецький Богдан

epsilon = 0.0001

'''
#Функції ряду Штурма
def function(x):
    return 2*(x**4) - (x**3) - 5*(x**2) + 2*x - 2
def function1(x):
    return 8*(x**3) - 3*(x**2) -10*x
def function2(x):
    return 83*(x**2) -54*x + 64
def function3(x):
    return 101504*x + 11712

#Обчислення значень для заповнення таблиці
x = 3.5
print(function(x))
print(function1(x))
print(function2(x))
print(function3(x))
'''


class Polynome():
    def function(self, x):
        return 2*(x**4) - (x**3) - 5*(x**2) + 2*x - 2
    def first_derivative(self, x):
        return 8*(x**3) - 3*(x**2) -10*x
    def second_derivative(self, x):
        return 24*(x**2) - 6*x


    def bisection_method(self, func, a, b, epsilon):
        if (b - a > 2 * epsilon): #Якшо не досягнуто точності
            #Присвоюємо с значення середини
            c = (a + b) / 2
            #Якщо с це корінь рівняння, повертаємо його
            if func(c) == 0:
                return c
            #Якщо функція змінює знак в першому інтервалі
            if (func(a)*func(c) < 0):
                c = self.bisection_method(func, a, c, epsilon)
                return c           
            
            #Якщо функція змінює знак в другому інтервалі
            elif (func(c)*func(b) < 0):
                c = self.bisection_method(func, c, b, epsilon)
                return c
            
        return (a+b)/2  #Повертаємо корінь що є серединою проміжка         

    def chord_method(self, function, a, b, epsilon):
        c = []
        func = function.function

        
        if (func(a) * function.second_derivative(a) > 0):  
            c.append(b)  #С_0 = b, закрірлюємо праву межу
            c.append(b - ((b - a) * (func(b))) / (func(b) - func(a)))
            while(abs(c[-1] - c[-2]) > epsilon and abs(func(c[-1])) > epsilon): #Поки не буде досягнуто похибки
                c.append(c[-1] - ((c[-1] - a) * (func(c[-1]))) / (func(c[-1]) - func(a)))
       
        elif (func(b) * function.second_derivative(b) > 0):  
            c.append(a)  #С_0 = а, закріплюємо ліву межу
            c.append(a - ((b - a) * (func(a))) / (func(b) - func(a)))
            while(abs(c[-1] - c[-2]) > epsilon and abs(func(c[-1])) > epsilon): #Поки не буде досягнуто похибки
                c.append(c[-1] - ((b - c[-1]) * (func(c[-1]))) / (func(b) - func(c[-1])))
        return c[-1]
    
    def Neutons_method(self, function, a, b, epsilon):
        c = []
        func = function.function
        
        if (func(b) * function.second_derivative(b) > 0):  
            c.append(b)  #С_0 = 
            c.append(b - (func(b))/(function.first_derivative(b)))
        elif (func(a) * function.second_derivative(a) > 0):  
            c.append(a)  #С_0 = І
            c.append(a - (func(a))/(function.first_derivative(a)))
        
        while(abs(c[-1] - c[-2]) > epsilon and abs(func(c[-1])) > epsilon): #Поки не буде досягнуто похибки
            c.append(c[-1] - (func(c[-1])) / (function.first_derivative(c[-1])))

         
        return c[-1]
        


poly = Polynome()
            
x1 = poly.bisection_method(poly.function, -2.58, -1, epsilon)
x2 = poly.bisection_method(poly.function, 1, 2, epsilon)

xx1 = poly.chord_method(poly, -2.58, -1, epsilon)
xx2 = poly.chord_method(poly, 1, 2, epsilon)

xxx1 = poly.Neutons_method(poly, -2.58, -1, epsilon)
xxx2 = poly.Neutons_method(poly, 1, 2, epsilon)
 






