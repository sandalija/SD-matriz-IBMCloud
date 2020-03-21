import insert as i
import calculate as c


bucket = 'deposit-sd-2020' 
a = i.crearMatriz(6, 6, 10)
b = i.crearMatriz(6, 6, 10)
i.asyncGuardarMatriz(a, bucket, 'matriz-test-1')
i.asyncGuardarMatriz(b, bucket, 'matriz-test-2')
c.callWorkerFuncion(1, bucket, 'matriz-test-1', 'matriz-test-2' )



print ("FIN")

