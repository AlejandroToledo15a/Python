# Nuestro primer Hola mundo
print("Hola mundo")
#%%
# Así declaramos variables
a = 11
b = 5

# Realizamos operaciones de la siguiente forma
suma = a+b
print("La suma es:" + str(suma))
resta = a-b
print("La resta es:" + str(resta))
multiplicacion = a*b
print("La multiplicación es:" + str(multiplicacion))
division = a/b
print("La división es:" + str(division))

print(f"El multiplo inferior entre a y b 'a//b' es: ", a//b) 
print(f"El modulo entre a y b es: ", a%b)
print(f"a a la b es: ", a**b)

# Celdas en spyder, nos permite ejecutar una parte de código presionando control + enter
#%%
print("La suma es:" + str(suma))
print("La resta es:" + str(resta))
#%%
# Tipos de variables
var_str = "Hola"
var_str2 = "mundo"
type(var_str)
# Nos permite concatenar dos strings
print(var_str, var_str2)
print(var_str + " " + var_str2)
#%%
# Multiplicar strings
n = "Hola mundo!"
print(n * 2)
#%%
#format, nos permite insertar strings dentro de otros strings 
nombre = "Alejandro"
ciudad = "Ciudad de México"
presentacion = "Hola, soy {} y vengo de {}."
print(presentacion.format(nombre,ciudad))
#%%
import math
print(math.pi)
#%%
pi_str = "los primeros dígitos de PI son: {:.2f}".format(math.pi)
print(pi_str)
#%%
titulo = "introducción a Python"
print(titulo.upper())
print(titulo.lower())
print(titulo.capitalize())
#%%
nombre = ",alejandro,"
print(nombre.strip(",")) #quita elementos extremos
print(nombre.replace("dro","drino"))
print(nombre.strip(",").replace("dro","drino"))
#%%
colores = "rojo|verde|rosa"
print(colores.split("|"))
print(type(colores.split("|")))
#%%
nombre = "Alejandro"
ciudad = "Ciudad de México"
edad = 23
print(f"Hola, me llamo {nombre} y soy de {ciudad}. Tengo {edad} años.")
#%%
# Comparaciones lógicas
a = 7
b = 2
print(f"a > b ", a > b)
print(f"a <= b", a <= b)
print(f"a == 2", a == 2)
print(f"b != 8", b != 8)
#%%
print(f"a > b and b != 8", a > b and b != 8)
print(f"a > b and b != 8", a > b and b != 2) 


