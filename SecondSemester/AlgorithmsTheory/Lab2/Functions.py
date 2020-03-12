import random 
import matplotlib.pyplot as plt

#Initialising an array
def initArray(n, gen_type):
    if gen_type == "worst":
        a = [i+1 for i in range(n)]
    elif gen_type == "best":
        a = [i+1 for i in reversed(range(n))]
    elif gen_type == "random":
        a = [i+1 for i in range(n)]
        random.shuffle(a)
    return a

 

def define_graph(x, y,  gen_type, sort_type):
    for i in range(len(y)):
        plt.plot(x, y[i], label = gen_type[i])     
    plt.xlabel('number of elements') 
    plt.ylabel('number of swaps') 
    plt.title(sort_type) 
    
    plt.legend()
    plt.show()
       
def graph_by_sort_type(sort_type):

    n = [i*100 for i in range(1, 11)]
     
    gen_type = ["worst", "best", "random"]
    counter = []
    
    for j in range(len(gen_type)): #For every gen type of array
        temp_counter = [0]*len(n)
        for i in range(len(n)):     #For every number of elements
            array = initArray(n[i], gen_type[j])
            sorted_array, temp_counter[i] = sort_type(array) #Sort that array
        counter.append(temp_counter)
    define_graph(n, counter, gen_type, sort_type.__name__)
    






    