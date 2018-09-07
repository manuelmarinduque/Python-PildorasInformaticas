"""Crea un programa que pida números infinitamente. Los números introducidos deben ser cada vez mayores.
 El programa finalizará cuando se introduce un número menor que el anterior."""

numero1 = int(input("Ingrese un número: "))
numero2 = 0

while numero1 > numero2:
    numero2 = numero1
    numero1 = int(input("Ingrese un número: "))
    if numero2 > numero1:
        break
