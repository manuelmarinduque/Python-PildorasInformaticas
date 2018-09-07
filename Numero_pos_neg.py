""""Crea un programa que pida números positivos indefinidamente. El programa termina cuando se introduce un número negativo.
Finalmente el programa muestras la suma de todos los números introducidos"""

numero = int(input("Ingrese un número: "))
suma = 0

while numero > 0:
    suma = suma + numero
    numero = int(input("Ingrese un número: "))
    if numero < 0:
        print("Fin de la ejecución")
        break

print("El resultado es: ", suma)
