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
    matriz2 = obtenerMatriz(keyMatriz2)
    # Comprobar el tamaño de la matriz
    columns1 = matriz1.shape[0]
    rows2 = matriz2.shape[1]


bucket = 'deposit-sd-2020'
callWorkerFuncion(6, bucket, 'matriz', 'p')
