from xml.dom import minidom
from colorama import Fore
from TDA import SCList
from Operations import Operations


class XML:

    def __init__(self):
        self.ruta_xml = ''  # -----> Guardara la dirección del archivo XML
        self.paciente = []  # -----> Contendra toda la información de 1 paciente
        self.celda = []  # -----> Contendra la posición (x,y) de 1 celda
        self.lista_celdas = []  # -----> Es una lista con todas las celdas
        self.nombres = SCList()  # -----> Es una lista con los nombres de los pacientes
        self.pacientes = SCList()  # -----> Es una lista de todos los pacientes (posición, paciente)
        self.operaciones = Operations()  # -----> Es un objeto encargado de graficar

    def leer_xml(self, ruta):
        n = 1
        self.ruta_xml = ruta
        xml = minidom.parse(self.ruta_xml)
        pacientes = xml.getElementsByTagName('paciente')

        for i in pacientes:
            nombre = i.getElementsByTagName('nombre')[0]
            self.paciente.append(nombre.firstChild.data)
            self.nombres.agregar_fin(f'{n}) {nombre.firstChild.data}')
            edad = i.getElementsByTagName('edad')[0]
            self.paciente.append(edad.firstChild.data)
            periodos = i.getElementsByTagName('periodos')[0]
            self.paciente.append(periodos.firstChild.data)
            dimencion = i.getElementsByTagName('m')[0]
            self.paciente.append(dimencion.firstChild.data)
            lista_celdas = i.getElementsByTagName('celda')

            for celda in lista_celdas:
                fila = celda.getAttribute('f')
                columna = celda.getAttribute('c')
                self.celda.append(fila)
                self.celda.append(columna)
                self.lista_celdas.append(self.celda)
                self.celda = []

            self.paciente.append(self.lista_celdas)
            self.lista_celdas = []
            self.pacientes.agregar_fin(n)
            self.pacientes.agregar_fin(self.paciente)
            self.paciente = []
            n = n + 1

    def mostrar_pacientes(self):
        print('                                              ')
        print(Fore.GREEN+'--> Lista de pacientes disponibles:')
        print('                                              ')
        self.nombres.mostrar_contenido()
        print('                                                 ')
        posicion = input(Fore.CYAN+'--> Seleccione un paciente: ')
        resultado = self.pacientes.buscar(int(posicion))
        if resultado is not None:
            print('       ')
            print(resultado)
        self.operaciones.graficar(resultado)
        self.operaciones.analizar(resultado)
        self.operaciones.reportar(resultado)
