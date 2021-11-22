from gestion.zoologico import Zoologico

class Zona():
    def __init__(self, nombre = None, zoo = Zoologico()):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []
        zoo.agregarZonas(self)

    def agregarAnimales(self, animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)        

    def setNombre(self, nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre
    def setZoo(self, zoo):
        self._zoo = zoo
    def getZoo(self):
        return self._zoo
    def setAnimales(self, animales):
        self._animales = animales
    def getAnimales(self):
        return self._animales
