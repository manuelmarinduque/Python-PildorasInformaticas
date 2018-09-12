class Vehiculos:

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.__marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
              self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


# Herencia: Para especificar la clase de la cual se hereda, esta se pone dentro de los paréntesis:
class Vehiculos_Electricos(Vehiculos):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarenergia(self):
        self.cargando = True


class Bicicleta_Electrica(Vehiculos_Electricos):
    pass


miBicicleta = Bicicleta_Electrica("Electric Charge", 1997)
miBicicleta.estado()