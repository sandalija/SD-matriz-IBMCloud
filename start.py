import insert as i
import calculate as c
import reduce as r
import pywren_ibm_cloud as pywren
import time as t


bucket = 'deposit-sd-2020'

# Adapta el numero de Workers para realizar la division de matrices
def adaptarNumWorkers(n, cols, rows):
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
pw.clean()
