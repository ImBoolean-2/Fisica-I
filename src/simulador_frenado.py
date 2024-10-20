class Automovil:
    def __init__(self, velocidad_inicial, desaceleracion, coeficiente_friccion, resistencia_aire, peso, gravedad=9.8, abs=False):
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

    def mover(self, tiempo_transcurrido):
        if self.velocidad_actual > 0:
            self.velocidad_actual -= self.desaceleracion * tiempo_transcurrido
            if self.velocidad_actual < 0:
                self.velocidad_actual = 0
        self.x += self.velocidad_actual * tiempo_transcurrido

    def calcular_desaceleracion_total(self):
        g = self.gravedad
        peso = self.peso
        fuerza_friccion = self.coeficiente_friccion * peso * g
        desaceleracion_friccion = fuerza_friccion / peso
        desaceleracion_total = desaceleracion_friccion + self.resistencia_aire
        if self.abs:
            desaceleracion_total *= 1.231  # 23.1% más eficiente
        return desaceleracion_total

    def calcular_distancia_frenado(self):
        a = self.calcular_desaceleracion_total()
        if a <= 0:
            return float('inf')
        return (self.velocidad_inicial ** 2) / (2 * a)

    def calcular_tiempo_frenado(self):
        a = self.calcular_desaceleracion_total()
        if a <= 0:
            return float('inf')
        return self.velocidad_inicial / a

# Valores extraídos del texto
velocidad_inicial = 50
desaceleracion = 5
coeficiente_friccion = 0.5
resistencia_aire = 0.2
peso = 1000
gravedad = 9.8
abs = False

# Crear objeto Automovil
auto = Automovil(velocidad_inicial, desaceleracion, coeficiente_friccion, resistencia_aire, peso, gravedad, abs)

# Calcular distancia de frenado
distancia_frenado = auto.calcular_distancia_frenado()

print("La distancia de frenado es:", distancia_frenado)