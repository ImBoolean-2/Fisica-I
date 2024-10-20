class Automovil:
    def __init__(self, velocidad_inicial, desaceleracion, coeficiente_friccion, resistencia_aire, peso, gravedad=9.8, abs=False):
        if any(param < 0 for param in [velocidad_inicial, desaceleracion, coeficiente_friccion, resistencia_aire, peso]):
            raise ValueError("Los parámetros deben ser mayores o iguales a cero.")

        self.velocidad_inicial = velocidad_inicial
        self.velocidad_actual = velocidad_inicial
        self.desaceleracion = desaceleracion
        self.coeficiente_friccion = coeficiente_friccion
        self.resistencia_aire = resistencia_aire
        self.peso = peso
        self.gravedad = gravedad
        self.abs = abs
        self.x = 50  
        self.y = 300
        self.ancho = 50
        self.alto = 25
    
    def calcular_distancia_frenado(self):
        a = self.calcular_desaceleracion_total()
        if a <= 0:
            return float('inf')
        return self.velocidad_inicial ** 2 / (2 * a)
    
    def calcular_tiempo_frenado(self):
        a = self.calcular_desaceleracion_total()
        if a <= 0:
            return float('inf')
        return self.velocidad_inicial / a

    def mover(self, tiempo_transcurrido):
        if tiempo_transcurrido <= 0:
            raise ValueError("El tiempo transcurrido debe ser mayor que cero.")
        
        desaceleracion_total = self.calcular_desaceleracion_total()
        
        if self.velocidad_actual > 0:
            self.velocidad_actual -= desaceleracion_total * tiempo_transcurrido
            if self.velocidad_actual < 0:
                self.velocidad_actual = 0
        self.x += self.velocidad_actual * tiempo_transcurrido

    def calcular_desaceleracion_total(self):
        g = self.gravedad
        peso = self.peso
        fuerza_friccion = self.coeficiente_friccion * peso * g
        desaceleracion_friccion = fuerza_friccion / peso
        
        if not (0 <= self.resistencia_aire <= 1):
            raise ValueError("La resistencia del aire debe estar entre 0 y 1.")
        
        desaceleracion_total = desaceleracion_friccion + self.resistencia_aire
        if self.abs:
            desaceleracion_total *= 1.231  # 23.1% más eficiente
            
        return desaceleracion_total

    def __str__(self):
        return (f"Automóvil: velocidad_actual={self.velocidad_actual:.2f} m/s, "
                f"posicion=({self.x:.2f}, {self.y:.2f}), "
                f"peso={self.peso} kg, "
                f"coeficiente_friccion={self.coeficiente_friccion}, "
                f"resistencia_aire={self.resistencia_aire}, "
                f"gravedad={self.gravedad} m/s², "
                f"ABS={'Activado' if self.abs else 'Desactivado'}")
