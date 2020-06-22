from tkinter import *
from tkinter import ttk

from controladores.ControladorAcciones import ControladorAcciones
from modelo.figuras.Cuadrilatero import Cuadrilatero
from modelo.figuras.Circulo import Circulo
class Ventana:

    def __init__(self, titulo):

        self.ventana = Tk()
        self.ventana.geometry('700x500')
        self.ventana.configure(bg="#ABEBC6")
        self.ventana.title(titulo)
        self.canvas = Canvas(self.ventana, width=400,height=300, bg="#C3D4D7")
        self.canvas.pack()
        ttk.Button(self.ventana, text='Salir', command=self.ventana.destroy).pack(side=BOTTOM)
        ca = ControladorAcciones()
        botonCirculo = Button(self.ventana, text="Crear Circulo",  bg="#DB9CA6",command=lambda: ca.crearCirculo(self.canvas)).pack(side=TOP)
        botonCuadrilatero = Button(self.ventana, text="Crear Cuadrilatero", bg="#DB9CA6",command=lambda: ca.crearCuadrilatero(self.canvas)).pack(side=TOP)

