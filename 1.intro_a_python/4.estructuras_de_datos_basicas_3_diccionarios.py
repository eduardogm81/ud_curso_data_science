# -*- coding: utf-8 -*-

"""
*******************************************************************************
Diccionarios
*******************************************************************************

Los diccionarios son un conjunto de claves (keys) asociadas a valores (values).
Sabiendo una clave podemos encontrar el valor de dicha clave
"""

inventario = {
        "melocotones": 3,
        "fresas": 1,
        "manzanas": 4
        }
print(type(inventario))
print(inventario)
#%%

#podemos ver las claves que tiene un diccionario con el metodo keys()
print(inventario.keys())


#%%
#el metodo .keys() no devuelve una lista, si queremos acceder las claves como 
# una lista tenemos que convertirlas a una
print(inventario.keys()[0]) # Esto daría un error
#%%
print(list(inventario.keys())[0])

#%%
# podemos ver los valores de un diccionario con el metodo values()
print(inventario.values())
#%%
#Accedemos a los elementos de un diccionario con []
print(inventario["fresas"])
#%%
#Si la clave buscada no existe nos dará un error KeyError)
print(inventario["melon"])
#%%
#podemos evaluar si una clave existe en un diccionario facilmente
print("melon" in inventario)
print("melocotones" in inventario)

#%%
#Podemos eliminar una clave en un diccionario con pop()

kilos_fresas = inventario.pop("fresas")
print("Tenemos {} kilos de fresas".format(kilos_fresas))
print(inventario)

#%%
# Cada tipo de estructura de datos puede almacenar los otros!

#una lista con listas dentro
lista_trayectos =[
        ["Murcia", "Valencia"],
        ["Murcia", "Alicante"],
        ["Albacete", "Valencia"],
        ["Albacete", "Granada"]
        ] 

print(lista_trayectos[1][1])
#%%
#un diccionario con tuplas como valores
dict_trayectos = {
        "Murcia": ("Valencia", "Alicante"),
        "Albacete": ("Valencia", "Granada")
        }


print(dict_trayectos["Murcia"])

#%%
# Una lista que contiene diccionarios
lista_diccionarios = [
        {"origen": "Murcia", "destino": "Alicante"},
        {"origen": "Albacete", "destino": "Granada"}
        ]
#%%
"""