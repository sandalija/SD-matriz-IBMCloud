import numpy as np
import pickle
from COS_backend import COS_Backend

# Obtener la matriz desde bucket indicado por parámetro
def obtenerMatriz(bucket, matriz):
    cos = COS_Backend()
    #filename = cos.get(matriz)
    data = cos.get_object(bucket, matriz)
    desceralized = pickle.loads(data)
    return (desceralized)

# Lista de las posiciones que tendrá que evaular cada worker
def listaWorkers(size, workers):
    step = int(size/workers)
    res = size % workers
    positions = []
    for i in range(0, size-res, step):
        positions.append((i, i+step-1))
    if (res != 0):
        positions.append((size-res, size-1))
    return (positions)

def callWorkerFuncion(n_workers, bucket, keyMatriz1, keyMatriz2):
    matriz1 = obtenerMatriz(bucket, keyMatriz1)
    matriz2 = obtenerMatriz(bucket, keyMatriz2)
    # Comprobar el tamaño de la matriz
    columns1 = matriz1.shape[0]
    rows1 = matriz1.shape[1]
    columns2 = matriz2.shape[0]
    rows2 = matriz2.shape[1]
    print ("Columnas de 1: " + str(columns1))
    print ("Filas de 2:" + str(rows2))
    if (columns1 != rows2): # No se puede mutiplicar
        # Add exception (?)
        print ("Matrix not operable")
        exit()
    else:
        positions = listaWorkers(rows1, 1)
        matriz2_trans = matriz2.transpose()
        print (positions)
        # obtener las filas de la matriz1
        filas = []
        columnas = []
        matriz_result = np.zeros(shape = matriz1.shape)
        for pos in positions:
            for i in range(0, rows1):
                if (i >= pos[0] and i <= pos[1]):
                    filas.append(matriz1[i])
                    columnas.append(matriz2_trans[i])
            # los workers van aquí
            for i in range(0, rows1):
                for j in range(0, columns1):
                    matriz_result[i][j] 

        print ("FILAS:")
        print (filas)
        print ("COLUMNAS")
        print (columnas)

# Recibe la los nombres de los buckets que leerá desde el IBM COS
def map_function(a_submatrix, b_submatrix):
    a_sub = obtenerMatriz('deposit-sd-2020', a_submatrix)
    b_sub = obtenerMatriz('deposit-sd-2020', b_submatrix)
    """ print ("A matrix")
    print (a_sub)
    print ("B matrix")
    print (b_sub) """
    result = 0
    for i in range(0, len(a_sub)):
        result = a_sub[i]*b_sub[i] + result
    return result

# Hecho
def mapFunctionSecuencial(a_submatrix, b_submatrix):
    a_sub = obtenerMatriz('deposit-sd-2020', a_submatrix)
    b_sub = obtenerMatriz('deposit-sd-2020', b_submatrix)
    rowsA = a_sub.shape[0]
    rowsB = b_sub.shape[0]
    columnsB = b_sub.shape[1]
    c = np.zeros(shape=(rowsA, rowsB))
    for i in range(0, rowsA):
        for j in range (0, rowsB):
            for k in range (0, columnsB):
                c[i, j] = c[i, j] + a_sub[i, k]*b_sub[j, k]
    return (c)

def obtenerParte(nombre_matriz):
    nombre_matriz = nombre_matriz[1:]
    nombre_matriz = nombre_matriz.replace('_matrix_part_', '')
    return nombre_matriz

def mapFunctionDistr(a_submatrix, b_submatrix, resutlDimension):
    a_sub = obtenerMatriz('deposit-sd-2020', a_submatrix)
    b_sub = obtenerMatriz('deposit-sd-2020', b_submatrix)
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
    return (c, rowsA, rowsB, resutlDimension)
