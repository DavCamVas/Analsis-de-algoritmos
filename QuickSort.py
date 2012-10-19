import random
import math
import time

def quickSort(A, p, r):
    if p < r:
        q = randomPartition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)
    return A

def randomPartition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i+=1
            A[i], A[j] = A[j], A[i] 
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1
    
def calculateTime(list):
    t = time.clock()
    quickSort(list, 0, len(list) - 1)
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

print "Arreglo de 10 elementos aleatorio: " + str(list10)
time10 = calculateTime(list10)
print "Arreglo de 10 elementos ordenado: " + str(list10)
print "Tiempo en ordenar un arreglo de 10 elementos: " + str(time10)
print "Tiempo en ordenar un arreglo de 20 elementos: " + str(calculateTime(list20))
print "Tiempo en ordenar un arreglo de 100 elementos: " + str(calculateTime(list100))
print "Tiempo en ordenar un arreglo de 1000 elementos: " + str(calculateTime(list1000))
    