import numpy as np
import pickle
from COS_backend import COS_Backend

# Obtener la matriz desde bucket indicado por parámetro
def obtenerMatriz(bucket, matriz):
    cos = COS_Backend()
    #filename = cos.get(matriz)
    print ("Key: " + matriz)
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

def mapCandidate(filas, columnas):
    n = 0
    if (len(filas) != len(columnas)):
        # ERROR
        # Add exception (?)
        return -1
    else:
        for i in range(0, len(filas)):
            n = n + filas[i]*columnas[i]
    return n
