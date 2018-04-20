# -*- coding: utf-8 -*-

"""
*******************************************************************************
BOOLEANOS
*******************************************************************************

Una variable booleana es aquella que solo puede ser verdadera o falsa
"""

verdadero = True
falso = False

print(type(verdadero))


#%%
"""
Como tipo de primitiva especial, tenemos None, que es la variable nula.
"""

nulo = None
print(type(nulo))

#%%

# cualquier tipo de variable se puede convertir a booleano, transformandose en True
print(bool("patata"))

#%%
print(bool(""))
#%%
# 0 se transforma en False
print(bool(0))
#%%
print(bool(1))
#%%
#salvo None que se convierte a False
print(bool(nulo))
#%%
"""
COMPARACIONES LÓGICAS

Podemos hacer comparaciones entre variables, el resultado de estas comparaciones 
siempre es una variable booleana
"""

a = 7
b = 2
# a mayor o igual a b
print(f"{a} > {b}", a > b)
# b menor o igual a a
print(f"{b}<={a}", b<=a)
# b es igual a 2
print(f"{b}==2", b == 2)
# a es distinto a 23
print(f"{a}!=23",a != 23)
#%%

#podemos obtener el opuesto de un resultado logico con not
print(f"not {a}!=23",not a != 23)
#%%

# podemos evaluar que varias condiciones se cumplen con and
print(f"{a}!=23 and {a}<{b}=",a != 23 and a < b)
#podemos usar or para evaluar si se cumple una condicion u otra
print(f"{a}!=23 or {b}<{a}=",a != 23 or a < b)

#%%

"""
para comparar si algo es verdadero o falso, no usamos '==', sino que usamos 'is'
"""

print("verdadero is True=", verdadero is True)