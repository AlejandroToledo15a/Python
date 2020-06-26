"""
Las estructuras de datos son aquellos objetos que se usan para almacenar información. Hay muchos tipos, estos son los básicos.
"""
# Listas, son conjuntos de elementos ordenados donde cada elemento tiene una posición.
# Las estructuras de datos son aquellos objetos que se usan para almacenar información. Hay muchos tipos, estos son los básicos.
# Listas, son conjuntos de elementos ordenados donde cada elemento tiene una posición.

#%%
frutas = ["naranja","manzana","pera","fresa","coco","platano"]
print(frutas)
type(frutas)
#%%
# Accedemos a los elementos de una lsita con []
# El indíce de los elementos de una lsita empieza en 0, eso quiere decir que accedemos al 
# primer elemento con [0].
frutas[0]
print(frutas[0])
#%%
# Accedemos a los elementos desde el primero hasta el tercero.
frutas[:3]
#%%
# Accedemos a los elementos desde el tercero hasta el final.
frutas[2:]
#%%
# Accedemos a los últimos 2 elementos de una lista.
frutas[-2:]
#%%
# Accedemos a los elementos inpares.
frutas[::2]
#%%
# Accedemos a los elementos pares.
frutas[1::2]
#%%
# Escribe la lista al revés.
frutas[::-1]
#%%
# Nos ayuda a ver la longitud de una lista.
len(frutas)
#%%
# Añadimos elementos a una lista con la función append.
frutas.append("melon")
frutas
#%%
# Podemos repetir una lista multiplicando por un entero.
frutas*2
#%%
# Podemos concater listas con el simbolo más.
ciudades = ["Roma","Barcelona"]
lista = ciudades + frutas
lista
#%%
# Podemos modificar elementos de una lista.
frutas[0] = "mando"
frutas
#%%
# Podemos modificar rangos de una lista.
frutas[3:] = ["uva","guayaba","sandía","higo","aguacate"]
frutas
#%%
# Podemos evaluar si un elemento esta en una lista.
'uva' in frutas
#%%
'patata' in frutas
#%%
# Nos devuelve la posición de un elemento en una lista.
frutas.index("manzana")
#%%
# Nos elimina un elemento de una lista en una posición en específico.
frutas.pop(7)
frutas
#%%
# Podemos eliminar un elemento sin saber su posición.
frutas.pop(frutas.index('pera'))
frutas
#%%
# Podemos ordenar una lista de forma ascendente.
numeros = [1,12,3,44,40,12,0,1,40]
numeros
#%%
numeros.sort()
numeros
#%%
# Nos permite crear una lista de números consecutivos.
nuevo = range(10)
list(nuevo)
#%%

# Strings. Podemos jugador con las letras o caracteres de algún string.

nombre = "Manuel"
nombre[0]
nombre[2:]
#%%

# Tuples. Son versiones de listas que no se pueden modificar.

mosqueteros = ("Athos","Porthos","Aramis")
type(mosqueteros)
#%%
mosqueteros[0] = "da un error"
#%%

# Diccionarios. Son un conjunto de claves (key), asociadas a valores (values). Sabiendo 
# una clave podemos encontrar el valor de dicha clave. 
inventario = {"uva":3,"pera":1,"manzana":2}
#%%
inventario
#%%
type(inventario)
#%%
inventario.keys()
#%%
inventario.values()
#%%

# Listas de listas.

dos_listas = [
              ["Murcia","Valencia"],
              ["Barcelona","Madrid"],
              ["Milán","Roma"]
              ]
dos_listas
#%%

# Ejercicios.
# Crear un diccionario cuyas claves sean los tres primeros días de la semana y los 
# valores sean la posición en la semana de dicho día.

dias_semana = {"lunes":1,"martes":2,"miercoles":3}

#%%
# Convertir los días de la semana a mayúsculas.
dias_semana["LUNES"] = dias_semana.pop("lunes")
dias_semana["MARTES"] = dias_semana.pop("martes")
dias_semana["MIERCOLES"] = dias_semana.pop("miercoles")
#%%
dias_semana

# %%