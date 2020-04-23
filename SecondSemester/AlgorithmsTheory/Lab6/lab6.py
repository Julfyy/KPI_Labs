#Lab #6 by Bohdan Shybetskyi

#Отримання індексу батьківського елементу
def parent(i):
    return i >> 1

#Отримання індексу лівого дочірнього вузла
def left(i):
    return i << 1

#Отримання індексу правого дочірнього вузла
def right(i):
    return (i << 1) + 1

class MaxHeap:
    def __init__(self):
        self.heap_array = []
        
    def get_maximum(self):
        return self.heap_array[0]
    
    #Функція збільшення значення елемента за індексом та розташування його на правильну позицію
    def increase_key(self, i, key):
        if key < self.heap_array[i - 1]: #Перевірка чи ключ не менший за значення елемента
            return -1
        #Цикл while від індексу елемента до кореня та якщо батьківський ел менший за поточний
        while i > 0 and self.heap_array[parent(i)] < self.heap_array[i]:  
            #Якщо так, поміняти ці елементи місцями
            self.heap_array[i], self.heap_array[parent(i)] = self.heap_array[parent(i)], self.heap_array[i]
            i = parent(i)
    
    def max_insert(self, x):
        self.heap_array.append(x)  #Додаємо елемент в кінець
        #Замінюємо значення останнього елемента іксом та переміщуємо в правильне місце
        self.increase_key(len(max_heap.heap_array) - 1, x)
      
    def max_heapify(self, i):
        p = left(i)  
        q = right(i) 
        if p <= len(self.heap_array) - 1 and self.heap_array[p] > self.heap_array[i]:  
            largest = p
        else:
            largest = i
        if q <= len(self.heap_array) - 1 and self.heap_array[q] > self.heap_array[largest]:
            largest = q
        if largest != i:
            self.heap_array[i], self.heap_array[largest] = self.heap_array[largest], self.heap_array[i]
            self.max_heapify(largest)
            
    def heap_extract_max(self):
        if len(self.heap_array) < 1:
            return -1  #Помилка, бо черга порожня
        maximum = self.heap_array[0]   #Зберігаємо перший елемент
        self.heap_array[0] = self.heap_array[len(self.heap_array) - 1]  #Присвоюємо йому значення останнього
        self.heap_array.pop()    #Видаляємо останній елемент масиву
        self.max_heapify(0)  #Відновлюємо властивості піраміди
        return maximum  # повертаємо значення максимального елемента

        
        
class MinHeap:
    
    def __init__(self):
        self.heap_array = []
    
    def get_minimum(self):
        return self.heap_array[0]
   
    #Функція зменшення значення елемента за індексом та розташування його на правильну позицію
    def decrease_key(self, i, key):
        if key > self.heap_array[i - 1]:  #Перевірка чи ключ не більший за значення елемента
            return -1
        #Цикл while від індексу елемента до кореня та якщо батьківський ел більший за поточний
        while i > 0 and self.heap_array[parent(i)] > self.heap_array[i]:  
            #Якщо так, поміняти ці елементи місцями
            self.heap_array[i], self.heap_array[parent(i)] = self.heap_array[parent(i)], self.heap_array[i]
            i = parent(i)
    
    # вставка елемента у неспадну піраміду
    def min_insert(self, x):
        self.heap_array.append(x)  #Додаємо елемент в кінець
        #Замінюємо значення останнього елемента іксом та переміщуємо в правильне місце
        self.decrease_key(len(min_heap.heap_array) - 1, x)
    
    
    def min_heapify(self, i):
        p = left(i)  
        q = right(i) 
        if p <= len(self.heap_array) - 1 and self.heap_array[p] < self.heap_array[i]:  
            smallest = p
        else:
            smallest = i
        if q <= len(self.heap_array) - 1 and self.heap_array[q] < self.heap_array[smallest]:
            smallest = q
        if smallest != i:
            self.heap_array[i], self.heap_array[smallest] = self.heap_array[smallest], self.heap_array[i]
            self.min_heapify(smallest)
    
    #Функція для вилучення мінімального елементу з неспадної піраміди
    def heap_extract_min(self):
        if len(self.heap_array) < 1:
            return -1 #Помилка, бо черга порожня
        minimum = self.heap_array[0]  #Зберігаємо перший елемент
        self.heap_array[0] = self.heap_array[len(self.heap_array) - 1]#Присвоюємо йому значення останнього
        self.heap_array.pop()  #Видаляємо останній елемент масиву
        self.min_heapify(0)   #Відновлюємо властивості піраміди
        return minimum  # повертаємо значення мінімального елемента

#Функція вставки елементу в одну з пірамід
def insert_element(max_heap, min_heap, x, i):
    if i == 0:   
        max_heap.max_insert(x) #Якщо це перший елемент, додаємо в незростаючу піраміду H_low
    else:
        if x < max_heap.get_maximum():  # якщо x менше ніж найбільший елемент з max_heap, то додаємо його у цю піраміду
            max_heap.max_insert(x)
        else:  # інакше додаємо його у min_heap
            min_heap.min_insert(x)
    '''       
    Перевірка на збереження інваріанту:
        кількість елементів в піраміді H_low не повинна відрізнятись від 
        кількості елементів в H_high більше ніж на одиницю
    '''
   
    if len(max_heap.heap_array) - len(min_heap.heap_array) > 1:
        min_heap.min_insert(max_heap.get_maximum()) #Вставити найбільший елемент в min_heap
        max_heap.heap_extract_max()#Видаляємо цей елемент в піраміді max_heap
        min_heap.min_heapify(0) #Відновлюємо властивості піраміди

    elif len(max_heap.heap_array) - len(min_heap.heap_array) < -1:
        max_heap.max_insert(min_heap.get_minimum()) #Вставити менший елемент в max_heap
        min_heap.heap_extract_min() #Видаляємо цей елемент в піраміді min_heap
        max_heap.max_heapify(0)#Відновлюємо властивості піраміди


def median_search(max_heap, min_heap, x, i): 
   
    if len(max_heap.heap_array) - len(min_heap.heap_array) == 1:
        return max_heap.get_maximum()
    elif len(max_heap.heap_array) - len(min_heap.heap_array) == -1:
        return min_heap.get_minimum()
    elif len(max_heap.heap_array) == len(min_heap.heap_array):
        return max_heap.get_maximum(), min_heap.get_minimum()



input_file = open("task_04_examples/input_05_10.txt")
elements = input_file.readlines()
number_of_elements = int(elements[0])
input_array = [i for i in range(number_of_elements)]

for i in range(number_of_elements):
    input_array[i] = int(elements[i+1]) 

max_heap = MaxHeap() #Незростаюча піраміда H_low`
min_heap = MinHeap() #Неспадна піраміда H_high`


output_file = open("./is92_shybetskyi_16_output.txt", "w")
for i in range(number_of_elements):
    insert_element(max_heap, min_heap, input_array[i], i)
    output_file.write(str(median_search(max_heap, min_heap, input_array[i], i))+"\n" )
output_file.close()