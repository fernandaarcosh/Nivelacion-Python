# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:55:12 2019

@author: Feña
"""

my_list = [1, 3, 4, 5, 10, 8, 7, 6]

#Usando lista de python
for i in range(len(my_list)):
    my_list[i] *=3

#Usando arreglo Numpy
# my_array *=3

import numpy as np
a = np.array([2, 3, 4]) # arreglo de 3 numeros
print a
 
a = np.arange(1, 12, 2) # arreglo del 1 hasta el 12 avanzando de a 2 
print a

a = np.linspace(1, 12, 6) # arreglo del 1 al 12 con 6 numeros de elemento
print a

a1 = a.reshape(3,2) # hace un cambio en la forma del arreglo matriz de 3 filas por 2 columnas
print a1

print a.size # tamaño, canidad de elemtos del arreglo
print a.shape
print a1.shape

print a.dtype # tipo de arreglo numero

print a.itemsize # cuanta memoria en bits tiene cada elemento

b = np.array([(1.5, 2, 3), (4, 5, 6)]) # arreglo en dos dimensiones
print b

print (a < 4) # entrega para cada elemento si es que esta condicion se cumple o no
print (a1 < 4)

print (a * 3) # multiplicacion de cada elemento del arreglo
print (a1 * 3)

#print (a *= 3)
#print (a1 *= 3)

a = np.zeros((3, 4)) # arreglo de una matriz de 3x4 llena de 0
print a

print a.dtype

a = np.ones((2, 3)) # arreglo de una matriz de 2x3 llena de 1
print a

a = np.ones(10) # matriz de 1x10 llena de 1
print a

a = np.array([2, 3, 4], dtype = np.int16)# para ahorrar memoria
print a

print a.dtype
print a.itemsize

a = np.random.random((2,3)) #arreglos al azar desde el 0 al 1
print a

#print a.np.set_printoptions(precision=2, suppress=True) # debiese entregar el arreglo con mayor precision

a = np.random.randint(0,10,5)
print a
print a.sum()
print a.min()
print a.max()
# print a.average() 
print a.var()
print a.std()

a = np.random.randint(1, 10, 6)
print a 
a3 = a.reshape(3,2)
print a3  # cambiar forma de la matriz a una de 3x2

print a3.sum(axis=1) # suma los elementos de una misma fila 
print a3.sum(axis=0) # suma las los elementos de cada columna

# Importar archivo de texto
# data = np.loadtxt("data.txt", dtype=np.uint8, delimiter=",", skiprows=1)

a = np.arange(10)
print a
a4 = np.random.shuffle(a) # se supone que modifica la secuancia del arreglo, pero no entiendo porque sale ninguna en todo momento
print a4
a5 = np.random.choice(a) # elccion al azar de 2 elementos del arreglo, todas las veces que corra salen distintos
print a5

b =np.random.random_integers(5, 10, 2) # arreglo de elementos del 5 al 10, solo dos elementps
print b
















