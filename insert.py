import numpy as np
import pickle
from COS_backend import COS_Backend
import pywren_ibm_cloud as pywren

bucket = 'deposit-sd-2020'
name_matriz = ''
matriz = []
params = [matriz, bucket, name_matriz]


def crearMatriz(fila, col, maxValue):
    if (maxValue is None):
        maxValue = 100
    random_matrix_array = np.random.randint(0,maxValue,size=(fila,col))
    matriz = random_matrix_array
    return random_matrix_array

def comprobarRangos(matriz1, matriz2):
    print (matriz1.shape)
    print ("Filas de 1" + str(a))

def guardarMatriz(matriz, bucket, name_matrix):
    cos = COS_Backend()
    #bucket = 'deposit-sd-2020'
    serialized = pickle.dumps(matriz, protocol=0) # protocol 0 is printable ASCII
    cos.put_object(bucket, name_matrix, serialized)
    exit()

def asyncGuardarMatriz(matriz, bucket, name_matrix):
    ibmcf = pywren.ibm_cf_executor()
    params = [matriz, bucket, name_matrix]
    print (params)
    ibmcf.call_async(guardarMatriz, params)
    print("H")
