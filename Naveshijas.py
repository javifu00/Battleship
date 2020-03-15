import Naves
class Portaviones:
    """
    Clase donde se almacenan los datos especificos del Portaviones (tamano, cantidad)
    """
    tamano = 3
    cantidad = 1
    def __init__(self, orientacion, ubicacion, tamano, cantidad):
        self.tamano = tamano
        self.cantidad = cantidad
        super().__init__(orientacion, ubicacion)
    def caracteristicas(self):
        return "{} Portavion que ocupa {} posiciones y tiene la capacidad de aterrizar helicopteros en el para transportar las tropas".format(self.cantidad, self.tamano)
class Fragata:
    """
    Clase donde se almacenan los datos especificos de la Fragata (tamano, cantidad)
    """
    tamano = 2
    cantidad = 1
    def __init__(self, orientacion, ubicacion, tamano, cantidad):
        self.tamano = tamano
        self.cantidad = cantidad
        super().__init__(orientacion, ubicacion)
    def caracteristicas(self):
        return "{} Fragata que ocupa {} posiciones y tiene la capacidad de comunicarse con tierra y otros miembro de la flota".format(self.cantidad, self.tamano)
class Submarinos:
    """
    Clase donde se almacenan los datos especificos de los Submarinos (tamano, cantidad)
    """
    tamano = 1
    cantidad = 4
    def __init__(self, ubicacion, tamano, cantidad):
        self.tamano = tamano
        self.cantidad = cantidad
        super().__init__(ubicacion)
    def caracteristicas(self):
        return "{} Submarinos que ocupan {} posicion y que tienen la capacidad de sumergirse y emerger del agua".format(self.cantidad, self.tamano)  
