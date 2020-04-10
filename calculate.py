import numpy as np
import pickle
from COS_backend import COS_Backend

# Obtiene la matriz (nombre del fichero) desde el bucket indicado por parámetro
def obtenerMatriz(bucket, matriz):
    cos = COS_Backend()
    data = cos.get_object(bucket, matriz)
    desceralized = pickle.loads(data)
    return (desceralized)

def obtenerParte(nombre_matriz):
    nombre_matriz = nombre_matriz[1:]
    nombre_matriz = nombre_matriz.replace('_matrix_part_', '')
    return nombre_matriz

def mapFunction(a_submatrix, b_submatrix, resultDimension, bucket):
    a_sub = obtenerMatriz(bucket, a_submatrix)
    b_sub = obtenerMatriz(bucket, b_submatrix)
    rowsA = a_sub.shape[0]
    rowsB = b_sub.shape[0]
    columnsB = b_sub.shape[1]
    c = np.zeros(shape=(rowsA, rowsB))
    for i in range(0, rowsA):
        for j in range (0, rowsB):
            for k in range (0, columnsB):
                c[i, j] = c[i, j] + a_sub[i, k]*b_sub[j, k]
    """a_part = obtenerParte(a_submatrix)
    b_part = obtenerParte(b_submatrix)"""
    return (c, rowsA, rowsB, resultDimension)
