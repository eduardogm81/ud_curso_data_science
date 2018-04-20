# -*- coding: utf-8 -*-
"""
******************************************************************************

EJERCICIOS

******************************************************************************
"""

#%%
"""
 Crear un diccionario cuyas claves sean los tres primeros dias de la semana y los 
 valores sean la posicion en la semana de dicho dia
"""
(1)
#%%
"""
 De dicho diccionario, convertir todas las claves a mayúsculas
"""
(2)

#%%
semana = {
        "lunes": 1,
        "martes": 1,
        "miercoles": 1
        }
print(semana)
#%%
# Convertir claves a mayusculas
for key in semana.keys():        
    semana[key.upper()] = semana.pop(key)
    
#%%
print(semana)