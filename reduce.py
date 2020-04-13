import numpy as np
import pickle
import insert as i
import calculate as c
import operator
from COS_backend import COS_Backend

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

# Recibe por parametro los resultados obtenidos de cada worker
# Introduce estos valores en un array lineal que se redimensiona segun el tamaño de la matriz resultado
def reduceCapture(results):
    m = Stack()
    a = 0
    results.sort(key=operator.itemgetter(1, 2), reverse = True)    
    for r in results:  # por cada worker
        i = 0
        row = r[5][1]
        cols = r[5][0]
        col = fila = 0
        for c in r[0]:     # por cada row de submatriz
            m.push((c, int(r[1]), int(r[2])))

    matrix = []
    temp = m.pop()
    last = [temp[1], temp[2]] # Fila y columna inicial
    for n in temp[0]:
        matrix.append(n)
    #matrix.append(temp)
    nexts = Stack()
    while (m.isEmpty() is False):
        if (temp[1] > last[0]):
            matrix.append(-1)
            m.push(temp)
            while (nexts.isEmpty() is False):
                m.push(nexts.pop())
            last = [-1, -1]
        temp = m.pop()
        if (temp[1] == last[0] and temp[2] == last[1]):
             # De la misma subamtriz, me lo salto
            nexts.push(temp)
        else:
            for n in temp[0]:
                matrix.append((temp, last))
            last = [temp[1], temp[2]]
    """ matrix = [ ]
    while (m.isEmpty() is False):
         matrix.append(m.pop()) """
    """ matrix = np.array(matrix)
    matrix = np.reshape(matrix, (row, cols)) """
    return (matrix)