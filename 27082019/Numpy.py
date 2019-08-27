# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:41:02 2019

@author: Feña
"""
import numpy as np

a = np.zeros(3) # matrices de ceros, esta es de 1 x 3
print a

z = np.zeros(10) # matriz de ceros, de 1 x 10
print z

z.shape # forma de la matriz

z.shape = (10, 1) # cambiar la forma de la matriz
print z

z = np.ones(10) # matriz de puros 1, de 1 x 1'
print z

z = np.empty(3) # otra forma de escribir matriz vacía
print z

z = np.linspace(2, 10, 5)# crea una matriz con un rango y punto de partida y final
print z

z = np.array ([10, 20]) # matriz desde una lista
print z

a_list = [1, 2, 3, 4, 5, 6, 7]
z = np.array([a_list])
print z

print z.shape

b_list= [[9, 8, 7, 6, 5, 4, 3],[1, 2, 3, 4, 5, 6, 7]]# matriz en 2D
z = np.array([b_list])
print z

np.random.seed(0) # arreglo al azar
z1 = np.random.randint(10, size=6) # no se por que aparece error de los parentesis que ocipa, siendo que es el mismo codigo del videp
print z1

# Para poder ver una foto, y su tipo de matriz.Como no esta esta la foto, se dejara como comentario
#from skimae import io
#import Image
#import matplotlib.pyplot as plt
#photo = Image.open("photo.jpg")
#type(photo)
#plt.imshow(photo[|| -1]) #Da vuelta la foto, giro en 180°
#plt.imshow(photo[:,::-1]) #invierte las columnas de la imagen
#plt.imshow(photo [50:150, 150:200])# corte en la foto, agarra una seccion

#photo 
#photo_sin =np.sin(photo)
#photo_sin

#print (np.sum(photo))
#print (np.prod(photo))
#print (np.mean(photo))
#print (np.std(photo))
#print (np.var(photo))
#print (np.min(photo))
#print (np.max(photo))
#print (np.argmin(photo))
#print (np.argmax(photo))

z = np.array([1, 2, 3, 4, 5])
print (z < 3)
print (z > 3)
print (z[z > 3])

#photo_masked = np.where(photo >100, 255,0) # reemplaza los valores mayores a 100 por 255
#plt.imshow(photo_masked) #finalmetnte se muestra la imagen con difererntes tonalidades de saturacion

a_array = np.array([1, 2, 3, 4, 5])
b_array = np.array([6, 7, 8, 9, 10])

print a_array + b_array

print a_array + 30
# print (a_array @ b_array) producto entre ambos arreglos

x = np.array([2, 1, 4, 3, 5])
x_1 = np.sort(x)

print x_1


