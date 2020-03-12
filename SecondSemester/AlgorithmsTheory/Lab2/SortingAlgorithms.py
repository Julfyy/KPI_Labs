def improvedBubbleSort(array):
    counter = 0
    i = 0
    swapped = True
    while(swapped):
        swapped = False
        for j in range(len(array) - 1 - i):
            counter+=1
            if(array[j+1] > array[j]):               
                array[j+1], array[j] = array[j], array[j+1]
                swapped = True
        i+=1
    return array, counter

def bubbleSort(array):
    counter = 0
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            counter+=1
            if(array[j+1] > array[j]):               
                array[j+1], array[j] = array[j], array[j+1]
    return array, counter



#Insertion Sort
def insertionSort(array):  
    counter= 0
    for i in range(1, len(array)): 
        key = array[i]                  #key is the second element of array
        j = i-1                         #Element before key
        #counter += 1
        while j >=0 and array[j] < key: #While each element is less then a key
            counter += 1
            array[j+1] = array[j]       #Move each element one step right
            j -= 1                      #Go to previous element
            #Keep moving elements to the right till they are less then key
        array[j+1] = key                #Set key value to the right position
    return array, counter







