# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:35:36 2019

@author: Feña
"""

a = ["banana", "apple", "microsoft"]
for element in a:# se recorre los elementos de la lista
    print (element)# para cada elemento se imprime su valor
        
b = [20, 10, 5]
total = 0 
for e in b:# se recorren los elementos de la lista b
    print(e)# se imprime el valor de cada elemento
    total = total + e# se le suma al antiguo valor de total el elemento actual
print (total)

#1, 2, 3, 4
#range(1, 5)#arreglo de numeros que va desde el 1 sin tomar el 5, numeros enteros
c = list(range(1, 5))# lista de arreglos del 1 al 4

#no es neceaario poner el arreglo en una lista para poder recorrerlo con un for
for i in range(1, 5):
    print(i)

#Ejercicio Video; calcular la suma de todos los múltiplos de 3 y 5
# entre 100 numeros y ver si la suma es mayor a 100
k = 0 # contador en 0
for i in range(1,100):# se recorren los numeros desde el 1 al 99
    if i % 3 == 0:# si es que el resto de la division de i con 3 es 0, se sumaa i al contador
        k += i
    elif i % 5 == 0:# si no, se observa si el resto de i con 5 es 0, si lo es
        k += i# se suma i al contador
print (k)# valor final y total del contador
    
    
        