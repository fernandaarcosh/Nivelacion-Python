# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:39:03 2019

@author: Feña
"""

from matplotlib import pyplot as plt

#print(plt.style.avaible) estilos de graficos que se pueden utilizar

plt.style.use('fivethirtyeight')

# 04:22, Ejemplo de salarios segun edad
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] # edad, datos que se ubicaran en eje x

dev_y = [38469, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752] #salario, datos que se ubicaran en el eje y

#marker, marca los puntos de los datos entregados
# Median Python Developer Salaries by Age
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] # edad, datos que se ubicaran en eje x

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640] #salario, datos que se ubicaran en el eje y

# 'b' blue, cambia el color de la linea, los colores tambien pueden ser escritos en codigos de numeros
# Median JavaScript Developer Salaries by Ages
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583] #salario, datos que se ubicaran en el eje y


plt.plot(dev_x, py_dev_y,color= 'b',marker='o', linewidth=3, label='Python')# como en todos los graficos las edades son las mismas se cambia los nombres y se ocupa el mismo
plt.plot(dev_x, js_dev_y,color= 'y', linewidth=3, label='JavaScript')
plt.plot(dev_x, dev_y, color= 'k', linestyle='--',marker='.',label='All Devs') # k--- linea punteada

plt.xlabel("Ages")# titulo eje x
plt.ylabel("Median Salary (USD)")#titulo eje y
plt.title("Median Salary (USD) by Age")#titulo del grafico

#plt.legend(["All Devs", 'Python'])#para poder identificar que linea en el grafico es de que 
plt.legend()

#plt.grid(True)

plt.tight_layout()

plt.savefig('plot.png')
plt.show()