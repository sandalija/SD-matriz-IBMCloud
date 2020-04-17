import insert as i
import calculate as c
import reduce as r
import pywren_ibm_cloud as pywren
import numpy as np
import math
import time as t


bucket = 'deposit-sd-2020'

# Adapta el numero de Workers para realizar la division de matrices
def adaptarNumWorkers(n, rows):
    if (n > rows): n = rows
    elif (n > 100): n = 100
    return (n)

v = int(input("Max Value:"))
m = int(input("A Rows: "))
n = int(input("A Columns / B Rows: "))
l = int(input("B Columns: "))
a = i.crearMatriz(m, n, v)
b = i.crearMatriz(n, l, v)
w = int(input("Workers: "))
print ("A:")
print (a)
print ("B:")
print (b)

if (w is not 1): 
    wk = adaptarNumWorkers(w, m)
    print (f"\n\n*******\nW: {wk} \n*******\n")
    a_matrix_list = i.dividirMatriz(a, wk, False, 'A', bucket)
    b_matrix_list = i.dividirMatriz(b, 1, False, 'B', bucket)
    pw = pywren.ibm_cf_executor()
    params = []
    for i in range(0, len(a_matrix_list)):
        params.append((a_matrix_list[i], b_matrix_list[0], (l, m), bucket))
    print ("\n\n" + str(params) + "\n\n")
    start_time = t.time()
    futures = pw.map_reduce(c.mapFunction, params, r.reduceCapture)
    
else:
    a_matrix_list = i.dividirMatriz(a, 1, False, 'A', bucket)
    b_matrix_list = i.dividirMatriz(b, 1, False, 'B', bucket) 
    pw = pywren.ibm_cf_executor()
    start_time = t.time()
    futures = pw.map(c.mapFunction, (a_matrix_list[0], b_matrix_list[0], (l, m), bucket))
matrix = pw.get_result()
print(matrix)
pw.wait(futures)
elapsed_time = t.time() - start_time
print("Seconds: %.3f" % elapsed_time)
pw.clean()  