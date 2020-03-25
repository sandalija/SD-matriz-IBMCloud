import insert as i
import calculate as c
import pywren_ibm_cloud as pywren


bucket = 'deposit-sd-2020' 
a = i.crearMatriz(4, 4, 10)
b = i.crearMatriz(4, 4, 10)
i.dividirMatriz(a, 3, False)
i.dividirMatriz(b, 3, True) # True para trasponerla 
pywren.clean()


"""i.asyncGuardarMatriz(a, bucket, 'matriz-test-1')
i.asyncGuardarMatriz(b, bucket, 'matriz-test-2')
c.callWorkerFuncion(1, bucket, 'matriz-test-1', 'matriz-test-2' )
"""


print ("FIN")

