import random
import math
import time

def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    return result

def mergeSort(lst):
    if len(lst) < 2:
        return lst
    middle = len(lst) / 2
    left = mergeSort(lst[:middle])
    right = mergeSort(lst[middle:])
    return merge(left, right)
    
def calculateTime(list):
    t = time.clock()
    mergeSort(list)
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

print "Tiempo en ordenar un arreglo de 10 elementos: " + str(calculateTime(list10))
print "Tiempo en ordenar un arreglo de 20 elementos: " + str(calculateTime(list20))
print "Tiempo en ordenar un arreglo de 100 elementos: " + str(calculateTime(list100))
print "Tiempo en ordenar un arreglo de 1000 elementos: " + str(calculateTime(list1000))
    