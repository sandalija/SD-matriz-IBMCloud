import insert as i


bucket = 'deposit-sd-2020' 
n = i.crearMatriz(6, 5, 10)
b = i.crearMatriz(3, 4, 10)
#i.guardarMatriz(n, bucket, 'matriz-test-1')
i.asyncGuardarMatriz(n)
print ("FIN")

