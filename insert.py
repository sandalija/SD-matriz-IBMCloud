import numpy as np
import pickle
from COS_backend import COS_Backend
import pywren_ibm_cloud as pywren

#Devuelve una matriz de dimension fila x col con valores maximos (maxValue)
def crearMatriz(fila, col, maxValue):
    if (maxValue is None):
        maxValue = 100
    random_matrix_array = np.random.randint(0,maxValue,size=(fila,col))
    return random_matrix_array

# Guarda la matriz serialitzada introducida por parametro 
# en el bucket de IBM COS indicado
def guardarMatriz(matriz, name_matrix, bucket):
    cos = COS_Backend()
    serialized = pickle.dumps(matriz, protocol=0) # protocol 0 is printable ASCII
    cos.put_object(bucket, name_matrix, serialized)
    exit()

def asyncGuardarMatriz(matriz, name_matrix, bucket):
    ibmcf = pywren.ibm_cf_executor()
    params = [matriz, name_matrix, bucket]
    print (params)
    ibmcf.call_async(guardarMatriz, params)

# Invoca guardarMatriz por cada submatriz generada.
# Retorna una lista con los nombres de los ficheros que contiene cada parte de la matriz
# en IBM COS
def dividirMatriz(matriz, n_workers, transpose, stamp, bucket):
    if (transpose):     # Si es la segunda matriz, giramos las filas por columnas
        matriz = matriz.transpose()
    root_name = '_matrix_part_'
    submatrix_len = matriz.shape[0]
    m = 0
    name_matrix = ''
    list_matrix = []    # lista con los nombres de las martices en el IBM Cloud COS
    list = []
    for i in range (0, n_workers):
        list.append(1)
    sum = 0
    for l in list:
        sum = sum + l
    pos = 0
    while (sum < submatrix_len):
        print (f"POS: {pos}")
        list[pos] = list[pos] + 1
        pos = (pos + 1) % n_workers
        sum = sum + 1
    # while i < submatrix_len:
    print ("LISTA")
    print (list)
    i = 0
    for l in list:
        name_matrix = stamp + root_name + str(m)
        list_matrix.append(name_matrix)
        print (f"I: {i}, l+i: {l+i}")
        submatrix = matriz[i:l+i,:]
        print ("Inserting submatrix " + name_matrix + "\trange " + \
           str(i) + " to " + str(int(submatrix_len/n_workers)+i - 1))
        asyncGuardarMatriz(submatrix, name_matrix, bucket)      # Dejar matriz en el Bucket
        i = i + l
        m = m + 1
    return (list_matrix)
