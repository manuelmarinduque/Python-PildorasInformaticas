email = input("Ingrese email: ")

for i in email:
    if i == "@":
        arroba = True
        break
#Uso del else con el ciclo for. El else se ejecuta luego de realizar la
#última iteración:
else:
    arroba = False

print(arroba)
