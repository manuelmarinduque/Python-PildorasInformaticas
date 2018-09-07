edad = int(input("Ingrese una edad: "))

while edad < 0 or edad > 100:
    print("La edad es incorrecta")
    edad = int(input("Ingrese una edad: "))

print("La edad es: ", edad)

#Hay veces que es necesario usar bucles infinitos, como en el caso de los hilos.
#Ya que puede que un programa se ejecute indefinidamente en segundo plano.