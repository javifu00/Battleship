class Portaviones:
    tamano = 3
    cantidad = 1
    def __init__(self, orientacion, ubicacion):
        self.orientacion = orientacion
        self.ubicacion = ubicacion
    def tamano_cantidad(self):
        return self.tamano, self.cantidad
class Fragata:
    tamano = 2
    cantidad = 1
    def __init__(self, orientacion, ubicacion):
        self.orientacion = orientacion
        self.ubicacion = ubicacion
    def tamano_cantidad(self):
        return self.tamano, self.cantidad
class Submarinos:
    tamano = 1
    cantidad = 4
    def __init__(self, ubicacion):
        self.orientacion = orientacion
        self.ubicacion = ubicacion
    def tamano_cantidad(self):
        return self.tamano, self.cantidad   