import numpy as np
import pickle
from COS_backend import COS_Backend
import pywren_ibm_cloud as pywren


def crearMatriz(fila, col, maxValue):
    if (maxValue is None):
        maxValue = 100
    random_matrix_array = np.random.randint(0,maxValue,size=(fila,col))
    return random_matrix_array

def comprobarRangos(matriz1, matriz2):
    print (matriz1.shape)
    print ("Filas de 1" + str(a))

def guardarMatriz(matriz):
    cos = COS_Backend()
    bucket = 'deposit-sd-2020'
    serialized = pickle.dumps(matriz, protocol=0) # protocol 0 is printable ASCII
    cos.put_object(bucket, 'matriz', serialized)
    exit()

def asyncGuardarMatriz(matriz):
    ibmcf = pywren.ibm_cf_executor()
    ibmcf.call_async(guardarMatriz, matriz)
    print(ibmcf.get_result())
        
n = crearMatriz(5, 5, 10)
b = crearMatriz(5, 5, 10)
guardarMatriz(n)
print ("FIN")

