# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:07:39 2019

@author: Feña
"""

# While loops
# se peude realizar algunas cosas iguales que con el for in 
total = 0 # contador en 0
j = 1 # se comienza con el valor 1
while j < 5: # esto es mientras se cumpla la condicion de que j es menor a 5
    total += j# si se cumple, se suma el valor de j al total
    j += 1 # luego se le suma una unidad mas al valor de j
print (total)

given_list = [5, 4, 4, 3, 1]
total = 0
i = 0

while i < len(given_list) and given_list[i] > 0:# se crean las restricciones necesarias para que oueda correr el progrma
    total += given_list[i]
    i += 1
print (total)

given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total = 0
for element in given_list2:
    if element <= 0: #solo se quiere contabilizar los numeros postivos
        break# si los numeros son negativos se rompe el ciclo
    total += element
print (total)

total_1 = 0
i = 0
while True:# para que se entre en el ciclo, una afirmacion siempre verdadera
    total_1 += given_list2[i]# agregar al contador el elemento de la lista
    i += 1
    if given_list2[i] <= 0:#excluir los numeros negativos
        break# se rompe el ciclo
print (total_1)

#Ejercicio Video
given_list3 = [15, 26, 31, 8, -12, -3, -1, -6, 10, 14, -17, -15]#lista cualquiera
given_list3.sort(reverse=True)#lista en orden descendente

print(given_list3)

given_list3.sort()#lista en orden ascendente

total = 0
i = 0

while 1 < 2:# afirmacion verdadera para entrar en el ciclo
    total += given_list3[i]#suma de los numeros negativos
    i += 1
    if given_list3[i] >= 0:#romper el ciclo al momento de entrar a los numeros positivos
        break
print (total)