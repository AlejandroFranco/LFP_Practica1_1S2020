import re
import tkinter as tk
from tkinter import filedialog

def menu():
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
            cargarArchivo()
        #
        # elif entrada == "2":
        #
        # elif entrada == "3":
        #
        # elif entrada == "4":
        #
        # elif entrada == "5":
        #
        # elif entrada == "6":

    else:
        menu()


def cargarArchivo():
    root = tk.Tk()
    root.withdraw()
    nombre_archivo = filedialog.askopenfilename(initialdir="/", title="Seleccionar un archivo", filetypes=(("texto","*.txt"),("todos","*.*")))
    try:
        contenido = open(nombre_archivo,"r")
    except FileNotFoundError:
        print("archivo no encontrado")



menu()