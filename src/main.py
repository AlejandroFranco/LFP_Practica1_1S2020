import re
import webbrowser
import tkinter as tk
from tkinter import filedialog

from pip._vendor.distlib.compat import raw_input


class Comando:
    def __init__(self, nombre, parametro):
        self.nombre = nombre
        self.parametro = parametro


class Lista:
    def __init__(self, nombre, numeros, comandos):
        self.nombre = nombre
        self.numeros = numeros
        self.comandos = comandos


class Main:
    listas = []
    contenido_archivo = ""

    def menu(self):
        print("\n")
        print("1 Cargar archivo de entrada")
        print("2 Desplegar listas ordenadas")
        print("3 Desplegar busquedas")
        print("4 Desplegar todas")
        print("5 Desplegar todas al archivo")
        print("6 salir" + "\n")
        entrada = input("Ingrese un numero 1-6" + "\n")
        patron = "[1-6]{1}"
        if re.search(patron, entrada):
            if entrada == "1":
                self.cargarArchivo()
                self.menu()
            elif entrada == "2":
                self.listasOrdenadas()
            elif entrada == "3":
                self.busquedas()
                self.menu()
            elif entrada == "4":
                self.mostrarTodo()
                self.menu()
            elif entrada == "5":
                self.desplegarArchivo()
                self.menu()
            elif entrada == "6":
                print("\n"+"201708993")
                print("Pablo Alejandro Franco Lemus")
                print("alejandrofranco21815@gmail.com")
                print("Lenguajes Formales y de Programación")
                print("-A")
                print("17/02/2021"+"\n")
                raw_input("Presione una tecla"+"\n")
        else:
            self.menu()

    def cadenaMostrarTodo(self):
        cadena_final = ""
        for lista in self.listas:
            cadena_final += "<tr><td>" + lista.nombre + "</td>"
            cadena_final += "<td>" + ','.join(lista.numeros) + "</td>"
            for comando in lista.comandos:
                comando.nombre = re.sub(r"\s+", "", comando.nombre)
                if comando.nombre == "BUSCAR":
                    if comando.parametro in lista.numeros:
                        cadena_final += "<td>" + comando.nombre + " " + comando.parametro + ": " + str([i for i, x in enumerate(lista.numeros) if x == comando.parametro]) + "</td>"
                    else:
                        cadena_final += "<td>" + comando.nombre + ": " + "No encontrado" + "</td>"
                else:
                    a = sorted(lista.numeros, reverse=False)
                    cadena_final += "<td>" + comando.nombre + ": " + ','.join(a) + "</td>"
        cadena_final += "</tr>"
        return cadena_final

    def desplegarArchivo(self):
        archivo = open("modelo.html", "r")
        modelo = archivo.read()
        archivo.close()
        pagina_resultado = open("resultado.html", "w+")
        indice = modelo.index("</table>")
        nuevo_contenido = modelo[0:indice] + self.cadenaMostrarTodo() + modelo[indice:len(modelo)]
        pagina_resultado.write(nuevo_contenido)
        webbrowser.open_new_tab("resultado.html")

    def mostrarTodo(self):
        for lista in self.listas:
            print(lista.nombre)
            for comando in lista.comandos:
                comando.nombre = re.sub(r"\s+", "", comando.nombre)
                if comando.nombre == "BUSCAR":
                    if comando.parametro in lista.numeros:
                        print("Posición: " + str(lista.numeros.index(comando.parametro)))
                    else:
                        print("No encontrado")
                else:
                    a = sorted(lista.numeros, reverse=False)
                    print(*a, sep=", ")
            print("\n")

    def busquedas(self):
        for lista in self.listas:
            for comando in lista.comandos:
                comando.nombre = re.sub(r"\s+", "", comando.nombre)
                if comando.nombre == "BUSCAR":
                    if comando.parametro in lista.numeros:
                        print("Posición: "+str([i for i , x in enumerate(lista.numeros) if x ==comando.parametro]))
                    else:
                        print("No encontrado")

    def listasOrdenadas(self):
        for lista in self.listas:
           for comando in lista.comandos:
               if comando.nombre == "ORDENAR":
                    a = sorted(lista.numeros, reverse=False)
                    print("Lista: " + lista.nombre)
                    print(*a, sep=", ")
                    print("\n")

    def cargarArchivo(self):
        root = tk.Tk()
        # root.withdraw()
        nombre_archivo = filedialog.askopenfilename(initialdir="/", title="Seleccionar un archivo",
                                                    filetypes=(("texto", "*.txt"), ("todos", "*.*")))
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
            linea = linea.replace(nombre, "")
            linea = linea.replace("=", "")
            primer_comando = re.search("[a-zA-Z]", linea)
            numeros = linea[0:linea.index(primer_comando[0])]
            numeros = numeros.replace(" ", "")
            numeros = numeros.replace("\t", "")
            cadena_comandos = linea[linea.index(primer_comando[0]):len(linea)]
            comandos = cadena_comandos.split(",")
            lista_comandos = []
            for comando in comandos:
                comando = comando.lstrip()
                if re.search("[0-9]+", comando[len(comando) - 1:len(comando)]):
                    nombre_comando = comando[0:7]
                    parametro_comando = comando[7:len(comando)]
                else:
                    nombre_comando = comando[0:8]
                    parametro_comando = ""
                lista_comandos.append(Comando(nombre_comando, parametro_comando))
            self.listas.append(Lista(nombre, numeros.split(","), lista_comandos))

Main().menu()