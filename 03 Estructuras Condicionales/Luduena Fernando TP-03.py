#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

edad = int(input("Ingrese la edad: "))

if edad >= 18:
    print("Es mayor de edad.")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")
    
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar

numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("Ha ingresado un numero par.")
else:
    print("Por favor, ingrese un numero par.")
    
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Es nino.")
elif edad >= 12 and edad < 18:
    print("Es adolescente.")
elif edad >= 18 and edad < 30:
    print("Es adulto/a joven")
elif edad >= 30:
    print("Es adulto/a")


#Ejercicio 5

contrasena = input("Ingrese una contrasena: ")

if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contrasena correcta.")
else:
    print("Por favor, ingrese una contrasena de entre 8 y 14 caracteres.")

#Ejercicio 6
from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1,100) for i in range(50)]

print(f"La moda es: {mode(numeros_aleatorios)}")
print(f"La mediana es: {median(numeros_aleatorios)}")
print(f"La media es: {mean(numeros_aleatorios)}")

#Ejercicio 7

frase = input("Ingrese una frase o palabra: ")
vocales = ('a','e','i','o','u')


if frase[-1].lower() == "a" or frase[-1]== "e" or frase[-1]== "i" or frase[-1]== "o" or frase[-1]== "u":
    print(f"{frase}!")
else:
    print(frase)

#Ejercicio 8

nombre = input("Ingrese su nombre: ")
opcion = int(input("Como quiere ver su nombre? 1)Mayusculas 2)Minisculas 3)Titulo:"))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Esa opcion no existe.") 

#Ejercicio 9

escalaTerremoto = float(input("Ingrese la escala del terremoto: "))

if escalaTerremoto < 3:
    print("Muy leve (imperceptible)")
elif escalaTerremoto >= 3 and escalaTerremoto < 4:
    print("Leve(ligeramente perceptible).")
elif escalaTerremoto >= 4 and escalaTerremoto < 5:
    print("Moderado(sentido por personas, pero generalmente no causa daños)")
elif escalaTerremoto >= 5 and escalaTerremoto < 6:
    print("Fuerte(Puede causar daños en estructuras debiles.)")
elif escalaTerremoto >= 6 and escalaTerremoto < 7:
    print("Muy fuerte(Puede causar daños significativos)")
elif escalaTerremoto >= 7:
    print("Extremo(puede causar graves daños a gran escala)")

#Ejercicio 10

hemisferio = input("Ingrese en que hemisferio se encuentra N/S: ")
dia = int(input("Ingrese en que dia del mes se encuentra (1-31): "))
mes = int(input("Ingrese el mes en el que se encuentra (1-12) : "))

if hemisferio.lower() == "n":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print ("Se encuentra en Invierno")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("Se encuentra en Primavera")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print ("Se encuentra en Verano")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print("Se encuentra en Otoño")
elif hemisferio.lower() == "s":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Se encuentra en Verano")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("Se encuentra en Otoño")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("Se encuentra en Invierno")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print("Se encuentra en Primavera")
else:
    print("Hemisferio no válido")
