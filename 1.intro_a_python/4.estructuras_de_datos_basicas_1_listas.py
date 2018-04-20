# -*- coding: utf-8 -*-
"""
Las estructuras de datos son aquellos objetos que se usan para almacenar
información.
Hay muchos tipos, pero estos son los básicos en python.
"""

"""
*******************************************************************************
LISTAS
*******************************************************************************

Las listas son conjuntos de elementos ordenados donde cada elemento tiene una
posición.

"""
#%%
frutas = ["naranja", "manzana", "pera", "fresa"]
print(frutas)
print(type(frutas))

#%%
# Accedemos a los elementos de una lista con []
# El indice de los elementos de una lista empieza en 0, eso quiere decir 
# que el primer elemento se accede con [0]
primera_fruta = frutas[0]
print(primera_fruta)
#%%
# Podemos acceder a un rango de elementos de una lista con [inicio:final-1:orden]
print(frutas[:2])
#%%
# accedemos a los elementos desde el 2 hasta el final
print(frutas[2:])
#%%
"""Podemos acceder a los elementos empezando por el final accediendo a la lista 
con numeros negativos
Por ejemplo, accedemos a los ultimos dos elementos
"""
print(frutas[-2:])
#%%
#podemos saltarnos elementos de n en n usando [::n], por ejemplo, si solo queremos
#los elementos impares
print(frutas[::2])
# print(frutas[1:3:2]) # incial, final-1, orden
# print(frutas[:]) # Lo imprime todo
#%%
#si el orden es un numero negativo nos devolverá la lista en sentido inverso 
print(frutas[::-1])
# print(frutas[::-2]) # impares en sentido inverso
#%%
#Podemos ver el número de elementos de una lista con len
print(len(frutas))
#%%
#podemos añadir elementos a listas con append. Esto modifica la lista original
frutas.append("melon")
print(frutas)

#%%
# podemos repetir una lista multiplicandola por un entero
print(frutas * 2)  
#%%
#Podemos concatenar listas con el simbolo +
ciudades = ["Murcia", "Cartagena"]
print(frutas + ciudades) # Prints concatenated lists

#%%
#Podemos modificar elementos de una lista 
frutas[0] = "mango"
print(frutas)
#%%
#Podemos alargar la lista sin importar el tamaño inicial
frutas[3:] = ["uva", "higo", "sandia", "pomelo"]
print(frutas)

#%%
#podemos evaluar si un elemento existe en una lista
print(frutas)
print("uva" in frutas)
#%%
print("patata" in frutas)
#%%
# Podemos buscar la posición de un elemento en una lista

frutas = [ "naranja", "manzana", "pera", "fresa"]

print(frutas)

print("Posicion en la lista de la palabra pera es {}".format(frutas.index("pera")))
#%%

# podemos eliminar un elemento en una posicion concreta con pop

a = frutas.pop(2)
print(frutas)
print(a)
#%%

# combinando index y pop podemos eliminar un elemento en concreto
frutas.pop(frutas.index("naranja"))
print(frutas)
#%%
# las listas se pueden ordenar con el método sort()

edades = [23, 33, 10,54,65,34,25]
edades.sort()
print(edades)

#%%
frutas = [ "naranja", "manzana", "pera", "fresa"]
print(frutas.sort())
print(frutas)
#%%
# Podemos generar listas de numeros con la función range()

#%% 
range(10)
#%%
print(list(range(15)))
#%%
# Los strings se pueden acceder de forma similar a las listas

nombre = "Murcia"

print(nombre[0])
print(nombre[2:])

#%%
"""
Podemos convertir listas a strings con .join
"""

frutas = [ "naranja", "manzana", "pera", "fresa"]
frutas_separadas_por_comas = ",".join(frutas)

print(frutas_separadas_por_comas)
print(type(frutas_separadas_por_comas))
#%%
frutas_separadas_por_lineas = "\n".join(frutas)

print("tenemos que comprar: {}".format(frutas_separadas_por_lineas))


#%%

























