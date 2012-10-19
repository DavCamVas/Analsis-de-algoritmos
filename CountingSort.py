import random
import math
import time

def countingSort(A, k):
    B = []
    C = []
    for i in range(0, len(A)):
        B.append(0)
    for i in range(0, k + 1):
        C.append(0)
    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(1, k + 1):
        C[i] = C[i] + C[i -1]
    for j in reversed(range(0, len(A))):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

    return B
    
def calculateTime(list):
    t = time.clock()
    countingSort(list, len(list) * 2)
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
print "Arreglo de 10 elementos ordenado: " + str(countingSort(list10, len(list10)*2))
print "Tiempo en ordenar un arreglo de 10 elementos: " + str(calculateTime(list10))
print "Tiempo en ordenar un arreglo de 20 elementos: " + str(calculateTime(list20))
print "Tiempo en ordenar un arreglo de 100 elementos: " + str(calculateTime(list100))
print "Tiempo en ordenar un arreglo de 1000 elementos: " + str(calculateTime(list1000))
