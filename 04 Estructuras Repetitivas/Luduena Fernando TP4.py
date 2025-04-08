#Ejercicio 1

for i in range(0, 101):
    print(i) 

#Ejercicio 2

numero = int(input("Ingrese un numero entero: "))
cantDigitos = 0

while numero > 0:
    numero //= 10
    cantDigitos += 1

print(f"La cantidad de digitos es {cantDigitos}")

#Ejercicio 3

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

suma = 0

for num in range(numero1 + 1, numero2):
    suma += num

print(f"La suma entre los numeros {numero1} y {numero2}, excluyendolos es de {suma}")

#Ejercicio 4

num = 1
suma = 0

while num != 0:
    num = int(input("Ingrese un numero(corta con 0):"))
    suma += num

print(f"La suma de los numeros ingresados es {suma}")

#Ejercicio 5

from random import randint

aleatorio = randint(1,9)
cont = 0
num = 0

while  num != aleatorio:
    num = int(input("Ingrese el numero que cree que es: "))
    cont += 1

print(f"La cantidad de intentos realizados es de {cont} intentos.")

#Ejercicio 6

for i in range(100, 0, -2):
    print(i)

#Ejercicio 7

num = int(input("Ingrese un numero: "))
suma = 0

for i in range(0 , num):
    suma += i

print(f"La suma de 0 hasta el numero ingresado es {suma}")

#Ejercicio 8

pares = 0
impares = 0
positivos = 0
negativos = 0


for i in range(0,100):
    num = int(input("Ingrese un numero: "))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        print("El cero no se contabilizara porque es un numero neutro")

print(f"La cantidad de pares ingresados es de {pares}")
print(f"La cantidad de impares ingresados es de {impares}")
print(f"La cantidad de positivos ingresados es de {positivos}")
print(f"La cantidad de negativos ingresados es de {negativos}")

#Ejercicio 9

from statistics import mean
acumuladorMedia = 0

for i in range(0, 100):
    num = int(input("Ingrese los numeros para saber la media(puede ingresar hasta 100): "))
    acumuladorMedia += num

print(f"La media de los numeros ingresados es {mean(acumuladorMedia)}")

#Ejercicio 10

num = input("Ingrese un numero para darlo vuelta: ")
numInvertido = ""

for digito in num[::-1]:
    numInvertido += digito

print(f"Numero invertido: {numInvertido} ")