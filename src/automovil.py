class Automovil:
    def __init__(self, velocidad_inicial, desaceleracion, coeficiente_friccion, resistencia_aire):
        self.velocidad_inicial = velocidad_inicial
        self.velocidad_actual = velocidad_inicial
        self.desaceleracion = desaceleracion
        self.coeficiente_friccion = coeficiente_friccion
        self.resistencia_aire = resistencia_aire
        self.x = 50  
        self.y = 300
        self.ancho = 50
        self.alto = 25

    def mover(self, tiempo_transcurrido):
        if self.velocidad_actual > 0:
            self.velocidad_actual -= self.desaceleracion * tiempo_transcurrido
            if self.velocidad_actual < 0:
                self.velocidad_actual = 0
        self.x += self.velocidad_actual * tiempo_transcurrido

    def calcular_distancia_frenado(self):
        desaceleracion_total = self.desaceleracion + self.coeficiente_friccion + self.resistencia_aire
        if desaceleracion_total == 0:
            return float('inf') 
        return (self.velocidad_inicial ** 2) / (2 * desaceleracion_total)