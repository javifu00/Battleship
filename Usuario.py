class Usuario:
    def __init__(self, username, nombre, edad, genero, puntaje=1, disparos_efectuados=100):
        self.username = username
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.puntaje = puntaje
        self.disparos_efectuados = disparos_efectuados
    def __str__(self):
        return "Usuario: {}\nNombre completo: {}\nEdad: {}\nGenero: {}\nPuntaje: {}\nDisparos efectuados: {}".format(self.username, self.nombre, self.edad, self.genero, self.puntaje, self.disparos_efectuados)
    def mostrar_datos(self):
        print("Info del usuario \nUsername: {} \nNombre: {}\nEdad: {}\nGenero: {}\nPuntaje: {}\nDisparos acertados: {}".format(self.username, self.nombre, self.edad, self.genero, self.puntaje, self.disparos_efectuados))
    def para_txt(self):
        print("{}, {}, {}, {}".format(self.username, self.nombre, self.edad, self.genero))
    def mostrar_usuario(self, username):
        self.username = username
        print(self.username)

