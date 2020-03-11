from COS_backend import COS_Backend

cos = COS_Backend()

bucket = 'deposit-sd-2020'

#cos.put_object(bucket, 'prova.txt', b'Hola')


data = cos.get_object(bucket, 'prova.txt')

print("RECIEVED FOR IBM COS")
print(data)


"""
data = cos.head_object(bucket, 'prova.txt')

print("RECIEVED FOR IBM COS")
print(data)
"""

# cos.delete_object(bucket, 'prova.txt')

"""
cos.put_object(bucket, 'prova.txt', b'Hola')
cos.put_object(bucket, 'prova2.txt', b'P')
cos.put_object(bucket, 'prova3.txt', b'Q')
cos.put_object(bucket, 'prova4.txt', b'R')
"""
# data = cos.list_object(bucket)
# print(data)





exit()

