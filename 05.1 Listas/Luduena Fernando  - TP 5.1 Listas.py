#Ejercicio 1

lista_numeros = list(range(0,100,4))

print(lista_numeros)

#Ejercicio 2

lista_5elementos = ["Ricardo Arjona", "Juan Gabriel", "Call of Duty", "Dragon Ball Z", "Naruto"]
print(lista_5elementos[-2])

#Ejercicio 3

lista_vacia = []

lista_vacia.append("Python")
lista_vacia.append("C#")
lista_vacia.append("Assembler")

print(lista_vacia)

#Ejercicio 4

animales = ["perro", "gato", "conejo", "pez"]
print(animales)

animales[1] = "loro"
animales[-1] = "oso"

print(animales)

#Ejercicio 5

#Lo que hace el script del ejercicio 5 es remover el mayor numero de la lista(que seria el 22)

#Ejercicio 6

lista_10a30 = []
lista_10a30 = list(range(10, 31, 5))

print(lista_10a30[:2])

#Ejercicio 7

autos = ["sedan", "polo","suran", "gol"]

autos[1] = "SW4"
autos[2] = "Tiguan"

print(autos)

#Ejercicio 8

dobles = []

dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)

#Ejercicio 9

compras = [["pan", "leche"], ["arroz","fideos","salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

#Ejercicio 10

lista_anidada = [[15],[True],[25.5,57.9, 30.6],[False]]

print(lista_anidada)