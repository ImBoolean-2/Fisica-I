import tkinter as tk
import random
from PIL import Image, ImageTk
from automovil import Automovil 
from db import Save

class SimulacionGrafica:
    def __init__(self, canvas, app, velocidad_inicial, desaceleracion, coeficiente_friccion, resistencia_aire, peso, gravedad, abs):
        self.canvas = canvas
        self.app = app
        self.auto = Automovil(velocidad_inicial, desaceleracion, coeficiente_friccion, resistencia_aire, peso, gravedad, abs)
        self.auto.x = 0
        self.auto.y = random.randint(50, 550)

        try:
            original_image = Image.open("resources/car.png")
            resized_image = original_image.resize((50, 25))
            self.car_image = ImageTk.PhotoImage(resized_image)
        except FileNotFoundError:
            print("Error: La imagen del automóvil no se encuentra.")
            return
        
        self.car = self.canvas.create_image(self.auto.x, self.auto.y, anchor=tk.NW, image=self.car_image)
        self.info_text = self.canvas.create_text(self.auto.x + 25, self.auto.y - 20, text="", fill="black")
        self.velocidad_text = self.canvas.create_text(self.auto.x + 25, self.auto.y - 40, text="", fill="black")

        self.distancia_frenado = self.auto.calcular_distancia_frenado()
        self.dibujar_lineas(800)
        self.actualizar()

    def actualizar(self):
        tiempo_transcurrido = 1 / 60
        self.auto.mover(tiempo_transcurrido)

        self.canvas.coords(self.car, self.auto.x, self.auto.y)
        self.canvas.coords(self.info_text, self.auto.x + 25, self.auto.y - 20)
        self.canvas.coords(self.velocidad_text, self.auto.x + 25, self.auto.y - 40)

        self.canvas.itemconfig(self.velocidad_text, text=f"Vel. Inicial: {self.auto.velocidad_inicial:.2f} m/s\nVel. Actual: {self.auto.velocidad_actual:.2f} m/s")

        if self.auto.velocidad_actual <= 0:
            self.auto.velocidad_actual = 0
            self.mostrar_punto_rojo()
            tiempo_frenado = self.auto.calcular_tiempo_frenado()
            self.app.actualizar_resultados(self.auto.x, tiempo_frenado)
            simulador_save = Save(self.auto)
            simulador_save.guardar_en_db()
            self.canvas.itemconfig(self.velocidad_text, text="")
        else:
            if self.auto.x > self.canvas.winfo_width() - 50:
                nuevo_scrollregion_x = int(self.auto.x + 100)
                self.canvas.config(scrollregion=(0, 0, nuevo_scrollregion_x, self.canvas.winfo_height()))
                self.dibujar_lineas(nuevo_scrollregion_x)

            self.canvas.after(16, self.actualizar)

    def dibujar_lineas(self, ancho_maximo):
        self.canvas.delete("grid_line")  
        for i in range(0, int(ancho_maximo) + 50, 50): 
            self.canvas.create_line(i, 0, i, self.canvas.winfo_height(), fill="lightgray", dash=(5, 2), tags="grid_line")
            self.canvas.create_text(i + 10, 10, text=f"{i}m", fill="black", tags="grid_line")

    def mostrar_punto_rojo(self):
        punto_rojo = self.canvas.create_oval(self.auto.x - 5, self.auto.y - 5, self.auto.x + 5, self.auto.y + 5, fill="red")
        self.canvas.tag_bind(punto_rojo, "<Enter>", self.mostrar_info)
        self.canvas.tag_bind(punto_rojo, "<Leave>", self.ocultar_info)

    def mostrar_info(self, event):
        info = (f"Distancia de frenado: {self.auto.x:.2f} m\n"
                f"Velocidad Inicial: {self.auto.velocidad_inicial:.2f} m/s\n"
                f"Desaceleración: {self.auto.desaceleracion:.2f} m/s²\n"
                f"Coeficiente de Fricción: {self.auto.coeficiente_friccion:.2f}\n"
                f"Resistencia del Aire: {self.auto.resistencia_aire:.2f}\n"
                f"Peso: {self.auto.peso:.2f} kg\n"
                f"Gravedad: {self.auto.gravedad:.2f} m/s²\n"
                f"ABS: {'Sí' if self.auto.abs else 'No'}")
        self.canvas.itemconfig(self.info_text, text=info)

    def ocultar_info(self, event):
        self.canvas.itemconfig(self.info_text, text="")


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Frenado")

        self.frame_izquierda = tk.Frame(self.root)
        self.frame_izquierda.grid(row=0, column=0, sticky="nsew")

        self.entradas = {}
        self.check_vars = {}
        self.valores_default = {
            "velocidad_entry": 108,
            "desaceleracion_entry": 9.8,
            "coeficiente_friccion_entry": 0.7,
            "resistencia_aire_entry": 0.05,
            "peso_entry": 1000,
            "gravedad_entry": 9.8
        }

        self.crear_entradas()

        self.abs_var = tk.BooleanVar()
        self.abs_checkbutton = tk.Checkbutton(self.frame_izquierda, text="ABS", variable=self.abs_var)
        self.abs_checkbutton.grid(row=len(self.entradas), column=0, columnspan=2, pady=10)

        self.simular_button = tk.Button(self.frame_izquierda, text="Simular", command=self.simular)
        self.simular_button.grid(row=len(self.entradas) + 1, column=0, columnspan=2, pady=20)

        self.resultado_label = tk.Label(self.frame_izquierda, text="")
        self.resultado_label.grid(row=len(self.entradas) + 2, column=0, columnspan=2, pady=10)

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.grid(row=0, column=1, sticky="nsew")

        self.scrollbar = tk.Scrollbar(self.root, orient=tk.HORIZONTAL)
        self.scrollbar.grid(row=1, column=1, sticky="ew")

        self.canvas.config(xscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.canvas.xview)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.establecer_valores_por_defecto()
        self.dibujar_fondo()

    def crear_entradas(self):
        labels = ["Velocidad Inicial (km/h):", "Desaceleración (m/s²):", "Coeficiente de Fricción:", "Resistencia del Aire:", "Peso (kg):", "Gravedad (m/s²):"]
        keys = ["velocidad_entry", "desaceleracion_entry", "coeficiente_friccion_entry", "resistencia_aire_entry", "peso_entry", "gravedad_entry"]

        for i, (label_text, key) in enumerate(zip(labels, keys)):
            label = tk.Label(self.frame_izquierda, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            entry = tk.Entry(self.frame_izquierda)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entradas[key] = entry

            check_var = tk.BooleanVar()
            check_button = tk.Checkbutton(self.frame_izquierda, variable=check_var, command=lambda e=entry, v=check_var, k=key: self.toggle_entry(e, v, k))
            check_button.grid(row=i, column=2, padx=5)
            self.check_vars[key] = check_var

    def toggle_entry(self, entry, check_var, key):
        if check_var.get():
            entry.config(state="disabled")
            entry.delete(0, tk.END)
            entry.insert(0, self.valores_default[key])
        else:
            entry.config(state="normal")

    def establecer_valores_por_defecto(self):
        for key, entry in self.entradas.items():
            entry.delete(0, tk.END)
            entry.insert(0, self.valores_default[key])

    def dibujar_fondo(self):
        self.canvas.delete("all") 
        self.canvas.create_rectangle(0, 0, 800, 600, fill="white")

        for i in range(0, 800, 50):
            self.canvas.create_line(i, 0, i, 600, fill="lightgray", dash=(5, 2))
            self.canvas.create_text(i + 10, 10, text=f"{i}m", fill="black")

        for j in range(0, 600, 50):
            self.canvas.create_line(0, j, 800, j, fill="lightgray")

    def simular(self):
        try:
            velocidad = float(self.entradas["velocidad_entry"].get()) if not self.check_vars["velocidad_entry"].get() else self.valores_default["velocidad_entry"]
            desaceleracion = float(self.entradas["desaceleracion_entry"].get()) if not self.check_vars["desaceleracion_entry"].get() else self.valores_default["desaceleracion_entry"]
            coeficiente_friccion = float(self.entradas["coeficiente_friccion_entry"].get()) if not self.check_vars["coeficiente_friccion_entry"].get() else self.valores_default["coeficiente_friccion_entry"]
            resistencia_aire = float(self.entradas["resistencia_aire_entry"].get()) if not self.check_vars["resistencia_aire_entry"].get() else self.valores_default["resistencia_aire_entry"]
            peso = float(self.entradas["peso_entry"].get()) if not self.check_vars["peso_entry"].get() else self.valores_default["peso_entry"]
            gravedad = float(self.entradas["gravedad_entry"].get()) if not self.check_vars["gravedad_entry"].get() else self.valores_default["gravedad_entry"]
            abs = self.abs_var.get()
    
            self.simulador = SimulacionGrafica(self.canvas, self, velocidad, desaceleracion, coeficiente_friccion, resistencia_aire, peso, gravedad, abs)
        except ValueError:
            self.resultado_label.config(text="Por favor, ingrese valores válidos.")

    def actualizar_resultados(self, x, tiempo_frenado):
        self.resultado_label.config(text=f"Posición X: {x:.2f} metros\nTiempo de Frenado: {tiempo_frenado:.2f} segundos")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
