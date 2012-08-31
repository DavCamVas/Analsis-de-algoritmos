import random
import time

def insertionSort(list): 
    n = len(list) 
    for i in range(n):
      indice = list[i]
      a = i-1
      while (a >= 0 and list[a] > indice):
         list[a+1] = list[a]
         a = a-1
      list[a+1] = indice

def calculateTime(list):
    t = time.clock()
    insertionSort(list)
    t = time.clock()  - t
    return t

def randomArray(n):
    list = []
    for i in range(n):
        list.append(random.randint(0, n*2))
    
    return list
    
list10 = randomArray(10)
list20 = randomArray(20)
list100 = randomArray(100)
list1000 = randomArray(1000)

t = time.clock()
insertionSort(list10)
t = time.clock()  - t
print "Tiempo en ordenar un arreglo de 10 elementos: " + str(calculateTime(list10))
print "Tiempo en ordenar un arreglo de 20 elementos: " + str(calculateTime(list20))
print "Tiempo en ordenar un arreglo de 100 elementos: " + str(calculateTime(list100))
print "Tiempo en ordenar un arreglo de 1000 elementos: " + str(calculateTime(list1000))
