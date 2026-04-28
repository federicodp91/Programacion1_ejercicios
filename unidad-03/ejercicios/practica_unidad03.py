"""

1. Solicita al usuario que ingrese su nombre y su edad. Luego, imprime un mensaje que diga "¡Hola, [nombre]! Tienes [edad] años".
"""

nombre_usuario = input("Ingresar nombre de usuario: ")
edad_usuario = int(input("Ingresar edad: "))

print(f"Hola {nombre_usuario}, tienes {edad_usuario} años")


# 2. Imprima en pantalla las siguientes figuras geometricas (utilizar concatenación y replicación de strings)

extremos = "+" + "*" * 15 + "+"
medio = "*" + " " * 15 + "*"

print(extremos)
print(medio)
print(medio)
print(medio)
print(extremos)


"""
+***************+
*               *
*               *
*               *
+***************+

"""

linea_arriba_abajo = "+" + "-" * 3 + "+"
linea_medio = "|" + " " * 3 + "|"

print(linea_arriba_abajo)
print(linea_medio)
print(linea_medio)
print(linea_medio)
print(linea_arriba_abajo)


"""
+---+
|   |
|   |
|   |
+---+

"""

a = "#" * 35
b = "#" * 2 + " " * 31 + "#" * 2

print(a)
print(a)
print(b)
print(b)
print(b)
print(a)
print(a)


###################################
###################################
##                               ##
##                               ##
##                               ##
###################################
###################################


""" 3. Solicita al usuario que ingrese dos números enteros.
Luego, convierte estos números a float, realiza la división de ambos y muestra el resultado.
"""
numero1 = int(input("Ingresar un numero entero: "))
numero2 = int(input("Ingresar otro numero entero: "))
resultado = float(numero1 / numero2)

print(resultado)
print(type(resultado))

""" 4. Pide al usuario que ingrese una cadena que represente un número entero.
Convierte esta cadena a un entero usando la función int() y luego suma 10. Imprime el resultado.
"""

numero_usuario = input("Ingresar un número entero: ")
resultado = int(numero_usuario) + 10

print(f"El resultado es: {resultado}")

""" 5. Pregunta al usuario que ingrese un número. Si el número es mayor que 10,
imprime "El número es mayor que 10". Si es igual a 10,
imprime "El número es igual a 10". De lo contrario, imprime "El número es menor que 10".
"""

numero = int(input("Por favor ingresar un número: "))

if numero > 10:
    print("El número es mayor que 10")

elif numero == 10:
    print("El número es igual a 10")

else:
    print("El número es menor que 10")


""" 6. Solicita al usuario que ingrese dos números y compara si son iguales. Si lo son, imprime "Los números son iguales".
De lo contrario, imprime "Los números son diferentes".
"""
numero1 = int(input("Ingresar un número: "))
numero2 = int(input("Ingresar otro número: "))

if numero1 == numero2:
    print("Los números son iguales")

else:
    print("Los números son diferentes")

""" 7. Pregunta al usuario que ingrese su edad. Si la edad es mayor o igual a 18,
imprime "Eres mayor de edad". De lo contrario, imprime "Eres menor de edad".
"""

edad_usuario = int(input("Ingresá tu edad: "))

if edad_usuario >= 18:
    print("Eres mayor de edad")

else:
    print("Eres menor de edad")


""" 8. Pide al usuario que ingrese una temperatura en Celsius. Si la temperatura es mayor o igual a 100,
imprime "El agua está hirviendo". Si es menor o igual a 0, imprime "El agua está congelada". De lo contrario,
imprime "El agua está en estado líquido".
"""

temperatura = int(input("Ingresar una temperatura en grados Celsius"))

if temperatura >= 100:
    print("El agua está hirviendo")

elif temperatura <= 0:
    print("El agua esta congelada")

else:
    print("El agua está en estado líquido")


""" 9. Pregunta al usuario que ingrese un número. Si es positivo, imprime "El número es positivo".
Si es negativo, imprime "El número es negativo". Si es cero, imprime "El número es cero".
"""

numero = int(input("Ingresar un número: "))

if numero > 0:
    print(f"El número {numero} es positivo")

elif numero < 0:
    print(f"El número {numero} es negativo")

else:
    print(f"El número es {numero}")


""" 10. Solicita al usuario que ingrese un número del 1 al 7. Luego, imprime el día de la semana correspondiente
(1 para Lunes, 2 para Martes, etc.). Si ingresa un número fuera de ese rango, imprime "Número de día no válido".
"""

numero = int(input("Ingresar un número de 1 al 7: "))

if numero == 1:
    print("Lunes")

elif numero == 2:
    print("Martes")

elif numero == 3:
    print("Miercoles")

elif numero == 4:
    print("Jueves")

elif numero == 5:
    print("Viernes")

elif numero == 6:
    print("Sabado")

elif numero == 7:
    print("Domingo")

else:
    print("Numero de día no valido")


""" 11.Calculadora básica
Crea un programa que tome dos números como entrada y luego imprima la suma, resta,
multiplicación y división de esos dos números. Usa operadores aritméticos y asegúrate de manejar casos donde el divisor sea cero.
"""

numero_1 = int(input("Ingresar un número: "))
numero_2 = int(input("Ingresar otro número: "))


suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2

if numero_2 != 0:
    print(f"la división de ambos números es: {numero_1 / numero_2}")
else:
    print("No se puede dividir por 0")


print(f"La suma de ambos números es {suma}")
print(f"La resta de ambos números es {resta}")
print(f"La multiplicacion de ambos números es {multiplicacion}")
# SUGERENCIA: el orden de impresión es raro: primero mostrás la división y después suma/resta/multiplicación.
#             Quedaría más prolijo imprimir todo en orden lógico (suma, resta, multiplicación, división).
# CORRECCIÓN: typo "multiplicacion" → "multiplicación" (en el mensaje del print).


""" 12.Calculador de IMC
Crea un programa que calcule el Índice de Masa Corporal (IMC) de una persona. Pide al usuario su peso en kilogramos y su altura en metros.
Luego, calcula el IMC usando la fórmula `IMC = peso / altura**2` y muestra el resultado con un mensaje que indique si el IMC está en el rango normal,
bajo peso, sobrepeso, etc.
"""
peso_usuario = float(input("Ingresar tu peso en Kg: "))
altura_usuario = float(input("Ingresar tu altura en Mts: "))

if peso_usuario <= 0 or altura_usuario <= 0:
    print("Error, el peso y la altura deben ser mayores a 0")

else:
    imc = peso_usuario / (altura_usuario**2)

    if imc < 18.5:
        print(f"El IMC es {imc} y se encuentra en un rango de bajo peso")

    elif 18.5 <= imc < 25:
        print(f"El IMC es {imc} y se encuentra en un rango normal")

    elif 25 <= imc < 30:
        print(f"El IMC es {imc} y se encuentra en un rango de sobrepeso")

    else:
        print(f"El IMC es {imc} y se encuentra en un rango de obesidad")


""" 13.Conversión de unidades
Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit. La fórmula de conversión es
`F = C * 9/5 + 32`. Pide al usuario que ingrese una temperatura en Celsius y muestra el resultado en Fahrenheit.
"""

celsius = float(input("Ingresar la temperatura en grados celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°Celsius corresponden a {fahrenheit}° Fahrenheit")

""" 14.Juego de adivinanza
Crea un programa que pida al usuario que adivine un número entre 1 y 10.
El programa debe comparar el número ingresado con uno predefinido (por ejemplo, 7) y decir si es correcto o no. Si es incorrecto,
debe dar una pista si el número es mayor o menor.
"""
"""
"""
valor_usuario = int(input("Inresar un número entre 1 y 10: "))
# CORRECCIÓN: typo en el mensaje "Inresar" → "Ingresar".
valor_ganador = 7

if valor_usuario <= 0 or valor_usuario > 10:
    # CORRECCIÓN: la condición `valor_usuario <= 0` deja pasar valores entre 0 y 1 si fueran floats,
    #             pero más importante: el rango pedido es 1 a 10, así que lo correcto sería:
    #                 if valor_usuario < 1 or valor_usuario > 10:
    #             Con `<= 0` rechazás 0 y negativos, pero la lógica conceptual debería ser "fuera del rango [1, 10]".
    print("Error! El valor ingresado debe ser entre 1 y 10")

elif valor_usuario == valor_ganador:
    print("GANASTE")

elif valor_usuario < valor_ganador:
    print("Pista: es Mayor!")

else:
    print("Pista: Es menor")


""" 15.Identificación del tipo de dato
"""

""" Escribe un programa que tome una entrada del usuario usando input() y determine qué tipo de dato representa la cadena ingresada.
Ten en cuenta que input() siempre devuelve una cadena de texto (string), pero el usuario puede haber ingresado algo que representa un número.



Tu programa debe analizar la entrada y determinar si representa:

Un número entero (positivo o negativo)
Un número flotante (positivo o negativo)
Una cadena de texto

Requisitos específicos:

Usa el método isdigit() para verificar si todos los caracteres son dígitos
Para números negativos, verifica si el primer carácter es un guión (-) usando indexación
Para números flotantes, verifica si contiene exactamente un punto decimal
Imprime un mensaje claro indicando qué tipo de dato representa la entrada


Ejemplo de salidas esperadas:

Entrada: "123" → "El dato representa un número entero"
Entrada: "-45" → "El dato representa un número entero negativo"
Entrada: "3.14" → "El dato representa un número flotante"
Entrada: "-2.5" → "El dato representa un número flotante"
Entrada: "hola" → "El dato representa una cadena de texto"
"""

entrada = input("Ingresar un número: ")

print(entrada.isdigit())
# CORRECCIÓN: este print parece ser de debug, conviene eliminarlo de la versión final.

if entrada.isdigit() == True:
    # SUGERENCIA: comparar con `== True` es redundante. Es más pythónico escribir:
    #             if entrada.isdigit():
    print("El dato representa un número entero")

else:
    if entrada[0] == "-" and entrada[1:].isdigit() == True:
        # CORRECCIÓN: si la entrada está vacía (""), `entrada[0]` lanza IndexError.
        #             Convendría validar primero: if len(entrada) > 0 and entrada[0] == "-" ...
        print("El dato representa un número entero negativo")

    elif entrada.count(".") == 1 and entrada.replace(".", "").isdigit() == True:
        print("El dato representa un número flotante")

    elif (
        entrada[0] == "-"
        and entrada.count(".") == 1
        and entrada.replace(".", "").replace("-", "").isdigit() == True
    ):
        print("El dato representa un número flotante negativo")

    else:
        print("El dato representa una cadena de texto")


""" 16.Calculador de calificaciones
Crea un programa que pida al usuario que ingrese sus calificaciones en tres materias.
Luego, calcula el promedio de esas calificaciones e imprime un mensaje que indique si el alumno aprobó (promedio ≥ 6) o no. """

calificacion_matematica = int(input("Ingresar calificación de matemáticas: "))
calificacion_historia = int(input("Ingresar calificación de Historia: "))
calificacion_programacion = int(input("Ingresar calificación de Programación: "))

promedio = (
    calificacion_historia + calificacion_matematica + calificacion_programacion
) / 3

if promedio >= 6:
    print(f"El promedio de las 3 materias es: {promedio}, esta aprobado")

else:
    print(f"El promedio de las 3 materias es: {promedio}, esta desaprobado")


""" 17.Concatenación de strings
Escribe un programa que pida al usuario su nombre y su color favorito. Luego,
concatena estos datos en una sola oración que diga "Hola [nombre], tu color favorito es [color]" y la imprima.
"""

nombre_usuario = input("Ingresá tu nombre: ")
color_usuario = input("Ingresá tu color favorito: ")

print(f"Hola {nombre_usuario}, tu color favorito es {color_usuario}")
