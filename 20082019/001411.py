# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 21:09:03 2019

@author: Feña
"""

# funciones: coleccion de instrucciones, coleccion de codigos
def function1():
    print ("ahhhh")
    print ("ahhhh 2")
print ("fuera de la funcion")

function1()
#mapeo, se toma una entrada y se retorna una salida / output
def function2(x):
    return 2*x
    
a = function2(3)

def function3(x,y):
    return x + y

def function4(x):
    print(x)
    print("sigue en la funcion")
    return 3 * x

f = function4(4)
print (f)

#Claculadora que convierta millas en kilometros
def convert_km(x):#funcion de conversion de millas a kilometros
    return 1.6 * x# trnasformacion de lo ingresado por en millas por 1.6
    #retornando la cantidad en kilometros

x = input("Cantidad de Millas:")# variable x toma la cantidad de millas
km = convert_km(x)# la variable km toma el valor que retorna la funcion convert_km
print ("Cantidad en Kilometros"),km # se imprime valor que entrega la funcion
    