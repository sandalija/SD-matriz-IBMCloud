import insert as i
import calculate as c
import pywren_ibm_cloud as pywren


bucket = 'deposit-sd-2020' 

"""
a_matrix_list = i.dividirMatriz(a, 1, False)
b_matrix_list = i.dividirMatriz(b, 1, True) # True para trasponerla 

print (a_matrix_list)
pw = pywren.ibm_cf_executor()
for a_elem in a_matrix_list:
    for b_elem in b_matrix_list:
        # Worker function
        print ("\n\n\****************n\n\n")
       pw.map(c.map_function, (a_elem, b_elem))
        print(pw.get_result())
        n = c.mapFunctionSecuancial(a_elem, b_elem)
        print (n)
        print ("\n\n\****************n\n\n")
    print ("\n\n\++++++++++++++++++n\n\n")
"""
a = i.crearMatriz(4, 4, 10)
b = i.crearMatriz(4, 4, 10)
a_matrix_list = i.dividirMatriz(a, 1, False)
print (a_matrix_list)
b_matrix_list = i.dividirMatriz(b, 1, True) # True para trasponerla 
c.mapFunctionSecuencial(a_matrix_list, b_matrix_list)

pywren.clean()




print ("FIN")

