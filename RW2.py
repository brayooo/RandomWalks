import json
import random
import time

import numpy as np
import matplotlib.pyplot as plt

# Cargar números del archivo numbers.json
with open('PseudoRandomNumbers.json', 'r') as file:
    data = json.load(file)
    numbers = data['numbers']


def random_walk(xi, yi):
    """
    Realiza una caminata en dos dimensiones partiendo de una posición inicial.

    :param xi: Coordenada x inicial.
    :param yi: Coordenada y inicial.
    :return: Tupla con la posición final y el tiempo de procesamiento.
    """
    start_time = time.time()

    x, y = xi, yi
    xf, yf = np.zeros(shape=(len(numbers))), np.zeros(shape=(len(numbers)))

    for i in range(len(numbers)):
        # Uso de random para escoger al azar mis numeros pseudoaleatorios para elegir la dirección de movimiento
        rand_num = random.choice(numbers)
        if rand_num < 0.25:
            dx, dy = (0, 1)  # Arriba
        elif rand_num < 0.5:
            dx, dy = (0, -1)  # Abajo
        elif rand_num < 0.75:
            dx, dy = (1, 0)  # Derecha
        else:
            dx, dy = (-1, 0)  # Izquierda
        x += dx
        xf[i] = x
        y += dy
        yf[i] = y
        print("Paso " + str(i + 1) + " = (x,y) = (" + str(x) + "," + str(y) + ")")
        if (x, y) == (250, 300):
            print(f"La rana llegó a la posición (250, 300) en {i + 1} pasos.")
            break

    plt.plot(xf, yf, "b")
    plt.show()

    end_time = time.time()
    processing_time = end_time - start_time
    return (x, y), processing_time


walk, time_taken = random_walk(0, 0)
print("\nDistancia del origen = " + str((walk[0] ** 2 + walk[1] ** 2) ** 0.5) + " Unidades")
print(f"Tiempo de procesamiento: {time_taken} segundos")
