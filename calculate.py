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
    rows1 = matriz1.shape[0]
    rows2 = matriz2.shape[1]
    print ("Columnas de 1: " + str(columns1))
    print ("Filas de 2:" + str(rows2))
    if (columns1 != rows2): # No se puede mutiplicar
        # Add exception (?)
        print ("Matrix not operable")
        exit()
    else:
        positions = listaWorkers(rows1, 1)
        for i in positions:
            a = matriz1[np.ix_([i[0]])]


