import re
import tkinter as tk
from tkinter import filedialog


class Comando:
    def _init_(self,nombre,parametro):
        self.nombre = nombre
        self.parametro = parametro

class Lista:
    def _init_ (self,nombre,numeros,comandos):
        self.nombre = nombre
        self.numeros = numeros
        self.comandos = comandos

class Main:
    listas = []
    contenido_archivo = ""
    def menu(self):
        print("1 Cargar archivo de entrada")
        print("2 Desplegar listas ordenadas")
        print("3 Desplegar busquedas")
        print("4 Desplegar todas")
        print("5 Desplegar todas al archivo")
        print("6 salir"+"\n")
        entrada = input("Ingrese un numero 1-6"+"\n")
        patron = "[1-6]{1}"
        if re.search(patron, entrada):
            if entrada == "1":
                self.cargarArchivo()
                self.menu()
            # elif entrada == "2":
            # elif entrada == "3":
            #
            # elif entrada == "4":
            #
            # elif entrada == "5":

            elif entrada == "6":
                quit()
        else:
            self.menu()

    def cargarArchivo(self):
        root = tk.Tk()
        # root.withdraw()
        nombre_archivo = filedialog.askopenfilename(initialdir="/", title="Seleccionar un archivo", filetypes=(("texto", "*.txt"), ("todos", "*.*")))
        try:
            archivo = open(nombre_archivo, "r")
            contenido_archivo = archivo.read()
            self.crearLista(contenido_archivo)
        except FileNotFoundError:
            print("archivo no encontrado")

    def crearLista(self, contenido_archivo):
        lineas = contenido_archivo.split("\n")
        for linea in lineas:
                nombre = linea[0:linea.index('=')]
                linea = linea.replace(nombre,"")
                linea = linea.replace("=","")
                primer_comando = re.search("[a-zA-Z]", linea)
                numeros = linea[0:linea.index(primer_comando[0])]
                numeros = numeros.replace(" ", "")
                numeros = numeros.replace("\t", "")
                comandos = linea[linea.index(primer_comando[0]):len(linea)]
Main().menu()
