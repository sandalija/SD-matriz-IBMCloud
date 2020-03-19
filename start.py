import insert as i


bucket = 'deposit-sd-2020' 
n = i.crearMatriz(5, 5, 10)
b = i.crearMatriz(5, 5, 10)
i.asyncGuardarMatriz(n)
i.asyncGuardarMatriz(n)
print ("FIN")

