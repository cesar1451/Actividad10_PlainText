from .algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id=0, origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0,
                 red=0, green=0, blue=0, distancia=0.0):
        self.__id = id
        self.__origenX = origen_x
        self.__origenY = origen_y
        self.__destinoX = destino_x
        self.__destinoY = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(self.__origenX, self.__destinoX, self.__origenY, self.__destinoY)
    
    def __str__(self):
        return(
            'Id: ' + str(self.__id) + '\n' +
            'Origen x: ' + str(self.__origenX) + '\n' +
            'Origen y: ' + str(self.__origenY) + '\n' +
            'Destino x: ' + str(self.__destinoX) + '\n' +
            'Destino y: ' + str(self.__destinoY) + '\n' +
            'Velocidad: ' + str(self.__velocidad) + '\n' +
            'Color (rgb): \n'
            '       Red: ' + str(self.__red) + '\n' +
            '       Green: ' + str(self.__green) + '\n' +
            '       Blue: ' + str(self.__blue) + '\n' +
            'Distancia: ' + str(self.__distancia) + '\n'
        )
