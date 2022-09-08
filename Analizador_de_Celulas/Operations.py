class Operations:

    def __init__(self):
        self.paciente = []  # -----> [nombre, edad, periodos, dimención, celdas[]]
        self.nombre = ''
        self.edad = 0
        self.periodo = 0
        self.dimencion = 0
        self.celdas = []
        self.fila = 0
        self.columna = 0
        self.tablero = ''
        self.celda = []

    def graficar(self, paciente):
        self.paciente = paciente
        self.nombre = self.paciente[0]
        self.edad = self.paciente[1]
        self.periodo = self.paciente[2]
        self.dimencion = self.paciente[3]
        self.celdas = self.paciente[4]
        self.fila = self.columna = self.dimencion

        for linea in range(int(self.fila)):
            self.tablero = self.tablero + '<TR>'
            for nodo in range(int(self.columna)):
                for fila in self.celdas:
                    self.celda = fila
                    if self.celda == [linea, nodo]:
                        self.tablero = self.tablero + '<TD BGCOLOR="black"></TD>'
                self.tablero = self.tablero + '<TD BGCOLOR="white"></TD>'
            self.tablero = self.tablero + '\n'
            self.tablero = self.tablero + '</TR>'
            self.tablero = self.tablero + '\n'
        print(self.celdas)
        print(self.tablero)

    def analizar(self, paciente):
        self.paciente = paciente

    def reportar(self, paciente):
        self.paciente = paciente
