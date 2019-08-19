# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:07:36 2019

@author: Feña
"""

# Lista
a = [3, 10, -1]
print (a)

a.append(1)#se agrega el valor 1 a la lista
print (a)

a.append("hello")# se pueden mezclar numeros y palabras en la lista.
print (a)

a.append([1, 2])# se pueden agregar listas a la lista.
print (a)

a.pop() #elimina el ultimo elemento de la lista
print (a)

a[0]# recuperar el valor en la posicion 0 de la lista
print(a[0])

a[0] = 100 #se cambia el valor de la posicion 0 en la lista
print (a)

#Ejercicio video
b = ["banana", "apple","microsoft"]# lista con 3 elementos en ella
c = b[0] #variable que toma el valor de la posicion 0 de la lista
b[0] = b[2] # la posicion 0 toma el valor de la posicion 2
b[2] = c #la posicion 2 toma el valor de la variable c

print (b)

#metodo rapido y fácil.
#b[0], b[2] = b[2], b[0]