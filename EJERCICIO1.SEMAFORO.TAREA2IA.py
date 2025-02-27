import time
import random

class Semaforo:
    def __init__(self):
        self.estado = "Rojo"
        self.tiempo_espera = {"Verde": 4, "Amarillo": 3, "Rojo": 4}
    
    def detectar_trafico(self):
        """Simula la detección de vehículos en la vía."""
        return random.randint(0, 10)  # Número aleatorio de vehículos detectados
    
    def ajustar_tiempo(self, vehiculos):
        """cambio la duración de la luz verde según el tráfico."""
        if vehiculos > 8:
            self.tiempo_espera["Verde"] = 7
        elif vehiculos > 5:
            self.tiempo_espera["Verde"] = 3
        else:
            self.tiempo_espera["Verde"] = 2
    
    def cambiar_estado(self):
        """Cambia el estado del semáforo secuencialmente."""
        if self.estado == "Rojo":
            vehiculos = self.detectar_trafico()
            self.ajustar_tiempo(vehiculos)
            print(f"Detectados {vehiculos} vehículos. Duración de luz verde: {self.tiempo_espera['Verde']} segundos.")
            self.estado = "Verde"
        elif self.estado == "Verde":
            self.estado = "Amarillo"
        elif self.estado == "Amarillo":
            self.estado = "Rojo"
    
    def ejecutar(self):
        """Ejecuta la simulación del semáforo."""
        while True:
            print(f"Semáforo en {self.estado}")
            time.sleep(self.tiempo_espera[self.estado])
            self.cambiar_estado()

if __name__ == "__main__":
    semaforo = Semaforo()
    semaforo.ejecutar()