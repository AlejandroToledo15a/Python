
"""
CLASES.
Python es un lenguaje orientado a objetos. ¿Esto que significa? Pues que pese a que podamos
programar de forma funcional, esto es simplemente enviando datos a través de funciones,
muchas de las ventajas de Python están en su uso de clases.

Las clases en Python se definen de la forma:
    
class Clase:
    def metodo1(self): --> TODOS LOS ELEMENTOS DE CLASE TOMAN 'self' COMO PRIMER ARGUMENTO
        # Método que tienen los objetos de la clase
    
    def metodo2(self): 
        # Otro método que tienen los objetos de la clase
    
"""
#%%
# Creamos una clase básica llamada coche.

class CocheBasico:
    def girar_izquierda(self):
        print('Girando a la izquierda')
    def girar_derecha(self):
        print('Girando a la derecha')
    def acelerar(self):
        # podemos usar pass si queremos que la función no haga nada
        pass
    def frenar(self):
        pass
    
print(CocheBasico)
#%%
"""
Hemos generado la clase CocheBasico. Las clases se pueden considerar como plantillas que 
se pueden usar para generar objetos. Por ejemplo la plantilla (clase) CocheBasico nos da 
instrucciones para fabricar un Coche.

En jerarga de desarrollo se llama 'instanciar una clase', es decir creamos una instancia
(objeto) de la clase coche.
"""

coche_manuel = CocheBasico()
print(coche_manuel)
#%%
# el objeto coche_manuel es un CocheBasico, es decir, es un objeto de la clase CocheBasico 
print(type(coche_manuel) == CocheBasico())
#%%
# éste objeto también tiene todas las cararacterísticas de la clase CocheBasico
coche_manuel.girar_derecha()
coche_manuel.girar_izquierda()
coche_manuel.acelerar() # esto no hace nada
#%%
"""
Al igual que las funciones, generalmente queremos que los objetos que creemos tengan unas
características definidas de forma variable. 

Con la clase CocheBasico todos los objetos que creemos serán 100% iguales. ¿Cómo podríamos
generar coches (objetos) que tengan distinto color?

Para esto podemos usar el método especial __init__ que se ejecuta cuando se crea el 
objeto de una clase.
"""

class CocheConColor:
    def __init__(self, color):
        self.color = color # éste es un atributo
    def describir(self):
        print('Este coche es de color: {}'.format(self.color))
    def girar_izquierda(self):
        print('Girando a la izquierda')
    def girar_derecha(self):
        print('Girando a la derecha')
    def acelerar(self):
        # podemos usar pass si queremos que la función no haga nada
        pass
    def frenar(self):
        pass
#%%
# creemos un objeto (coche) de color rojo..

coche_rojo = CocheConColor(color = 'rojo')
coche_rojo.describir()
coche_rojo.color
#%%
# también podemos añadir atributos a los objetos

coche_rojo.matricula = '868-NRG'
coche_rojo.matricula
#%%
# para crear un objeto de esta clase debemos definir el color, si no aparece un error
coche_sin_color = CocheConColor()
#%%
# podemos evitar esto si definimos el color desde que definimos la clase
class CocheConColor:
    def __init__(self, color = 'negro'):
        self.color = color # éste es un atributo
    def describir(self):
        print('Este coche es de color: {}'.format(self.color))
    def girar_izquierda(self):
        print('Girando a la izquierda')
    def girar_derecha(self):
        print('Girando a la derecha')
    def acelerar(self):
        # podemos usar pass si queremos que la función no haga nada
        pass
    def frenar(self):
        pass
#%%
coche_sin_color = CocheConColor()
coche_sin_color.color
#%%
coche_sin_color.describir()
#%%
# también podemos definir una clase con muchas variables 

class CocheVariables:
    def __init__(self, color, modelo, velocidad_maxima):
        self.color = color # éste es un atributo
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0 # la velocidad inicial es cero
    def describir(self):
        print('Este coche es de color {} y es un modelo {} cuya velocidad máxima es {}.'.format(self.color,self.modelo,self.velocidad_maxima))
    def describir_estado(self):
        if self.velocidad == 0:
            print('El coche esta parado')
        else:
            print('El coche va a: {} kilometros por hora'.format(self.velocidad))
    def girar_izquierda(self):
        print('Girando a la izquierda')
    def girar_derecha(self):
        print('Girando a la derecha')
    def acelerar(self):
        # podemos usar pass si queremos que la función no haga nada
        pass
    def frenar(self):
        pass
#%%
coche_alejandro = CocheVariables(color='rojo',modelo='Cavalier 2000',velocidad_maxima=200)
coche_alejandro.describir()
coche_alejandro.describir_estado()
#%%

class Vehiculo:
    
    def __init__(self, color, modelo, velocidad_maxima):
        self.color = color # éste es un atributo
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0 # la velocidad inicial es cero
        
    def describir(self):
        print('Este coche es de color {} y es un modelo {} cuya velocidad máxima es {}.'.format(self.color,self.modelo,self.velocidad_maxima))
    
    # __repr__ nos ayuda cuando queremos representar algo con el método print
    def __repr__(self):
        return self.describir()
        
    def describir_estado(self):
        if self.velocidad == 0:
            print('El coche esta parado')
        elif self.velocidad > 0:
            print('El coche va a: {} kilometros por hora'.format(self.velocidad))
        else:
            print('El vehículo va marcha atrás a {} km/h'.format(self.velocidad))
            
    def girar_izquierda(self):
        print('Girando a la izquierda')
        
    def girar_derecha(self):
        print('Girando a la derecha')
        
    def acelerar(self,diferencia_velocidad):
        print('Acelerando {} km/h'.format(diferencia_velocidad))
        self.velocidad += abs(diferencia_velocidad)
        self.velocidad = min(self.velocidad_maxima,self.velocidad)
        
    def frenar(self,diferencia_velocidad):
        print('Frenando {} km/h'.format(diferencia_velocidad))
        self.velocidad -= abs(diferencia_velocidad)
        self.velocidad = max(self.velocidad,-5)
        
#%%
coche_alejandro = Vehiculo(color='rojo',modelo='Cavalier 2000',velocidad_maxima=200)
#%%
coche_alejandro.describir()
coche_alejandro.describir_estado()
#%%
coche_alejandro.frenar(50)
#%%
coche_alejandro.describir_estado()
#%%
coche_alejandro.acelerar(100)
#%%
"""
Herencia de Clases.

Una de las principales ventajas de usar clases es que se pueden crear clases usando
como plantillas otras clases (se dice que una clase 'hereda' de otra).

Esto nos permite crear una clase BASE con funcionalidades genéricas que todas las demás
tendrán en común. Así las nuevas clases serán más avanzadas con funcionalidades más
específicas.

Por ejemplo creemos una clase autobus, que no tiene marcha atrás y tiene un limite
de velocidad de 100 km/h.
"""
#%%

class AutoBus(Vehiculo):
    def acelerar(self,diferencia_velocidad):
        print('Autobus acelerando {} km/h'.format(diferencia_velocidad))
        self.velocidad += abs(diferencia_velocidad)
        self.velocidad = min(self.velocidad,100)
        
    def frenar(self,diferencia_velocidad):
        print('Autobus frenando {} km/h'.format(diferencia_velocidad))
        self.velocidad -= abs(diferencia_velocidad)
        self.velocidad = max(self.velocidad,0)
#%%
autobus_escolar = AutoBus(color='amarillo',modelo='Escolar 2020',velocidad_maxima=100)
#%%
autobus_escolar.describir()
autobus_escolar.describir_estado()
autobus_escolar.acelerar(40)
#%%
autobus_escolar.describir_estado()
#%%
autobus_escolar.frenar(30)
#%%
"""
Crear una clase Taxi que herede de Vehículo, y que pueda cobrarnos un trayecto. Tiene que
tener un atributo 'distancia recorrida' y tres métodos adicionales:
    - método 'cobrar', donde se imprime la cantidad a cobrar (3 euros por kilometro)
    - método 'añadir_distancia', donde se suma a la distancia recorrida un número de 
      kilometros
    - método 'añadir_tiempo', donde dado un tiempo en horas se añade distancia en función
      de la velocidad.
"""
#%%

class Taxi(Vehiculo):
    def __init__(self,modelo,velocidad_maxima):
        self.color = 'Rojo con dorado'
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0
        self.tiempo = 0
        self.distancia_recorrida = 0
        self.tarifa = 3
        
    def añadir_distancia(self,kilometros):
        self.distancia_recorrida += kilometros
        print('Vamos a recorrer {} kilometros'.format(kilometros))
        
    def añadir_tiempo(self,tiempo):
        self.añadir_distancia(tiempo*self.velocidad)
        print('Vamos a una velocidad de {} km/h y tardaremos {} horas en llegar'.format(self.velocidad,tiempo))
        
    def cobrar(self):
        print('Son {} euros por todo el recorrido'.format(self.tarifa*self.distancia_recorrida))
        
#%%
taxi_a_insurgentes = Taxi(modelo='Tsuru',velocidad_maxima=150)
#%%
taxi_a_insurgentes.acelerar(100)
#%%
taxi_a_insurgentes.describir_estado()
#%%
taxi_a_insurgentes.añadir_tiempo(2)
#%%
taxi_a_insurgentes.cobrar()
#%%
taxi_a_periferico = Taxi(modelo='Tsuru',velocidad_maxima=150)
#%%
# en este otro caso tenemos que añadimos la distancia directamente, más no aceleramos..
# por lo que la tarifa solo será la distancia del recorrido por la tarifa
taxi_a_periferico.añadir_distancia(52)
#%%
taxi_a_periferico.cobrar()
#%%
# otra forma más fácil de hacer una clase es la siguiente:
class Taxi2(Vehiculo):
    def __init__(self,tarifa, *args, **kwargs):
        super().__init__(*args,**kwargs) # de esta forma no necesitamos agregar todos los
        self.distancia_recorrida = 0     # parámetros de vehículo, solo añadimos los nuevos
        self.tarifa = tarifa
        
    def añadir_distancia(self,kilometros):
        self.distancia_recorrida += kilometros
        print('Vamos a recorrer {} kilometros'.format(kilometros))
        
    def añadir_tiempo(self,tiempo):
        self.añadir_distancia(tiempo*self.velocidad)
        print('Vamos a una velocidad de {} km/h y tardaremos {} horas en llegar'.format(self.velocidad,tiempo))
        
    def cobrar(self):
        print('Son {} euros por todo el recorrido'.format(self.tarifa*self.distancia_recorrida))
#%%
nuevo_viaje = Taxi2(tarifa=2,color='blanco',modelo='tsuru',velocidad_maxima=120)
#%%
nuevo_viaje.acelerar(91)
#%%
nuevo_viaje.describir_estado()
#%%
nuevo_viaje.añadir_tiempo(1)
#%%
nuevo_viaje.cobrar()
#%%
"""
Crear una clase parking, donde se pueda aparcar un limite determinado de vehículos, y donde
se pueda validar si un vehículo está aparcado o no.
"""

class Parking:
    def __init__(self,capacidad):
        self.capacidad = capacidad
        self.vehiculos = []
        
    def lugares_disponibles(self):
        if not len(self.vehiculos) < self.capacidad:
            return 1
        
    def aparcar(self,n_carro):
        if len(self.vehiculos) < self.capacidad:
            if not n_carro in self.vehiculos:
                self.vehiculos.append(n_carro)
                print('Aparcando {}'.format(n_carro))
                return self.vehiculos
            else:
                print('Este carro ya esta aparcado en el estacionamiento')
        else:
            print('Ya no hay capacidad en el estacionamiento')
            
    def sacar_carro(self,n_carro):
        if n_carro in self.vehiculos:
            self.vehiculos.pop(self.vehiculos.index(n_carro))
            return self.vehiculos
        else:
            print('Este carro no esta aparcado')

#%%
estacionamiento = Parking(capacidad=3)
#%%
estacionamiento.aparcar('carro1')
#%%
estacionamiento.aparcar('carro2')
#%%
estacionamiento.aparcar('carro3')
#%%
estacionamiento.sacar_carro('carro1')

# %%
