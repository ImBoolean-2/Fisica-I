import sqlite3
import os

class Simulador:
    def __init__(self, automovil):
        self.automovil = automovil

    def ejecutar_simulacion(self):
        distancia_frenado = self.automovil.calcular_distancia_frenado()
        return distancia_frenado

    def guardar_en_db(self):
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/simulaciones.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Crear la tabla si no existe
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS simulaciones (
                id INTEGER PRIMARY KEY,
                velocidad REAL,
                desaceleracion REAL,
                coeficiente_friccion REAL,
                resistencia_aire REAL,
                distancia REAL
            )
        ''')
        
        # Insertar los datos en la tabla
        cursor.execute('''
            INSERT INTO simulaciones (velocidad, desaceleracion, coeficiente_friccion, resistencia_aire, distancia)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.automovil.velocidad_inicial, self.automovil.desaceleracion, self.automovil.coeficiente_friccion, self.automovil.resistencia_aire, self.ejecutar_simulacion()))
        
        conn.commit()
        conn.close()