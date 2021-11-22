from animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0 
    aguilas = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPlumas = None):
        super().__init__(nombre=nombre, edad=edad, habitat=habitat, genero=genero)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)


    def crearHalcon(self, nombre, edad, genero):
        self.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")
    
    def crearAguila(self, nombre, edad, genero):
        self.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    def getColorPlumas(self):
        return self._colorPlumas  