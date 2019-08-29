# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:05:02 2019

@author: Feña
"""

a = [1, 2, 3, 4]
b = [10, 11, 12, 13]

print a + b
# como realizar la suma de los item de las listas sin numpy
output = []
for item1, item2 in zip(a, b):
    output.append(item1 + item2)
print output

g = list(range(10000000))

# %timeit sum(g) # este caracter muestra el tiempo en que se demoraria en desarrollar la operacion

import numpy as np

g_array = np.array(g)

# %timeit np.sum(g_array) # se ve una baja de mas o menos un orden de magnitud

a = np.array([1, 2, 3, 4])
b = np.array([10, 11, 12, 13])

print a + b #este tipo de arreglos relaiza de inmediato la suma de elementos en la misma coordenada, no se ncesita un loop 
print a * b
print a / b

print a ** b
print a.ndim
print a.shape

# La ventaja de numpy,es que entrega varias funciones como log, exp, etc de forma rapida y practica

#tipo de arreglo realozado, memoria bits
print a.dtype

a = np.array([1, 2, 3, 4.0])
print a
print a.dtype

a = np.array([1, 2, 3, 4.0 +1j])
print a
print a.dtype

a = np.array([1, 2, 3, 4.0], dtype ='int32')
print a
print a.dtype

c = np.array([[10, 11, 12], [20, 21, 22]])
print c # matriz realizada de 2x3
print c.dtype
print c.ndim
print c.shape
print c.size
print c.nbytes

a = np.array([1, 2, 3, 4], dtype = 'int32')
print a
print a.T # matriz transpuesta

print a[0]# observar o sacar un elemento especifico de la matriz
#en caso de una matriz de dos dimensiones
print c[0, 0]
# para una lista de python, sin numpy c[0][0]
print c[0]# para ver la fila 0 del arreglo
print c[:,0]# para ver la columna 0 del arreglo

# minuto 42:54
a = np.arange(25).reshape(5,5)
print a

red = a[:, 1::2]
print red

yellow = a[4]
print yellow

# Tambien puede ser 
# yellow = a[-1]
# yellow = a [-1, :]

blue = a[1::2, :3:2]
print blue
#tambien sirve 
#blue = a[1::2, :4:2]
#blue = a[1::2, :-1:2]
#blue = a[1::2, :-2:2]

a = np.array([3, -1, -2, 4, -6, 8])
print a
print a < 0
negatives = a <0
print a[negatives]

a[a < 0] = 0
print a
print a < 0
print a < 8
print a > 3
# print a >3 and a < 8, no funcina dado el operador y.

print (a < 8).any()
# OPERACIONES BINARIAS: AND, OR, NOT
#BITWISE OPERATORS: &, |, ~, ^
print (a > 3) & (a < 8)

a1 = np.nonzero(negatives)
print a1

# 1:21:25
a = np.array([10, 1, 20])
subset = a[[0, 2]]
print subset
print a.flags.owndata
print subset.flags.owndata
print a is subset

print a
print subset

a[-1] = 100 #siempre se puede estar odificando el arreglo

# 1:25:33, se quieren las posiciones de todos los numeros divisibles por 3
a = np.arange(25).reshape(5,5)
print a
print a % 3 # lo que enttrega como 0 es por que esl numero es divisible por 3
print a[a % 3]

print a % 3 == 0# muestra si es verdadero no  todos los numero divisibles por 3
print a[a% 3 == 0]  #muestra el numero que es divisible por 3 en el arreglo

output = np.empty_like(a, dtype ='float') # areglo que se parezca a la matriz a
print output 
print output.fill(np.nan)

mask = a % 3 == 0 # se crea un arreglo con los numeros divisibles por 3
output[mask] = a[mask]# se rellena la amtriz output con los elementos divisibles de a en su posicion
print output

print a[mask]
print output[mask]

# 1:55:50
# Rules
# rule 2
d = np.nan + 6
print d

d = np.sum([1, np.nan, 9])
print d

d = np.nansum([1, np.nan, 9])
print d

# metodos y funciones
a = np.array([1, 2, 3])
print a
print np.sum(a) # funcion actua sobre lo que se pone dentro
print a.sum() # metodo actua sobre el elemento que se le asigna 

# 2:10:15
a = np.arange(24).reshape(6,4)
print a
print a.shape
print a.mean(axis=0).shape # cantidad de filas que posee la matrz
print a.mean(axis=1).shape # seria cantidad de columnas 

channel_means = a.mean(axis=1)# para siempre estar claro en que se esta trbajando y donde 
print channel_means

# 2:15:54
# no se encontro el archivo con el que se trbaja en la pagina indicada bajo el video de youtube
# esto es oara trabajar con archivos de texto
# from numpy import loadtext
# data = loadtext("wind.data")
# dates = data [:, :3] # se extrae la informacion de la poscion deseada y se agrega a una matriz d eelementos llamada dates
# winds = data[:, 3:]

#print (winds.mean(), winds.min(), winds.max(), winds.std()) # se imprime y muestra en pantalla desde la matriz winds los maximos, minos valores de esto, ademas de la cantidad de valores 
#print (winds.min(axis=0)) # muestra cual es el minimo de los valores en las filas de la matriz
#print (winds.min(axis=1)) # muestra el minimo valor de las columnas de la matriz winds
#print (winds.argmax(axis=1))#localzacion del valor deseado dentro de la matriz

#Encontrar los datos asociados a cierto valor de la matriz
# row = winds.max(axis = 1).argmax() # encontrando el mayor valor 
# print (dates[row]) # se busca la fecha de el valor encontrado

#January = dates[:, 1] == 1 # fechas del primer mes del año, para asciarlas a la matriz de vientos 
#print winds[January, :].mean(axis=0) # valores de viento que tienen en su informacion la fecha del mes de enero
