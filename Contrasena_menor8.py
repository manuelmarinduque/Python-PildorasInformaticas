"""Crea un programa que pida por teclado introducir una contraseña. La contraseña no podrá tener menos de 8 caracteres ni
espacios en blanco. Si la contraseña es correcta, el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña errónea”"""

password = input("Ingrese una contraseña: ")
#passwrod es una lista.
contador = 0

if len(password)<8:
    print("Contraseña muy corta")
else:
    #i va tomando el valor de cada letra que se ingresa en password y evaluando
    #si hay espacios en blanco.
    for i in password:
        if i == " ":
            contador = contador+1

    if contador > 0:
        print("Contraseña incorrecta")
    else:
        print("Contraseña correcta")