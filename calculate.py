import numpy as np
import pickle
from COS_backend import COS_Backend


def obtenerMatriz(bucket, matriz):
    cos = COS_Backend()
    #filename = cos.get(matriz)
    data = cos.get_object(bucket, matriz)
    desceralized = pickle.loads(data)
    exit()
    return (desceralized)

def asyncCalcular(size, workers):
    step = int(size/workers)
    print (step)
    res = size % workers
    positions = []
    for i in range(0, size-res, step):
        positions.append((i, i+step-1))
    positions.append((size-res, size-1))
    print (positions)

asyncCalcular(99, 33)
