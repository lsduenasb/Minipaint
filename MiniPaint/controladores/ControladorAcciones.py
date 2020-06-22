from random import randint, uniform,random
from modelo.figuras.Cuadrilatero import Cuadrilatero
from modelo.figuras.Circulo import Circulo
class ControladorAcciones:

    def __init__(self):
        pass

    def crearCirculo(self,lienzo):
        circ = Circulo(randint(0, 400), randint(0, 300), randint(1, 3), "#3FD31F", randint(1, 150))
        circ.dibujar(lienzo)

    def crearCuadrilatero(self,lienzo):
        c = Cuadrilatero(randint(0, 400), randint(0, 300), randint(1, 3), "#D31F71", randint(5, 200), randint(5, 150))
        c.dibujar(lienzo)