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

# SECUENCIAL
a = i.crearMatriz(2, 3, 10)
b = i.crearMatriz(3, 2, 10)
print ("B")
print (b)
a_matrix_list = i.dividirMatriz(a, 1, False, 'A')
b_matrix_list = i.dividirMatriz(b, 1, True, 'B')
print ("A matrix list: " + str(a_matrix_list))
n = c.mapFunctionSecuencial(a_matrix_list[0], b_matrix_list[0])
print (n)
"""for a_elem in a_matrix_list:
    for b_elem in b_matrix_list:
        print ("A elem: " + a_elem)
        print ("B elem: " + b_elem)
        n = c.mapFunctionDistr(a_elem, b_elem)
        print (n)"""