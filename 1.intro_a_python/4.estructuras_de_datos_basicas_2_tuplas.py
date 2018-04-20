# -*- coding: utf-8 -*-

"""
*******************************************************************************
TUPLAS  (TUPLES)
*******************************************************************************

Las tuplas son versiones de las listas que no se pueden modificar.

"""
mosqueteros = ("Athos", "Porthos", "Aramis")
print(type(mosqueteros))
print(mosqueteros)

#%%
#podemos acceder a los elementos de una tupla de igual forma que a una lista
print(mosqueteros[1:])

#%%
# sin embargo, no podemos modificarla
mosqueteros[3] = "D'artagnan"

#%%