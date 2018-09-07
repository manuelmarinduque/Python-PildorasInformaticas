"""print("Hola. Escriba tu nombre: ")
nombre = input()
print("Es un placer conocerte, ", nombre)"""

"""
numero = 5
numero2 = 7

if numero2 > numero:
    print("numero", numero2, "es mayor")
"""

"""
def sumar(num1, num2):
    print(num1 + num2)


sumar(4, 6)


def sumar2(num1, num2):
    resultado = num1+num2
    return resultado
    

print(sumar2(6, 9))
"""

"""
miLista = ["Manuel", 1997, 21, "Marín"]
print(miLista) #Imprime toda la lista.
print(miLista[-2]) #Empieza desde el final.
print(miLista[0:2]) #Acceder a una porción de la lista.
"""

"""
miDiccionario = {"Alemania":"Berlin", "Francia":"Paris", "Colombia":"Bogotá"}
#Accediendo a la clave, se accede al valor.
print(miDiccionario["Colombia"])
#Agregar una nueva asociación clave:valor:
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)
#De igual modo al anterior se puede corregir un valor:
miDiccionario["Italia"]="Roma" #Aquí se sobreescribe.
print(miDiccionario)
#Eliminar un elemento:
del miDiccionario["Alemania"]
print(miDiccionario)
"""

"""
def evaluacion(nota):
    valoracion = "Aprobado"
    if nota < 5:
        valoracion = "Suspenso"
    return valoracion


nota_alumno = int(input("Ingrese una nota: "))
print(evaluacion(nota_alumno))
"""

"""
#Uso del else: el else es propiedad del if más cercano:
#Para que el else sea parte del bloque cuando se tienen varias condiciones, se usa elif.
edad_usuario = int(input("Introduce tu edad"))
if edad_usuario<18:
    print("No puede pasar")
#Probar con if para observar el error.
elif edad_usuario>100:  #No se puede usar if, ya que se produce un error.
    print("Edad incorrecta")
else:
    print("Puede pasar")
"""

"""
edad = 7

if 0<edad<100:   #Concatenación de operadores de comparación. Se lee con "y": todas las condiciones deben
                  #  cumplirse para que sea correcto. Se pueden concatenar 1 o varios comparadores.
    print("Edad es correcta")
else:
    print("Edad incorrecta")
"""

"""
distancia_escuela = int(input("Ingrese distancia "))
numero_hermanos = int(input("Ingrese cantidad de hermanos "))
salario = int(input("Ingrese salario "))

if distancia_escuela>40 and numero_hermanos>2 or salario<=20000:
    print("Tiene derecho a la beca")
else:
    print("No tiene derecho a la beca")
"""

"""
# Uso del operador in
opcion = input("Ecribe tu asignatura ")
#Python es case sentitive y distingue entre MAY y min. Si un usuario digita una asignatura con una letra en
#MAY, la siguiente línea convierte toda la frase en min. y así se evita el error de escritura.
#Eso sí, en el in las opciones de la lista deben estar en min.
asignatura = opcion.lower()

if asignatura in ("informatica", "pruebas", "usabilidad"):
    print("Asignatura elegida", asignatura)
else:
    print("Asignatura no en la lista")
"""

"""
# Uso del ciclo for
# Este ciclo es confuso, pues recorre las veces de la longitud de un elemento: lista, tupla, etc.
for i in [1, 2, 3]:  # Recorre una Lista de 3 elementos.
    print("Hola")

for j in ("Maria", "Pedro", "Carlos", "ángela"):  # Recorre una tupla de 4 elementos.
    print("Confuso")

for estaciones in ["Primavera", "verano", "Otoño", "Invierno"]:
    print(estaciones)

# Observar min. +15 video 14

# For con un incrementador, así como en Java:
for i in range(5):  #Empieza desde el 0 hasta el 4
    print("Similar Java")
"""

"""
# Uso del ciclo for para comprobar si una dir. de email es correcta al llevar el @:
# email = input("Ingrese email")  # El email ingresado es una lista.
cond = 0  # Boleanos empiezan con MAY
for i in "Manuel.duque5.2@gmail.com":  # Manera de recorrer un string en PY. i va tomando el valor de cada letra.
    if i == "@" or i == ".":
        cond = cond+1
if cond >= 2:
    print("Email es correcto")
else:
    print("Email incorrecto")
"""

"""
# Método alternativo a la concatenación:
for i in range(4, 9):  #Empieza desde el 4 al 8
    print(f"Valor de la variable {i}")  # Memorizar la sintasis

for j in range(4):  #Empieza desde el 0 al 3
    print(f"Valor de la variable {j}")

for k in range(5, 50, 3):  #Empieza desde el 5 al 50 de 3 en 3
    print(f"Valor de la variable {k}")

# Conclusión, el usar range es para pocas ocasiones. Siempre se usa el for por defecto de PY
"""


