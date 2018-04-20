# -*- coding: utf-8 -*-
"""
*******************************************************************************
NÚMEROS
*******************************************************************************
"""
print("hay dos tipos básicos de primitivas numéricas en python, int(enteros) y float(decimales)")

entero = 23
print(type(entero))

#%%
decimal = 23.1
print(type(decimal))

#%%
print(type(23.))

#%%
print("podemos convertir números a strings fácilmente")
print(type(str(entero)))
print("dos + " + str(decimal))
#%%
print("Tambien podemos usar numeros en interpolacion de strings")
nombre = "Manuel"
ciudad = "Murcia"
edad = 33
print(f"Hola, me llamo {nombre}, soy de {ciudad} y tengo {edad} años")
#%%
print("de igual forma, podemos convertir strings a números")
numero_string = "24"
print(int(numero_string) + 5)
print(float(numero_string) + 5)
#%%
print("Hay que asegurarse de que sean números válidos!")
numero_string_invalido = "24,5"
print(float(numero_string_invalido))
#%%
print("de igual forma, no podemos convertir un string float a un entero")
print(int("24.1"))
#%%
"""
OPERACIONES NUMERICAS


Podemos usar los simbolos basicos de aritmetica para realizar operaciones
"""
#suma
print("2+2=",2+2)
#resta
print("4-9=",4-9)
#multiplicacion
print("3*2=",3*2)
#division
print("7/2=",7/2)
#%%
"""
Aparte, tenemos más operaciones que podemos hacer
"""
a = 7
b = 2
# multiplo inferior, realizar la division eliminando el resto
print(f"{a}//{b}=", a//b)
# modulo, realizar una division y quedarse solo con el resto
print(f"{a}%{b}=", a%b)
#negacion, cambiar de sentido un valor
print(f"negacion de {a}=", -a)
#potencias, elevar al cuadrado, al cubo, etcétera
print(f"{a}**{b}=",a**b)
#%%
#%%
#%%

























