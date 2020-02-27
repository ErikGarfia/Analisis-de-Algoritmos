import random
import random
import os
import sys
import numpy
from timeit import timeit
from time import time


def quicksort(arr, start, stop):
    global start_time
    start_time = time()
    if(start < stop):
        pivotindex = partitionrand(arr, start, stop)
        quicksort(arr, start, pivotindex - 1)
        quicksort(arr, pivotindex + 1, stop)


def partitionrand(arr, start, stop):
    global randpivot
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)


def partition(arr, start, stop):
    pivot = start
    i = start + 1
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return (pivot)


def opciones():
    print('Valores que puede tomar n, Elige uno\n')
    print("A)1000\nB)2000\nC)3000\nD)4000\nE)5000\nF)6000\nG)7000\nH)8000\nI)9000\nJ)10,000\n")


opciones()
array = []
vn = input("Que valor de n quieres?\n")
if (vn == 'A'):
    for j in range(1000):
        array.append(random.randint(1, 100000))
    n = len(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo desordenado\n", array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo ordenado\n")
    quicksort(array, 0, len(array) - 1)
    print(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("el pivote fue el numero en la posicion\n", randpivot)
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'B'):
    for j in range(2000):
        array.append(random.randint(1, 100000))
    n = len(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo desordenado\n", array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo ordenado\n")
    quicksort(array, 0, len(array) - 1)
    print(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("el pivote fue el numero en la posicion\n", randpivot)
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'C'):
    for j in range(3000):
        array.append(random.randint(1, 100000))
    n = len(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo desordenado\n", array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo ordenado\n")
    quicksort(array, 0, len(array) - 1)
    print(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("el pivote fue el numero en la posicion\n", randpivot)
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'D'):
    for j in range(4000):
        array.append(random.randint(1, 100000))
    n = len(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo desordenado\n", array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo ordenado\n")
    quicksort(array, 0, len(array) - 1)
    print(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("el pivote fue el numero en la posicion\n", randpivot)
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'E'):
    for j in range(5000):
        array.append(random.randint(1, 100000))
    n = len(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo desordenado\n", array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo ordenado\n")
    quicksort(array, 0, len(array) - 1)
    print(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("el pivote fue el numero en la posicion\n", randpivot)
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'F'):
    for j in range(6000):
        array.append(random.randint(1, 100000))
    n = len(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo desordenado\n", array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo ordenado\n")
    quicksort(array, 0, len(array) - 1)
    print(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("el pivote fue el numero en la posicion\n", randpivot)
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'G'):
    for j in range(7000):
        array.append(random.randint(1, 100000))
    n = len(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo desordenado\n", array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo ordenado\n")
    quicksort(array, 0, len(array) - 1)
    print(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("el pivote fue el numero en la posicion\n", randpivot)
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'H'):
    for j in range(8000):
        array.append(random.randint(1, 100000))
    n = len(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo desordenado\n", array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo ordenado\n")
    quicksort(array, 0, len(array) - 1)
    print(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("el pivote fue el numero en la posicion\n", randpivot)
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'I'):
    for j in range(9000):
        array.append(random.randint(1, 100000))
    n = len(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo desordenado\n", array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo ordenado\n")
    quicksort(array, 0, len(array) - 1)
    print(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("el pivote fue el numero en la posicion\n", randpivot)
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'J'):
    for j in range(10000):
        array.append(random.randint(1, 100000))
    n = len(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo desordenado\n", array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Arreglo ordenado\n")
    quicksort(array, 0, len(array) - 1)
    print(array)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("el pivote fue el numero en la posicion\n", randpivot)
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)
