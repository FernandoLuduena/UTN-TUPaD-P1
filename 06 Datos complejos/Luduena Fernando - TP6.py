#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Ejercicio 3
precios_frutas = {'Banana', 'Anana', 'Melon', 'Uva', 'Naranja', 'Manzana','Pera'}
print(precios_frutas)

#Ejercicio 4 

class Persona:

    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad
    
    def saludar(nombre, pais, edad):
        print(f"¡Hola! Soy {nombre}, vivo en {pais} y tengo {edad} años.")

#Ejercicio 5

from math import pi, pow    
class Circulo:

    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(radio):
        area = pi * pow(radio, 2)
        return area 

    def calcular_perimetro(radio):
        perimetro = 2 * pi * radio
        return perimetro

#Ejercicio 6

class Pila:
    
    def __init__(self, elemento):
        self.elementos = [] 
    
    def apilar(self, elemento):
        self.elementos.append(elemento)
        
    def desapilar(self,elemento):
        return self.elementos.pop() if not self.esta_vacia() else "La pila está vacía"
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def ver_tope(self):
        return self.elementos[-1] if not self.esta_vacia() else "La pila está vacía"
    
def balanceado(cadena):
    pila = Pila()
    pares = {')': '(', '}': '{', ']': '['}
    
    for caracter in cadena:
        if caracter in pares.values():
            pila.apilar(caracter)
        elif caracter in pares.keys(): 
            if pila.esta_vacia() or pila.ver_tope() != pares[caracter]:
                return False
            pila.desapilar()
    
    return pila.esta_vacia()

print(balanceado("({[]})")) 
print(balanceado("({[})"))   
print(balanceado("[{()}]"))  
print(balanceado("{(])}"))

#Ejercicio 7

from collections import deque

class Cola:
    def __init__(self):
        self.clientes = deque()

    def encolar(self, cliente):
        self.clientes.append(cliente)
        print(f"{cliente} ha sido agregado a la cola.")

    def desencolar(self):
        if not self.esta_vacia():
            cliente_atendido = self.clientes.popleft()
            print(f"{cliente_atendido} está siendo atendido.")
            return cliente_atendido
        else:
            return "No hay clientes en la cola."

    def siguiente_cliente(self):
        return self.clientes[0] if not self.esta_vacia() else "No hay clientes en la cola."

    def esta_vacia(self):
        return len(self.clientes) == 0

cola_banco = Cola()
cola_banco.encolar("Cliente 1")
cola_banco.encolar("Cliente 2")
cola_banco.encolar("Cliente 3")

print(f"Siguiente en la fila: {cola_banco.siguiente_cliente()}")
cola_banco.desencolar()  
print(f"Siguiente en la fila: {cola_banco.siguiente_cliente()}") 

cola_banco.desencolar()  
cola_banco.desencolar()  
cola_banco.desencolar()  

#Ejercicio 8

class Nodo:
    def __init__(self, dato):
        self.dato = dato 
        self.siguiente = None 
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        print(f"📌 {dato} insertado al inicio.")

    def recorrer(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' ➡️ ')
            actual = actual.siguiente
        print("None") 

lista = ListaEnlazada()
lista.insertar_al_inicio(30)
lista.insertar_al_inicio(20)
lista.insertar_al_inicio(10)

print("Contenido de la lista:")
lista.recorrer()

#Ejercicio 9

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def recorrer(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def invertir(self):
        previo = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = previo
            previo = actual
            actual = siguiente
        self.cabeza = previo

lista = ListaEnlazada()
lista.insertar_al_inicio(3)
lista.insertar_al_inicio(2)
lista.insertar_al_inicio(1)

print("Lista original:")
lista.recorrer()

lista.invertir()
print("Lista invertida:")
lista.recorrer()
