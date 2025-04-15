
#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo")

imprimir_hola_mundo()

#Ejercicio2

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

#Ejercicio 3

def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4

from math import pi, pow

def calcular_area_circulo(radio):
    area = pi * pow(radio, 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * radio
    return perimetro

radio = int(input("Ingrese el radio para saber calculara area y perimetro: "))

print(f"El area del circulo es {round(calcular_area_circulo(radio),2)} y su perimetro es {round(calcular_perimetro_circulo(radio),2)}")

#Ejercicio 5

def segundos_a_horas(segundos):
    total = segundos / 60
    return total

segundos = int(input("Ingrese la cantidad de segundos para pasar a horas: "))

print(f"La cantidadd de segundos en horas es {segundos_a_horas(segundos)} hs.")

#Ejercicio 6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero * i)

numero = int(input("Ingrese el numero del que quiere sabre la tabla de multiplicar: "))

tabla_multiplicar(numero)

#Ejercicio 7

def operaciones_basicas(a,b):
    
    suma = a + b
        
    resta = a - b
    
    multiplicacion = a * b
    
    if b != 0:
        division = a / b
    
        
    resultados = (f"Suma:{suma}",f"Resta:{resta}", f"Multiplicacion:{multiplicacion}",f"Division:{division}")
    
    print (resultados)

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

operaciones_basicas(numero,numero2)

#Ejercicio 8

def calcular_imc(peso, altura):
    
    imc = peso / altura ** 2
    return round(imc, 2)

peso = float(input("Ingrese su peso(en kg): "))
altura = float(input("Ingrese su altura(en mts): "))

print(f"Su imc es {calcular_imc(peso, altura)}")

#Ejercicio 9

def celsius_a_farenheit(celsius):
    resultado = (celsius * 1.8) + 32
    return resultado

celsius = float(input("Ingrese la cantidad de celsius a pasar a farenheit: "))

print(f"La cantidad de grados celsius en farenheit es {celsius_a_farenheit(celsius)}")

#Ejercicio 10

def calcular_promedio(a,b,c):
    
    promedio = (a+b+c) / 3
    return promedio

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

print(f"El promedio de los numeros ingresados es {calcular_promedio(numero1, numero2, numero3)}")