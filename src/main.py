import tkinter as tk
import random
from PIL import Image, ImageTk
from automovil import Automovil
from simulador import Simulador

class SimulacionGrafica:
    def __init__(self, canvas, velocidad_inicial, desaceleracion, coeficiente_friccion, resistencia_aire):
        self.canvas = canvas
        self.auto = Automovil(velocidad_inicial, desaceleracion, coeficiente_friccion, resistencia_aire)
        self.auto.x = 0
        self.auto.y = random.randint(50, 550) 
        
        original_image = Image.open("resources/car.png")
        resized_image = original_image.resize((50, 25)) 
        self.car_image = ImageTk.PhotoImage(resized_image)
        self.car = self.canvas.create_image(self.auto.x, self.auto.y, anchor=tk.NW, image=self.car_image)
        
        self.info_text = self.canvas.create_text(self.auto.x + 25, self.auto.y - 20, text="", fill="black")
        self.actualizar()

    def actualizar(self):
        tiempo_transcurrido = 1 / 60 
        self.auto.mover(tiempo_transcurrido)
        self.canvas.coords(self.car, self.auto.x, self.auto.y)
        info = f"X: {self.auto.x:.2f} m\nVelocidad: {self.auto.velocidad_actual:.2f} m/s\nDesaceleración: {self.auto.desaceleracion} m/s²"
        self.canvas.coords(self.info_text, self.auto.x + 25, self.auto.y - 20)
        self.canvas.itemconfig(self.info_text, text=info)
        
        if self.auto.velocidad_actual > 0:
            self.canvas.after(16, self.actualizar)
        else:
            self.punto_rojo = self.canvas.create_oval(self.auto.x - 5, self.auto.y - 5, self.auto.x + 5, self.auto.y + 5, fill="red")
            self.canvas.tag_bind(self.punto_rojo, "<Enter>", self.mostrar_info)
            self.canvas.tag_bind(self.punto_rojo, "<Leave>", self.ocultar_info)

    def mostrar_info(self, event):
        self.canvas.itemconfig(self.info_text, state="normal")

    def ocultar_info(self, event):
        self.canvas.itemconfig(self.info_text, state="hidden")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Frenado de Automóvil")
        self.root.geometry("1200x700")

        self.entradas = {}
        elementos = [
            ("Velocidad Inicial (km/h):", "velocidad_entry"),
            ("Desaceleración (m/s²):", "desaceleracion_entry"),
            ("Coeficiente de Fricción:", "coeficiente_friccion_entry"),
            ("Resistencia del Aire:", "resistencia_aire_entry")
        ]

        for i, (texto, nombre) in enumerate(elementos):
            label = tk.Label(self.root, text=texto)
            label.grid(row=i, column=0, padx=10, pady=10, sticky="e")
            entry = tk.Entry(self.root)
            entry.grid(row=i, column=1, padx=10, pady=10)
            self.entradas[nombre] = entry

        self.simular_button = tk.Button(self.root, text="Simular", command=self.simular)
        self.simular_button.grid(row=len(elementos), column=0, columnspan=2, pady=20)

        self.resultado_label = tk.Label(self.root, text="")
        self.resultado_label.grid(row=len(elementos) + 1, column=0, columnspan=2, pady=10)

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.grid(row=0, column=2, rowspan=len(elementos) + 2, padx=20, pady=20)

        self.dibujar_medidas()

    def dibujar_medidas(self):
        for i in range(0, 801, 50): 
            self.canvas.create_line(i, 0, i, 600, dash=(2, 2), fill="gray")
            self.canvas.create_text(i, 10, text=f"{i} m", fill="black")

    def simular(self):
        try:
            velocidad = float(self.entradas["velocidad_entry"].get())
            desaceleracion = float(self.entradas["desaceleracion_entry"].get())
            coeficiente_friccion = float(self.entradas["coeficiente_friccion_entry"].get())
            resistencia_aire = float(self.entradas["resistencia_aire_entry"].get())
            
            auto = Automovil(velocidad, desaceleracion, coeficiente_friccion, resistencia_aire)
            simulador = Simulador(auto)
            
            distancia_frenado = simulador.ejecutar_simulacion()
            self.resultado_label.config(text=f"Distancia de Frenado: {distancia_frenado:.2f} metros")
            
            simulador.guardar_en_db()
            
            SimulacionGrafica(self.canvas, velocidad, desaceleracion, coeficiente_friccion, resistencia_aire)
        except ValueError:
            self.resultado_label.config(text="Por favor, ingrese valores válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()