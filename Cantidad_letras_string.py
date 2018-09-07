#Cotar la cantidad de letras de un estring, se hace uso de continue para que no cuente
#el espacio en blanco.
nombre = "Pildoras informáticas"
contador = 0

for i in nombre:
    if i == " ":
        #Continue hace que el ciclo actual no se ejecute.
        #En este caso no cuenta el espacio en blanco y continúa con el sgte ciclo.
        continue
    contador += 1

print(contador)
