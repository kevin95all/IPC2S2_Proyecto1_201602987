from tkinter import *
from tkinter import filedialog
from colorama import Fore
from XML import XML


class Main:

    def __init__(self):
        self.ruta = ''
        self.op = ''
        self.salida = False
        self.paciente_seleccionado = False
        self.archivo = XML()

    def menu_principal(self):
        while not self.salida:
            print('                                          ')
            print('┌------------ MENU PRINCIPAL ------------┐')
            print('|                                        |')
            print('|        1)   Cargar archivo             |')
            print('|        2)   Seleccionar paciente       |')
            print('|        3)   Seleccionar celula         |')
            print('|        4)   Analizar paciente          |')
            print('|        5)   Generar reporte            |')
            print('|        6)   Salir                      |')
            print('|                                        |')
            print('└----------------------------------------┘')
            print('                                          ')

            self.op = input('--> Ingrese una opción: ')

            if self.op == '1':
                self.cargar_archivo()
            elif self.op == '2':
                pass
            elif self.op == '3':
                pass
            elif self.op == '4':
                pass
            elif self.op == '5':
                pass
            elif self.op == '6':
                self.salir()
            else:
                print('                    ')
                print('--> Opción no valida')

    def cargar_archivo(self):
        ventana = Tk()
        respaldo = self.ruta
        self.ruta = ''

        self.ruta = filedialog.askopenfilename(
            title='Buscar archivo',
            filetypes=[
                ('Archivos xml', '*.xml'),
                ('Todos los archivos', '*.*')
            ]
        )
        if self.ruta == '':
            self.ruta = respaldo
            print('                              ')
            print('--> No se cargo ningun archivo')
        else:
            self.archivo.leer_xml(self.ruta)
            print('                             ')
            print('--> Archivo cargado con exito')
        ventana.mainloop()

    def salir(self):
        print('                                ')
        print(Fore.RED+'--> Programa finalizado')
        self.ruta = ''
        self.op = ''
        self.paciente_seleccionado = False
        self.salida = True


app = Main()
app.menu_principal()
