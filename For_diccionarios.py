frutas = {'Fresa': 'roja', 'Limon': 'verde', 'Papaya': 'naranja', 'Manzana': 'amarilla', 'Guayaba': 'rosa'}

for nombre, color in frutas.items():
    print(nombre, "es de color", color)

print(frutas.items())
print(type(frutas.items()))
