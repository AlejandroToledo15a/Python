"""
Usamos los flujos de control para llevar un control de algún programa. Por ejemplo tenemos if, if-else. Los cuales nos ayudan a tomar una decisión y ejecutar distintas partes del código en función de una condición.

NOTA: En python la manera de indicar si estamos en un bucle (una función) es mediante el indentado, es decir poniendo 4 espacios delante del código. (En spyder pulsar la tecla del tabulador inserta los 4 espacios automáticamente)
"""
#%%
# Función IF.
temperatura = 15

if temperatura <= 20:
    print("Hace frío, ponte una chamarra!")
# Como temperatura no es menor o igual que 20, no imprime nada.
#%%
# Si queremos tomar distintas condiciones en función de una condición podemos 
# usar IF-ELSE

temperatura = 30.001

if temperatura <= 10:
    print("Hace mucho frío, te vas a congelar!")
elif 10 < temperatura <= 20:
    print("Puede que tengas frío, ponte una chamarra")
elif 20 < temperatura <= 30:
    print("Ya esta haciendo algo de calor, destapate!")
else: # else contempla todos los demás casos que no pusimos en elif
    print("Uy! estás que hierves, vamos a la playa")

#%%
# Podemos insertar otros ifs dentro de algún if.

temperatura = 25
lluvia = False

if 20 < temperatura < 30:
    if not lluvia:
        print ("El clima es bueno y no llueve, vamos de picnic")
#%%
# FOR. Los bucles FOR sirven para iterar entre los elementos de una lista uno por uno
# o de cualquier elemento de Python que soporte iteraciones.

numeros = list(range(11))
numeros.pop(0)
numeros

for numero in numeros:
    if numero <= 5:
        print(f"Como el número: {numero} es menor o igual que 5, es un número válido.")
    else:
        print(f"Como el número: {numero} es mayor que 5, es un número inválido.")

#%%
# Si queremos salir del bucle en cuanto la condición no se cumpla usamos un "break".

numeros = list(range(11))
numeros.pop(0)
numeros

for numero in numeros:
    if numero <= 5:
        print(f"Como el número: {numero} es menor o igual que 5, es un número válido.")
    else:
        print(f"Como el número: {numero} es mayor que 5, es un número inválido.")
        break

#%%
# Si en lugar de romper el código solo queremos pasar usamos "pass".
        
numeros = list(range(11))
numeros.pop(0)
numeros

for numero in numeros:
    if numero <= 5:
        print(f"Como el número: {numero} es menor o igual que 5, es un número válido.")
    else:
        print(f"Como el número: {numero} es mayor que 5, es un número inválido.")
        pass
#%%
# Una forma de simplificar las iteraciones de elementos de una lista es:

numeros = list(range(11))
numeros.pop(0)

[numero for numero in numeros if numero <= 5]

# Esta forma de usar FOR, nos puede ayudar a simploficar más nuestro código.
 
#%%
# Se pueden hacer fors para diccionarios.

frutas = {'manzana': 2,'pera':4,'piña':7,'aguacate':5}

for fruta in frutas:
    print(fruta)

#%%
for fruta, cantidad in frutas.items():
    print(f"Hay {cantidad} kilos de {fruta}")
#%%
for fruta, cantidad in frutas.items():
    print("Hay {} kilos de {}".format(cantidad,fruta))
#%%
# FOR para strings
    
nombre = 'Alejandro'

for letra in nombre:
    print(f'Dame una {letra}')
#%%
    
"""
TRY-EXCEPT

En ocaciones los programas fallan arrojando una excepción, pero una manera de hacer que 
nuestro programa continúe su funcionamiento pese haber fallado es 'atrapando' la 
excepción. En python lo podemos hacer mediante el bloque TRY-EXCEPT.

IMPORTANTE: Siempre que encontremo una excepción, es importante por lo menos imprimir el
mensaje de error. Así nos aseguramos que nuestro programa no esta fallando 
catastróficamente sin que nos demos cuenta.
"""

numero_str = "10.5"

try:
    numero_int = int(numero_str)
except Exception as e:
    print(f'Error, el número {numero_str} no se puede convertir a entero.')
    print(f'El mensaje de error es {type(e)} tal que {e}')
#%%
numero_str = "10.5"

try:
    numero_int = int(numero_str)
except Exception as e:
    print('Error, el número {} no se puede convertir a entero.'.format(numero_str))
    print('El mensaje de error es {} tal que {}'.format(type(e),e))
#%%
    
numero_str = "10.5"

try:
    numero_int = int(numero_str)
except Exception as e:
    print(f'Error, el número {numero_str} no se puede convertir a entero.')
    print('El error ha sido: ')
    print(e,type(e))
#%%
"""
WHILE
El bucle while siguen ejecutando mientras una condición sigue ocurriendo.
"""

elefante = 5

while elefante <= 10:
    print(f'{elefante} se columpiaban, sobre la tela de una araña..')
    elefante += 1

#%%
# loop infinito.
    
while 1>0:
    print('atascado en el loop')
#%%
# Ejercicio 1.

while 1:
    input_usuario = input('Hola, dame un número entre el 1 y el 10. Escribe "exit" para salir: ')
    try:
        if input_usuario == "exit":
            print("Adios!")
            break
        elif 1 <= int(input_usuario) <= 10:
            cuadrado = int(input_usuario)**2
            print(f"El cuadrado de {input_usuario} es: {cuadrado}")
        else:
            print(f"El número {input_usuario} no esta en el intervalo.")
    except ValueError:
        print(f"Error, el valor {input_usuario} que diste no se puede convertir a entero")

#%%
# Ejercicio 2 y 3.

dias = {'lunes':1,'martes':2,'miercoles':3,'jueves':4,'viernes':5,'sabado':6,'domingo':7}
dias
#%%
# Crea una lista con los días que contengan la letra 'o'.
nuevo = [] # primero creo una lista vacía

for dia in dias.keys():
    if 'o' in dia:
        nuevo.append(dia)
    else:
        pass        

nuevo
#%%
# Dado dicho diccionario, convertir todas las claves a mayúsculas.

dias_mayus = {} # creamos un directorio vacío.

for clave, valor in dias.items():
    dias_mayus[clave.upper()] = valor

dias_mayus