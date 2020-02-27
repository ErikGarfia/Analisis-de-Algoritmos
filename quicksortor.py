import random
import os
import sys
import numpy
from timeit import timeit
from time import time
arr = []

# MODELO DETERMINISTICO, ELEGIMOS EL PIVOTE. EL PIVOTE ES EL ELEMENTO MAS GRANDE


def partition(arr, min, mayor):
    i = (min-1)
    pivot = arr[mayor]

    for j in range(min, mayor):

        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[mayor] = arr[mayor], arr[i+1]
    return (i+1)


def opciones():
    print('Valores que puede tomar n, Elige uno\n')
    print("A)1000\nB)2000\nC)3000\nD)4000\nE)5000\nF)6000\nG)7000\nH)8000\nI)9000\nJ)10,000\n")


def quickSort(arr, min, mayor):
    global start_time
    start_time = time()
    if min < mayor:
        pi = partition(arr, min, mayor)
        quickSort(arr, min, pi-1)
        quickSort(arr, pi+1, mayor)


opciones()
vn = input("Que valor de n quieres?\n")
if (vn == 'A'):
    for j in range(1000):
        arr.append(random.randint(1, 100000))
    n = len(arr)
    print("Arreglo desordenado\n", arr)
    quickSort(arr, 0, n-1)
    print("Arreglo ordenado")
    for i in range(n):
        print("%d" % arr[i])
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'B'):
    for j in range(2000):
        arr.append(random.randint(1, 100000))
    n = len(arr)
    print("Arreglo desordenado\n", arr)
    quickSort(arr, 0, n-1)
    print("Arreglo ordenado")
    for i in range(n):
        print("%d" % arr[i])
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'C'):
    for j in range(3000):
        arr.append(random.randint(1, 100000))
    n = len(arr)
    print("Arreglo desordenado\n", arr)
    quickSort(arr, 0, n-1)
    print("Arreglo ordenado")
    for i in range(n):
        print("%d" % arr[i])
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'D'):
    for j in range(4000):
        arr.append(random.randint(1, 100000))
    n = len(arr)
    print("Arreglo desordenado\n", arr)
    quickSort(arr, 0, n-1)
    print("Arreglo ordenado")
    for i in range(n):
        print("%d" % arr[i])
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'E'):
    for j in range(5000):
        arr.append(random.randint(1, 100000))
    n = len(arr)
    print("Arreglo desordenado\n", arr)
    quickSort(arr, 0, n-1)
    print("Arreglo ordenado")
    for i in range(n):
        print("%d" % arr[i])
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'F'):
    for j in range(6000):
        arr.append(random.randint(1, 100000))
    n = len(arr)
    print("Arreglo desordenado\n", arr)
    quickSort(arr, 0, n-1)
    print("Arreglo ordenado")
    for i in range(n):
        print("%d" % arr[i])
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'G'):
    for j in range(7000):
        arr.append(random.randint(1, 100000))
    n = len(arr)
    print("Arreglo desordenado\n", arr)
    quickSort(arr, 0, n-1)
    print("Arreglo ordenado")
    for i in range(n):
        print("%d" % arr[i])
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'H'):
    for j in range(8000):
        arr.append(random.randint(1, 100000))
    n = len(arr)
    print("Arreglo desordenado\n", arr)
    quickSort(arr, 0, n-1)
    print("Arreglo ordenado")
    for i in range(n):
        print("%d" % arr[i])
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'I'):
    for j in range(9000):
        arr.append(random.randint(1, 100000))
    n = len(arr)
    print("Arreglo desordenado\n", arr)
    quickSort(arr, 0, n-1)
    print("Arreglo ordenado")
    for i in range(n):
        print("%d" % arr[i])
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)

if (vn == 'J'):
    for j in range(10000):
        arr.append(random.randint(1, 100000))
    n = len(arr)
    print("Arreglo desordenado\n", arr)
    quickSort(arr, 0, n-1)
    print("Arreglo ordenado")
    for i in range(n):
        print("%d" % arr[i])
    t_transcurrido = time() - start_time
    print("Tiempo %.6f " % t_transcurrido)
