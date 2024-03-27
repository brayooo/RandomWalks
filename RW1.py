import json
from collections import Counter

import numpy as np
import matplotlib.pyplot as plt

# Cargar números del archivo linearCongruentialNumbers.json
with open('PseudoRandomNumbers.json', 'r') as file:
    data = json.load(file)
    numbers = data['numbers']


class RandomWalk1D:
    """
    Clase que simula un  caminata aleatoria en una dimensión.
    """

    def __init__(self, steps):
        """
        Inicializa la simulación de la caminata aleatorio.

        :param steps: Número de pasos a simular.
        """
        self.steps = steps
        self.fmove = []
        self.start_simulation()
        self.show_graphs()

    def start_simulation(self):
        """
        Realiza la simulación del paseo aleatorio.
        """
        Rmove = numbers[:self.steps]
        self.fmove = np.zeros(shape=self.steps)

        move = 0

        for i in range(self.steps):
            if Rmove[i] > 0.5:
                move += 1
                self.fmove[i] = move
            else:
                move -= 1
                self.fmove[i] = move

    def show_graphs(self):
        """
        Muestra gráficos de la trayectoria, frecuencia de posiciones de la caminata aleatorio
        y el punto final a donde llega la rana.
        """
        position_counts = Counter(self.fmove)
        positions = list(position_counts.keys())
        frequencies = list(position_counts.values())

        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        plt.plot(self.fmove, "g")
        plt.xlabel('Step')
        plt.ylabel('Position')
        plt.title('Trajectory of the Random Walk')

        plt.subplot(1, 2, 2)
        plt.bar(positions, frequencies, color='g', alpha=0.7)
        plt.xlabel('Position')
        plt.ylabel('Frequency')
        plt.title('Frequency of Positions in a Single Simulation')

        final_position = self.fmove[-1]
        plt.plot(final_position, position_counts[final_position], 'ro')  # 'ro' means red circle
        plt.text(final_position, position_counts[final_position], f'Final position: {final_position}', ha='center')

        plt.tight_layout()
        plt.show()


RandomWalk1D(1000000)
