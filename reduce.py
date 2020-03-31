import numpy as np
import pickle
import insert as i
import calculate as c
from COS_backend import COS_Backend

def reduceCapture(results):
    i = results
    return (results)

def adaptarNumWorkers(n, cols, rows):
    i = True
    while (cols*rows > n):
        if (i): cols = cols-1
        else: rows = rows-1
        i = (not i)
    return (cols, rows)

a = i.crearMatriz(3, 3, 10)
b = i.crearMatriz(3, 4, 10)
print ("B")
print (b)
n = int(input("Numbers of workers: "))
m = adaptarNumWorkers(n, 4, 4)
print ("partes " + str(m))
a_matrix_list = i.dividirMatriz(a, m[0], False)
b_matrix_list = i.dividirMatriz(b, m[1], True)
print ("A matrix list: " + str(a_matrix_list))
n = c.mapFunctionSecuencial(a_matrix_list[0], b_matrix_list[0])
print (n)
"""for a_elem in a_matrix_list:
    for b_elem in b_matrix_list:
        print ("A elem: " + a_elem)
        print ("B elem: " + b_elem)
        n = c.mapFunctionDistr(a_elem, b_elem)
        print (n)"""