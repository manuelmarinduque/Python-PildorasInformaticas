def devuelve_ciudades(*ciudades):
    # * indica que se ingresa una cantidad indefinida de parámetros, los cuales
    # estarán dentro de una tupla.
    for elemento in ciudades:
        yield elemento

# Creando el objeto generador:
ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
