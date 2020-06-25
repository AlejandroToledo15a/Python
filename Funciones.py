"""
FUNCIONES.

Las funciones son formas de separar la lógica en piezas sin tener que ejecutarlas linea a
linea, y además permitir reutilizar partes del código que se repitan.
"""

#%%
def saludar():
    print('Hola mundo')
    
saludar()
#%%
def saludar(nombre):
    print(f'Hola {nombre}, cómo estás?')
    
saludar('Alejandro')
#%%
# Podemos crear una función con una función adentro. En este ejemplo si nosotros dejamos
# la funcion saludar_amigo en blanco nos arroja el amigo dentro de la otra función. 
def saludar_amigo(nombre = 'amigo'):
    saludar(nombre)
    
saludar_amigo('Carlos')
#%%
def suma(a,b):
    return a+b
    # lo que se escribe después de un return no se toma en cuenta.

suma(5,50)
#%%
def suma_resta(a,b):
    suma = a+b
    resta = a-b
    return suma, resta

suma_resta(10,4)
#%%
res_suma, res_resta = suma_resta(10,4)
res_suma
#%%
res_resta
#%%
"""
Existe otra forma de definir funciones, las llamadas funciones lamda o anónimas.

La sintaxis es:
    
    nombre_de_la_funcion_lambda = lambda  input : output
    
Estas funciones se realizan cuando queremos aplicar lógica sencilla, para lo cual definir
una función 'oficial' no es necesario.
"""

sum_lambda = lambda a,b : a+b

sum_lambda(4,4)
#%%
# Ejercicios.

# Crear una función que le pasemos un string y lo convierta a minusculas.

def minusculas(palabra):
    return palabra.lower()

minusculas('MARCOS')
#%%
minusculas_lambda = lambda palabra : palabra.lower()

minusculas_lambda('QUIERO UN ELOTE')
#%%
# Una función que acepte 3 argumentos, 2 números y un string. Si el string es suma realiza
# la suma entre los números, si es resta realiza la resta entre los números.

def suma_o_resta(a,b,decision):
    if decision == 'suma':
        resultado = a+b
    elif decision == 'resta':
        resultado = a-b
    else:
        resultado = 'Ingresaste mal algo'
    return resultado

suma_o_resta(30,23,'suma')    
#%%
# Crear una función que le pida una oración al usuario y regrese dicha oración al revés.
# Por ejemplo si escribe 'Hola mundo enorme', regrese 'enorme mundo hola'.

def oracion(cadena):
    return cadena[::-1]

oracion('Hoy tengo ganas de estudiar')
#%%
def otra_forma(cadena_texto):
    otro = cadena_texto.split() # split separa cadenas de texto y los convierte en listas.
    cadena_invertida = []
    for letra in otro:
        cadena_invertida.append(letra)
    return ' '.join(cadena_invertida[::-1])

otra_forma('Hola soy Alejandro Toledo')
#%%
def otra_otra(cadenita):
    cadenita_invertida = []
    for letrita in cadenita.split():
        cadenita_invertida.append(letrita)
    return ' '.join(cadenita_invertida[::-1])

otra_otra('hola amigos que me cuentan')
#%%
def mejorado(cad):
    cade = cad.split()
    return ' '.join(cade[::-1])

mejorado('hola amigos que me cuentan')
#%%
ejemplo = 'hola como estan'
ejemplo.split('a') # separa la cadena cuando hay una 'a'
#%%
# Crear una función que detecte si una palabra o frase es un palindromo, es decir si
# dicha palabra o frase se lee de igual forma de un sentido o del otro.

def palindromo(frase):
    n_frase = frase.replace(' ','')
    aux = 0
    for i in range(len(n_frase)):
        if n_frase[i] == n_frase[::-1][i]:
            aux = 1 + aux
        else:
            pass
    if aux == len(n_frase):
        print('Es un palindromo')
    else:
        print('No es un palindromo')

palindromo('ana la lana')
#%%
"""
Crear una función que dada una lista de listas, nos devuelva una lista simple. (Es decir
sin ninguna lista dentro). 

Por ejemplo:
lista = [[1,2,3],[4,5,6,7],[8,9]] 

la función nos de:
lista = [1,2,3,4,5,6,7,8,9]
"""
#%%
def lista_simp(granlista):
    n_lista = []
    for i in range(len(granlista)):
        for j in granlista[i]:
            n_lista.append(j)
    return n_lista
#%%
listita = [[1,2,3],[4,5,6,7],[8,9],[10],[11,12,13,14]]

lista_simp(listita)