class Animal():
    totalAnimales = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self.totalAnimales += 1
        self._zona = []

    def totalPorTipo(self):
        formato = """Mamiferos: {0}
        Aves: {1}
        Reptiles: {2}
        Peces: {3}
        Anfibios: {4}"""

        return formato.format(len(Mamifero.listado),len(Ave.listado),len(Reptil.listado),len(Pez.listado),len(Anfibio.listado))

    def __str__(self):
        if (len(self._zona) == 1):
            formato = "Mi nombre es {0}, tengo una edad de {1}, habito en {2} y mi genero es {3}, la zona en la que me ubico es {4}, en el {5}"
            return formato.format(self._nombre, self._edad, self._habitat, self._genero, self._zona[0].getNombre(), self._zona[0].getZoo().getNombre())
        else:
            formato = "Mi nombre es {0}, tengo una edad de {1}, habito en {2} y mi genero es {3}"
            return formato.format(self._nombre, self._edad, self._habitat, self._genero)           


    def setNombre(self, nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre

    def setEdad(self, edad):
        self._edad = edad
    def getEdad(self):
        return self._edad   

    def setHabitat(self, habitat):
        self._habitat = habitat
    def getHabitat(self):
        return self._habitat

    def setGenero(self, genero):
        self._genero = genero
    def getGenero(self):
        return self._genero