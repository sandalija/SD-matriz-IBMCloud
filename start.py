import insert as i
import calculate as c
import reduce as r
import pywren_ibm_cloud as pywren
import numpy as np
import math
import time as t


bucket = 'deposit-sd-2020'

# Adapta el numero de Workers para realizar la division de matrices
""" def adaptarNumWorkers(n, cols, rows):
    i = True
    if (n > 100): n = 100
    while (cols*rows > n):
        if (i): cols = cols-1
        else: rows = rows-1
        i = (not i)
    return (cols, rows)

v = int(input("Max Value:"))
m = int(input("A Rows: "))
n = int(input("A Columns / B Rows: "))
l = int(input("B Columns: "))
a = i.crearMatriz(m, n, v)
b = i.crearMatriz(n, l, v)
w = int(input("Workers: "))
start_time = t.time()
if (n is not 1): 
    wk = adaptarNumWorkers(w, l, m)
    a_matrix_list = i.dividirMatriz(a, wk[0], False, 'A', bucket)
    b_matrix_list = i.dividirMatriz(b, wk[1], True, 'B', bucket) # True para trasponerla
    pw = pywren.ibm_cf_executor()
    params = []
    for i in range(0, len(a_matrix_list)):
        for j in (range(0, len(b_matrix_list))):
            params.append((a_matrix_list[i], b_matrix_list[j], (l, m), bucket))
    print ("\n\n" + str(params) + "\n\n")
    futures = pw.map_reduce(c.mapFunction, params, r.reduceCapture)
else:
    a_matrix_list = i.dividirMatriz(a, 1, False, 'A', bucket)
    b_matrix_list = i.dividirMatriz(b, 1, True, 'B', bucket) # True para trasponerla 
    pw = pywren.ibm_cf_executor()
    futures = pw.map(c.mapFunction, (a_matrix_list[0], b_matrix_list[0], (l, m), bucket))
print(pw.get_result())
pw.wait(futures)
elapsed_time = t.time() - start_time
print("Seconds: %.3f" % elapsed_time)
pw.clean() """

def adaptarNumWorkers(n, cols, rows):
    if (n > 100): n = 100
    if (cols*rows < n): n = cols*rows
    sq = math.sqrt(n)
    print (f"SQ: {sq}")
    sq_tmp = sq - int(sq)
    print (f"SQ_tmp: {sq_tmp}")
    if (sq_tmp == 0): # es entero
        cols = int(sq)
        rows = int(sq)
    else:
        cols = int(sq)
        rows = int(sq) + 1
    print (f"cols: {cols}, rows: {rows}")
    return (cols, rows)
    """ i = True
    if (n > 100): n = 100
    while (cols*rows > n):
        if (i): cols = cols-1
        else: rows = rows-1
        i = (not i)
    return (cols, rows) """

v = int(input("Max Value:"))
m = int(input("A Rows: "))
n = int(input("A Columns / B Rows: "))
l = int(input("B Columns: "))
""" a = i.crearMatriz(m, n, v)
b = i.crearMatriz(n, l, v) """
a = np.matrix([[1, 2, 3, 4],  [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
b = np.matrix([[5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8]])
w = int(input("Workers: "))
print ("A")
print (a)
print ("B")
print (b)
start_time = t.time()
if (w is not 1): 
    wk = adaptarNumWorkers(w, l, m)
    #wk = (10, 9)
    a_matrix_list = i.dividirMatriz(a, wk[0], False, 'A', bucket)
    b_matrix_list = i.dividirMatriz(b, wk[1], True, 'B', bucket) # True para trasponerla
    print (a_matrix_list)
    print (b_matrix_list)
    pw = pywren.ibm_cf_executor()
    params = []
    for i in range(0, len(a_matrix_list)):
        for j in (range(0, len(b_matrix_list))):
            params.append((a_matrix_list[i], b_matrix_list[j], (l, m), bucket))
            # c.mapFunction(a_matrix_list[i], b_matrix_list[j], (m, l), bucket)
    print ("\n\n" + str(params) + "\n\n")
    futures = pw.map_reduce(c.mapFunction, params, r.reduceCapture)
    
else:
    a_matrix_list = i.dividirMatriz(a, 1, False, 'A', bucket)
    b_matrix_list = i.dividirMatriz(b, 1, True, 'B', bucket) # True para trasponerla 
    pw = pywren.ibm_cf_executor()
    futures = pw.map(c.mapFunction, (a_matrix_list[0], b_matrix_list[0], (l, m), bucket))
matrix = pw.get_result()
# matrix = np.reshape(matrix, (m, l))
print(matrix)
print(f"Len {len(matrix)}")
pw.wait(futures)
elapsed_time = t.time() - start_time
print("Seconds: %.3f" % elapsed_time)
pw.clean()
