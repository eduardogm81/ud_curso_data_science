# -*- coding: utf-8 -*-
"""
python tiene muchos tipos de variables básicas que forman parte del núcleo del
lenguaje, son lo que se llama primitivas. 
"""

"""Las primitivas más comunes son strings, numeros, booleanos"""

"""
*******************************************************************************
STRINGS
*******************************************************************************
"""
#%%
print("Se usan para definir un texto")
#%%
var_str = "Hola!"
var_str2 = "Mundo!"

print(var_str, var_str2)

print(type(var_str))
print(type(var_str2))
#%%
"""
los strings se pueden unir para formar strings más largos. Hay varias 
maneras de unir strings (lo que se llama interpolación de strings)
"""
# Podemos usar el simbolo + para "sumar" (concatenar) strings
var_str_unido = var_str + " " + var_str2
print(var_str_unido)
#%%
# También podemos multiplicar strings
n = "monja"
print(n * 10)
#%%
"""
Tambien podemos usar el método format, que nos permite insertar unos  strings
dentro de otros
"""
nombre = "Eduardo"
ciudad = "Madrid"
# presentacion = "Hola me llamo {}, soy de {}".format(nombre, ciudad)
# print(presentacion)
presentacion = "Hola me llamo {}, soy de {}"
print(presentacion.format(nombre, ciudad))
#%%
nombre2 = "María"
ciudad2 = "Barcelona"

print(presentacion.format(nombre2, ciudad2))
#%%
"""
Python es un lenguaje con "pilas incluidas" , esto quiere decir que tiene
un montón de funcionalidades incluidas con la instalación básica de Python.

Dichas funcionalidades se agrupan en módulos o paquetes y podemos usarlas 
con la palabra import

Por ejemplo, si queremos hacer uso del módulo de python encargado de operaciones 
matemáticas, escribimos "import math" (importamos el módulo math)
"""
import math

print (math.pi)

#%%
# Usando el metodo format se puede indicar como formatear las variables
# Por ejemplo, redondear números decimales.
pi_str = "Los primeros dígitos de pi son {}".format(math.pi)
print(pi_str)
#%%
# podemos restringir que se imprima pi con 2 decimales
pi_str = "Los primeros dígitos de pi son {:.2f}".format(math.pi)
print(pi_str)
#%%
#Si pasamos 0 decimales hemos redondeado a un entero
pi_str = "Los primeros dígitos de pi son {:.0f}".format(math.pi)
print(pi_str)
#%%
"""otra manera de usar interpolación de strings (solo disponible en python 3.6 
en adelante) es referenciar directamente las variables en el string convirtiendolo
en un f-string (se convierte un string poniendole la letra f delante)
"""
presentacion2 = f"Hola, me llamo {nombre} y soy de {ciudad}"
print(presentacion2)
#%%
"""
Más OPERACIONES CON STRINGS
"""
titulo = "introducción a PYTHON"
print("Convertimos un string en mayúsculas con upper")
print(titulo.upper())
print("Convertimos un string en minúsculas con lower")
print(titulo.lower())
print("Ponemos la primera letra en mayúscula con capitalize")
print(titulo.capitalize())
#%%
nombre_con_comas = ",ma,nuel,"
# nombre_con_comas = ",manuel,"
print("Usamos strip pra eliminar caracteres al inicio y al final de un string")
print(nombre_con_comas.strip(","))
print("Usamos replace para reemplazar partes de un string por otras")
print(nombre_con_comas.replace("nuel", "riano"))
print("Todos los métodos se pueden encadenar")
print(nombre_con_comas.strip(",").replace("nuel", "riano"))
#%%
# Se puede separar un string en múltiples usando el método split()
colores_str = "rojo|amarillo|verde|azul"
colores_lista = colores_str.split("|")
print(colores_lista)
#%%
#%%
#%%

























