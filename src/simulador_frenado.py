import tkinter as tk

ANCHO_VENTANA = 800
ALTO_VENTANA = 600
COLOR_FONDO = "white"
COLOR_AUTO = "blue"

class Automovil:
    def __init__(self, velocidad_inicial, desaceleracion):
        self.velocidad_inicial = velocidad_inicial
        self.velocidad_actual = velocidad_inicial
        self.desaceleracion = desaceleracion
        self.x = 50  
        self.y = ALTO_VENTANA // 2 - 25 
        self.ancho = 50
        self.alto = 25

    def mover(self, tiempo_transcurrido):
        if self.velocidad_actual > 0:
            self.velocidad_actual -= self.desaceleracion * tiempo_transcurrido
            if self.velocidad_actual < 0:
                self.velocidad_actual = 0
        self.x += self.velocidad_actual * tiempo_transcurrido

    def calcular_distancia_frenado(self):
        return (self.velocidad_inicial ** 2) / (2 * self.desaceleracion)

class SimulacionGrafica:
    def __init__(self, root, velocidad_inicial, desaceleracion):
        self.root = root
        self.canvas = tk.Canvas(root, width=ANCHO_VENTANA, height=ALTO_VENTANA, bg=COLOR_FONDO)
        self.canvas.pack()

        # Título
        self.titulo = tk.Label(root, text="Simulación de Frenado", font=("Helvetica", 16))
        self.titulo.pack(pady=10)

        # Información
        self.info = tk.Label(root, text=f"Velocidad Inicial: {velocidad_inicial} km/h, Desaceleración: {desaceleracion} m/s²", font=("Helvetica", 12))
        self.info.pack(pady=10)

        self.auto = Automovil(velocidad_inicial, desaceleracion)
        self.rect = self.canvas.create_rectangle(self.auto.x, self.auto.y, self.auto.x + self.auto.ancho, self.auto.y + self.auto.alto, fill=COLOR_AUTO)
        self.actualizar()

    def actualizar(self):
        tiempo_transcurrido = 1 / 60  # Aproximadamente 60 FPS
        self.auto.mover(tiempo_transcurrido)
        self.canvas.coords(self.rect, self.auto.x, self.auto.y, self.auto.x + self.auto.ancho, self.auto.y + self.auto.alto)
        if self.auto.velocidad_actual > 0:
            self.root.after(16, self.actualizar)  # Llamar a actualizar de nuevo después de 16 ms (~60 FPS)

def iniciar_simulacion_grafica(velocidad_inicial, desaceleracion):
    root = tk.Tk()
    root.title("Simulación de Frenado")
    simulacion = SimulacionGrafica(root, velocidad_inicial, desaceleracion)
    root.mainloop()