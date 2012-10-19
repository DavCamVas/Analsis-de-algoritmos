import random
import math
import time

def maxHeapify(A, i):
    
    l = i * 2 + 1
    r = i * 2 + 2
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest)

def buildMaxHeap(A):
    for i in reversed(range(0,len(A) / 2)):
        maxHeapify(A, i)
        
def heapSort(A):
    buildMaxHeap(A)
    B = []
    for i in reversed(range(1,len(A))):  
        A[0], A[i] = A[i], A[0]
        B.insert(0, A.pop())     
        maxHeapify(A, 0)
    return B
    
def calculateTime(list):
    t = time.clock()
    heapSort(list)
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
print "Arreglo de 10 elementos ordenado: " + str(heapSort(list10))
print "Tiempo en ordenar un arreglo de 10 elementos: " + str(calculateTime(list10))
print "Tiempo en ordenar un arreglo de 20 elementos: " + str(calculateTime(list20))
print "Tiempo en ordenar un arreglo de 100 elementos: " + str(calculateTime(list100))
print "Tiempo en ordenar un arreglo de 1000 elementos: " + str(calculateTime(list1000))

    