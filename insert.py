import numpy as np
import pickle
from COS_backend import COS_Backend
import pywren_ibm_cloud as pywren


def crearMatriz(fila, col, maxValue):
    if (maxValue is None):
        maxValue = 100
    random_matrix_array = np.random.randint(0,maxValue,size=(fila,col))
    return random_matrix_array

def guardarMatriz(matriz, name_matrix):
    cos = COS_Backend()
    bucket = 'deposit-sd-2020'
    serialized = pickle.dumps(matriz, protocol=0) # protocol 0 is printable ASCII
    cos.put_object(bucket, name_matrix, serialized)
    exit()

def asyncGuardarMatriz(matriz, name_matrix):
    ibmcf = pywren.ibm_cf_executor()
    params = [matriz, name_matrix]
    print (params)
    ibmcf.call_async(guardarMatriz, params)

# Invoca a guardarMatrix(..) por cada worker.
# Retorna una lista con los nombres de los ficheros que contiene cada parte de la matriz
# en IBM COS
def dividirMatriz(matriz, n_workers, transpose, stamp):
    if (transpose):     # Si es la segunda matriz, giramos las filas por columnas
        matriz = matriz.transpose()
    root_name = '_matrix_part_'
    submatrix_len = matriz.shape[1]
    i = 0
    m = 0
    name_matrix = ''
    list_matrix = []    # lista con los nombres de las martices en el IBM Cloud COS
    while i < submatrix_len:
        name_matrix = stamp + root_name + str(m)
        list_matrix.append(name_matrix)
        #print ("De " + str(i) + " a " + str(int(submatrix_len/n_workers)+i - 1))
        submatrix = matriz[i:int(submatrix_len/n_workers)+i,:]
        print ("Inserting submatrix " + name_matrix + "\trange " + \
           str(i) + " to " + str(int(submatrix_len/n_workers)+i - 1))
        asyncGuardarMatriz(submatrix, name_matrix)      # Dejar matriz en el Bucket
        i = i + int(submatrix_len/n_workers)
        m = m + 1
    return (list_matrix)
    """i = i - int(submatrix_len/n_workers)
    if (submatrix_len % n_workers != 0):
        i = i + int(submatrix_len/n_workers)
        name_matrix = stamp + root_name + str(m)
        print (name_matrix)
        print ("De " + str(i) + " a " + str(int(submatrix_len/n_workers)+i - 1))
        print (matriz[i: submatrix_len-1,:])"""

