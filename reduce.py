import numpy as np
import pickle
import insert as i
import calculate as c
from COS_backend import COS_Backend

# Recibe por parametro los resultados obtenidos de cada worker
# Introduce estos valores en un array lineal que se redimensiona segun el tamaño de la matriz resultado
def reduceCapture(results):
    matrix = []
    row = 0
    col = 0
    for r in results:
        m = r[0]
        values = np.array(m)
        row = r[3][1]
        col = r[3][0]
        for v in values:
            for x in v:
                if (type(x) is list): 
                    for n in x:
                        matrix.append(n)
                else: matrix.append(x)
    matrix = np.array(matrix)
    matrix = np.reshape(matrix, (row, col))
    return (matrix)
