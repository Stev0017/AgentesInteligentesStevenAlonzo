import random
import time

class AgenteBusqueda:
    def __init__(self, size=5):
        self.size = size
        self.grid = [["." for _ in range(size)] for _ in range(size)]
        self.agent_pos = [0, 0]
        self.object_pos = [random.randint(0, size - 1), random.randint(0, size - 1)]
        self.grid[self.object_pos[0]][self.object_pos[1]] = "X"
    
    def mostrar_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                if [i, j] == self.agent_pos:
                    print("Y", end=" ")
                else:
                    print(self.grid[i][j], end=" ")
            print()
        print("-" * 10)
    
    def mover_agente(self):
        while self.agent_pos != self.object_pos:
            time.sleep(0.5)
            if self.agent_pos[0] < self.object_pos[0]:
                self.agent_pos[0] += 1
            elif self.agent_pos[0] > self.object_pos[0]:
                self.agent_pos[0] -= 1
            elif self.agent_pos[1] < self.object_pos[1]:
                self.agent_pos[1] += 1
            elif self.agent_pos[1] > self.object_pos[1]:
                self.agent_pos[1] -= 1
            self.mostrar_grid()
        print("¡Objeto encontrado!")

if __name__ == "__main__":
    agente = AgenteBusqueda()
    agente.mostrar_grid()
    agente.mover_agente()