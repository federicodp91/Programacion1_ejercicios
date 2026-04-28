# 1. Calcula el área de un rectángulo con base 5 y altura 3. Imprime el resultado.

b = 5
h = 3

a = b * h

print("El área del rectángulo es ", a)


# 2. Convierte la temperatura de Celsius a Fahrenheit. Pide al usuario ingresar la temperatura en Celsius y luego imprime la temperatura equivalente en Fahrenheit.

celsius = float(input("Ingresar la temperatura en Celsius "))
fahrenheit = (celsius * 1.8) + 32

print(
    "La temperatura ingresada en Celsius es: ",
    celsius,
    "La misma equivale a ",
    fahrenheit,
    "grados fahrenheit",
)


# 3. Concatena tu nombre y tu edad como strings y guárdalos en una variable. Luego imprime el tipo de dato de esa variable.

nombre = "Federico"
edad = str(34)

concatenar = nombre + "" + edad
# CORRECCIÓN: el `+ "" +` no agrega nada, da "Federico34" sin separación.
#             Si querés un espacio entre nombre y edad, usá " " en lugar de "".
#             Los paréntesis envolviendo la expresión también son innecesarios.
# SUGERENCIA: el ejercicio pide imprimir el tipo de dato, pero también convendría imprimir el valor concatenado
#             para verificar el resultado, p. ej.: print(concatenar)

print(type(concatenar))

# 4. Calcula el área de un círculo con radio 4. Imprime el resultado.

radio = 4
pi = 3.14159
area = pi * (radio**2)

print("El área del círculo es ", area)
# SUGERENCIA: en vez de hardcodear pi, podés usar el módulo math (más preciso):
#             import math
#             area = math.pi * radio**2  ------>>> igual esto no lo habíamos visto en esa etapa

# 5. Pide al usuario que ingrese dos números y muestra la suma, resta, multiplicación y división de esos números.


numero1 = float(input("Ingrese un número "))
numero2 = float(input("Ingrese Otro número "))

print("La suma de esos números es: ", numero1 + numero2)
print("La resta de esos números es: ", numero1 - numero2)
print("La multiplicación de esos números es: ", numero1 * numero2)
print("La divición de esos números es: ", numero1 / numero2)
# CORRECCIÓN: typo "divición" → "división".
# CORRECCIÓN: si el usuario ingresa 0 como segundo número, el programa rompe con ZeroDivisionError.
#             Convendría validar antes:
#                 if numero2 != 0:
#                     print("La división es:", numero1/numero2)
#                 else:
#                     print("No se puede dividir por 0")

# 6. Almacena el resultado de una operación aritmética compleja en una variable y luego imprime tanto el resultado como el tipo de dato de esa variable.

a = 20
b = 100
c = 2
e = 1.2
operacion = (a + e * (b * c)) / 2

print(operacion)
print(type(operacion))

# 7. Crea una variable booleana que represente si un alumno ha aprobado o no un examen y luego imprime su estado.

nota = 7
nota_alumno1 = nota >= 7


print(f"¿El alumno, está aprobado?: {nota_alumno1}")


# 8. Calcula el perímetro de un triángulo equilátero con lados de longitud 6. Imprime el resultado.

lado_triangulo = 6
perimetro = lado_triangulo * 3

print(f"El perímetro del triángulo es: {(perimetro)}")

# 9. Pide al usuario que ingrese su nombre, edad y ciudad de residencia y luego imprime cada uno de esos datos con su respectivo tipo de dato.

nombre_usuario = input("Por favor, ingrese su nombre: ")
edad_usuario = int(input("Por favor, ingrese su edad: "))
ciudad_usuario = input("Por favor, ingrese su ciudad de residencia: ")

print(
    f"El nombre de usuario es: {nombre_usuario} y el tipo de dato es: {type(nombre_usuario)}"
)
print(
    f"La edad del usuario es: {edad_usuario} y el tipo de dato es: {type(edad_usuario)} "
)
print(
    f"La ciudad de residencia es: {ciudad_usuario} y el tipo de dato es : {type(ciudad_usuario)}"
)


# 10. Realiza una operación matemática que involucre paréntesis, multiplicación, suma y resta. Guarda el resultado en una variable y luego imprímela junto con su tipo de dato.

resultado = 205.6 * (1402.80 + 500) - 100

print(f"El resultado es: {resultado}")
print(f"El tipo de dato es: {type(resultado)}")


# Muy bien resuelto todos! Perfecto!
