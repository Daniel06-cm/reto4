# ===================================================
# Reto 4
# Daniel Camilo Calderon Vargas
# ===================================================

# --------------------------------------
# PROBLEMA 1:
# Determinar si un número corresponde al código ASCII de una vocal minúscula
# --------------------------------------

# Lista de códigos ASCII de vocales minúsculas
vocales_ascii = [ord(vocal) for vocal in "aeiou"]

# Solicitar un número al usuario
numero = int(input("Introduce un número entero: "))

# Verificar si el número corresponde a una vocal minúscula
if numero in vocales_ascii:
    print(f"El número {numero} corresponde a la vocal '{chr(numero)}'.")
else:
    print(f"El número {numero} no corresponde a una vocal minúscula.")


# --------------------------------------
# PROBLEMA 2:
# Dada una cadena de longitud 1, determine si el código ASCII de primera letra de la cadena es par o no.
# --------------------------------------

# Solicitar una cadena de longitud 1
caracter = input("Introduce un solo carácter: ")

# Validar que la entrada tenga longitud 1
if len(caracter) != 1:
    print("Debes ingresar exactamente un carácter.")
else:
    # Obtener el código ASCII del carácter
    codigo_ascii = ord(caracter)
    
    # Determinar si es par o impar
    if codigo_ascii % 2 == 0:
        print(f"El código ASCII de '{caracter}' es {codigo_ascii} y es un número PAR.")
    else:
        print(f"El código ASCII de '{caracter}' es {codigo_ascii} y es un número IMPAR.")



# --------------------------------------
# PROBLEMA 3:
# Dado un carácter, construya un programa en Python para determinar si el carácter es un dígito o no.
# --------------------------------------

# Solicitar un carácter al usuario
caracter = input("Introduce un carácter: ")

# Verificar que la entrada tenga longitud 1
if len(caracter) != 1:
    print("Debes ingresar exactamente un carácter.")
else:
    # Determinar si es un dígito usando el método isdigit()
    if caracter.isdigit():
        print(f"El carácter '{caracter}' es un dígito.")
    else:
        print(f"El carácter '{caracter}' NO es un dígito.")

        
# --------------------------------------
# PROBLEMA 4:
# Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
# --------------------------------------

# Solicitar dos números reales al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Validar que el segundo número no sea cero para evitar división por cero
if num2 == 0:
    print("No se puede dividir por cero.")
else:
    # Verificar si num1 es múltiplo de num2
    if num1 % num2 == 0:
        print(f"{num1} es múltiplo de {num2}.")
    else:
        print(f"{num1} NO es múltiplo de {num2}.")
        
# --------------------------------------
# PROBLEMA 5:
# Dado un número real x, construya un programa que permita determinar si el número es positivo, negativo o cero. Para cada caso de debe imprimir el texto que se especifica a continuación:

#Positivo: "El número x es positivo"
#Negativo: "El número x es negativo"
#Cero (0): "El número x es el neutro para la suma"
# --------------------------------------

# Solicitar un número real al usuario
x = float(input("Introduce un número real: "))

# Evaluar la condición y mostrar el mensaje adecuado
if x > 0:
    print(f"El número {x} es positivo")
elif x < 0:
    print(f"El número {x} es negativo")
else:
    print(f"El número {x} es el neutro para la suma")
    
# --------------------------------------
# PROBLEMA 6:
# Dado el centro y el radio de un círculo, determinar si un punto de R2 pertenece o no al interior del círculo.
# --------------------------------------

import math

# Solicitar datos al usuario
x_centro = float(input("Introduce la coordenada x del centro del círculo: "))
y_centro = float(input("Introduce la coordenada y del centro del círculo: "))
radio = float(input("Introduce el radio del círculo: "))
x_punto = float(input("Introduce la coordenada x del punto: "))
y_punto = float(input("Introduce la coordenada y del punto: "))

# Calcular la distancia euclidiana entre el punto y el centro del círculo
distancia = math.sqrt((x_punto - x_centro)**2 + (y_punto - y_centro)**2)

# Verificar si el punto está dentro del círculo
if distancia < radio:
    print("El punto está dentro del círculo.")
elif distancia == radio:
    print("El punto está sobre la circunferencia.")
else:
    print("El punto está fuera del círculo.")

# --------------------------------------
# PROBLEMA 7:
# Dada una cadena de longitud 1, determine si el código ASCII de primera letra de la cadena es par o no.
# --------------------------------------

# Solicitar las tres longitudes al usuario
a = float(input("Introduce la primera longitud: "))
b = float(input("Introduce la segunda longitud: "))
c = float(input("Introduce la tercera longitud: "))

# Verificar la condición de la desigualdad triangular
if a + b > c and a + c > b and b + c > a:
    print("Las longitudes pueden formar un triángulo.")
else:
    print("Las longitudes NO pueden formar un triángulo.")

# --------------------------------------
# PROBLEMA 8:
#Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado (Utilice match-case).
# --------------------------------------

# Solicitar el nombre del país en minúsculas
pais = input("Introduce el nombre de un país de América en minúsculas: ")

# Usar match-case para determinar la capital
match pais:
    case "argentina":
        capital = "Buenos Aires"
    case "bolivia":
        capital = "Sucre y La Paz"
    case "brasil":
        capital = "Brasilia"
    case "canadá":
        capital = "Ottawa"
    case "chile":
        capital = "Santiago"
    case "colombia":
        capital = "Bogotá"
    case "costa rica":
        capital = "San José"
    case "cuba":
        capital = "La Habana"
    case "ecuador":
        capital = "Quito"
    case "el salvador":
        capital = "San Salvador"
    case "estados unidos":
        capital = "Washington D.C."
    case "guatemala":
        capital = "Ciudad de Guatemala"
    case "haití":
        capital = "Puerto Príncipe"
    case "honduras":
        capital = "Tegucigalpa"
    case "méxico":
        capital = "Ciudad de México"
    case "nicaragua":
        capital = "Managua"
    case "panamá":
        capital = "Ciudad de Panamá"
    case "paraguay":
        capital = "Asunción"
    case "perú":
        capital = "Lima"
    case "república dominicana":
        capital = "Santo Domingo"
    case "uruguay":
        capital = "Montevideo"
    case "venezuela":
        capital = "Caracas"
    case _:
        capital = "País no identificado"

# Imprimir el resultado
print(f"La capital de {pais} es: {capital}")
