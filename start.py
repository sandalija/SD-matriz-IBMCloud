import insert as i
import calculate as c
import reduce as r
import pywren_ibm_cloud as pywren


bucket = 'deposit-sd-2020' 

"""
a_matrix_list = i.dividirMatriz(a, 1, False)
b_matrix_list = i.dividirMatriz(b, 1, True) # True para trasponerla 

print (a_matrix_list)
pw = pywren.ibm_cf_executor()
for a_elem in a_matrix_list:
    for b_elem in b_matrix_list:
        # Worker function
        print ("\n\n\****************n\n\n")
       pw.map(c.map_function, (a_elem, b_elem))
        print(pw.get_result())
        n = c.mapFunctionSecuancial(a_elem, b_elem)
        print (n)
        print ("\n\n\****************n\n\n")
    print ("\n\n\++++++++++++++++++n\n\n")
"""
# Retorna el número de fragments que habrá según el inidcado
def adaptarNumWorkers(n, cols, rows):
    i = True
    if (n > 100): n = 100
    while (cols*rows > n):
        if (i): cols = cols-1
        else: rows = rows-1
        i = (not i)
    return (cols, rows)


## SECUENCIAL
"""a = i.crearMatriz(4, 4, 10)
b = i.crearMatriz(4, 4, 10)
a_matrix_list = i.dividirMatriz(a, 1, False, 'A')
b_matrix_list = i.dividirMatriz(b, 1, True, 'B') # True para trasponerla 
pw = pywren.ibm_cf_executor()
pw.map(c.mapFunctionSecuencial, (a_matrix_list[0], b_matrix_list[0]))
print(pw.get_result())
pw.clean()"""


## PARALELA
a = i.crearMatriz(3, 5, 10)
b = i.crearMatriz(5, 4, 10)
print ("A")
print (a)
print ("B")
print (b)
n = int(input("Numbers of workers: "))
m = adaptarNumWorkers(n, 7, 4)
a_matrix_list = i.dividirMatriz(a, m[0], False, 'A')
b_matrix_list = i.dividirMatriz(b, m[1], True, 'B') # True para trasponerla
print ("Lista de A: " + str(a_matrix_list))
print ("Lista de B: " + str(b_matrix_list))
pw = pywren.ibm_cf_executor()
# map reduce y tal
# map está hecha
# reduce juntaria submatrices
params = []
for i in range(0, len(a_matrix_list)):
    for j in (range(0, len(b_matrix_list))):
        params.append((a_matrix_list[i], b_matrix_list[j], (a.shape[0], b.shape[1])))
print ("\n\n" + str(params) + "\n\n")
pw.map_reduce(c.mapFunctionDistr, params, r.reduceCapture)
print(pw.get_result())
pw.clean()
print ("FIN")
