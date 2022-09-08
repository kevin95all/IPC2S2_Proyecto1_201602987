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

    def menu_principal(self):  # -----> Metodo para mostrar el menu principal
        while not self.salida:
            print('                                                     ')
            print(Fore.GREEN+'┌------------ MENU PRINCIPAL ------------┐')
            print(Fore.GREEN+'|                                        |')
            print(Fore.GREEN+'|        1)   Cargar archivo             |')
            print(Fore.GREEN+'|        2)   Seleccionar paciente       |')
            print(Fore.GREEN+'|        3)   Mostrar celula             |')
            print(Fore.GREEN+'|        4)   Analizar paciente          |')
            print(Fore.GREEN+'|        5)   Generar reporte            |')
            print(Fore.GREEN+'|        6)   Salir                      |')
            print(Fore.GREEN+'|                                        |')
            print(Fore.GREEN+'└----------------------------------------┘')
            print('                                                     ')

            self.op = input(Fore.CYAN+'--> Ingrese una opción: ')

            if self.op == '1':
                self.cargar_archivo()
            elif self.op == '2':
                self.seleccionar_paciente()
            elif self.op == '3':
                self.mostrar_celula()
            elif self.op == '4':
                self.analizar_paciente()
            elif self.op == '5':
                self.generar_reporte()
            elif self.op == '6':
                self.salir()
            else:
                print('                             ')
                print(Fore.RED+'--> Opción no valida')

    def cargar_archivo(self):  # -----> Metodo para cargar archivos XML
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
            print('                                       ')
            print(Fore.RED+'--> No se cargo ningun archivo')
        else:
            self.archivo.leer_xml(self.ruta)
            print('                                       ')
            print(Fore.CYAN+'--> Archivo cargado con exito')
        ventana.mainloop()

    def seleccionar_paciente(self):  # -----> Metodo para elegir a un paciente
        if self.ruta == '':
            print('                                            ')
            print(Fore.RED+'--> No se ha cargado ningun archivo')
        else:
            self.archivo.mostrar_pacientes()
            self.paciente_seleccionado = True

    def mostrar_celula(self):  # -----> Metodo para mostrar la celula inicial
        if self.ruta == '':
            print('                                            ')
            print(Fore.RED+'--> No se ha cargado ningun archivo')
        else:
            if not self.paciente_seleccionado:
                print('                                              ')
                print(Fore.RED+'--> No se ha seleccionado un paciente')
            else:
                print('                                        ')
                print(Fore.CYAN+'--> Celula principal graficada')

    def analizar_paciente(self):  # -----> Metodo para iniciar el analisis
        if self.ruta == '':
            print('                                            ')
            print(Fore.RED+'--> No se ha cargado ningun archivo')
        else:
            if not self.paciente_seleccionado:
                print('                                              ')
                print(Fore.RED+'--> No se ha seleccionado un paciente')
            else:
                print('                                ')
                print(Fore.CYAN+'--> Paciente analizado')

    def generar_reporte(self):  # -----> Metodo para generar los reportes
        if self.ruta == '':
            print('                                            ')
            print(Fore.RED+'--> No se ha cargado ningun archivo')
        else:
            if not self.paciente_seleccionado:
                print('                                              ')
                print(Fore.RED+'--> No se ha seleccionado un paciente')
            else:
                print('                                        ')
                print(Fore.CYAN+'--> Reporte generado con exito')

    def salir(self):  # -----> Metodo para finalizar el programa
        print('                                ')
        print(Fore.RED+'--> Programa finalizado')
        self.ruta = ''
        self.op = ''
        self.paciente_seleccionado = False
        self.salida = True


app = Main()
app.menu_principal()
