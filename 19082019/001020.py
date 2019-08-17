# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:33:39 2019

@author: Feña
"""
import numpy as np
import scipy as sp

c = 3 # variable c se le asigna el valor 3
d = 4 # variable d se le asigna el valor 4

if c < d: # si es que se cumple que el valor de c sea menor que el de d se imprime la siguiente frase
    print ("c is less than d")

else: # si no se cumple lo que se menciono en el if anterior, se imprime la siguiente frase
    print ("c is NOT less than d")
    
    
#  Se prentende codificar el siguiente codigo, pedir ingresar 2 numeros del 1 al 5 y ver si son primos o no. (3,5)
print ("Ingresar dos numero del 1 al 5")
num_1 = input("Primer numero") # se pide ingresar el primer numero
num_2 = input ("Segundo numero") # se pide ingresar el segundo numero

num_1_1 = 0 # se crean variables de valor 0
num_2_2 = 0

if num_1 > 1: # en caso de que el primer numero ingresado sea mayor a 1
    num_1_1 = num_1 / float(2) # se realiza una division con el numero 2, entregando decimales
    if num_1_1 == int(num_1_1):# si la division entrega un resultado entero, el numero no es primo ya que es divisible por 2
        print ("El primer numero no es primo")
    else:# en el caso contrario, que el resultado entregue un decimal, el numero es primo
        print ("El primer numero es primo")
elif num_1 == 1: # en caso de que el valor del numero ingrsado sea 1, se imprime lo siguiente
    print ("El primer numero es primo")

if num_2 > 1:# se utiliza el mismo codigo para el segundo numero
    num_2_2 = num_2 / float(2) 
    if num_2_2 == int(num_2_2):
        print ("El segundo numero no es primo")
    else:
        print ("El segundo numero es primo")
elif num_2 == 1:
    print ("El segundo numero es primo")
    
