import sqlite3
import os

class Save:
    def __init__(self, automovil):
        self.automovil = automovil

    def ejecutar_simulacion(self):
        """Ejecuta la simulación y devuelve la distancia y el tiempo de frenado."""
        distancia_frenado = self.automovil.calcular_distancia_frenado()
        tiempo_frenado = self.automovil.calcular_tiempo_frenado()
        return distancia_frenado, tiempo_frenado

    def guardar_en_db(self):
        """Guarda los resultados de la simulación en la base de datos."""
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/simulaciones.db')

        # Asegurarse de que el directorio existe
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                
                # Crear la tabla si no existe
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS simulaciones (
                        id INTEGER PRIMARY KEY,
                        velocidad REAL,
                        desaceleracion REAL,
                        coeficiente_friccion REAL,
                        resistencia_aire REAL,
                        peso REAL,
                        gravedad REAL,
                        abs BOOLEAN,
                        distancia REAL,
                        tiempo REAL
                    )
                ''')
                
                # Calcular distancia y tiempo de frenado
                distancia_frenado, tiempo_frenado = self.ejecutar_simulacion()
                
                # Insertar los datos en la tabla
                cursor.execute('''
                    INSERT INTO simulaciones (velocidad, desaceleracion, coeficiente_friccion, resistencia_aire, peso, gravedad, abs, distancia, tiempo)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (self.automovil.velocidad_inicial, self.automovil.desaceleracion, self.automovil.coeficiente_friccion, self.automovil.resistencia_aire, self.automovil.peso, self.automovil.gravedad, self.automovil.abs, distancia_frenado, tiempo_frenado))
                
                print("Simulación guardada con éxito en la base de datos.")
        except sqlite3.Error as e:
            print(f"Error al guardar en la base de datos: {e}")