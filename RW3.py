import json
import random
import numpy as np
import matplotlib.pyplot as plt
import time

# Cargar números del archivo numbers.json
with open('PseudoRandomNumbers.json', 'r') as file:
    data = json.load(file)
    numbers = data['numbers']

def random_walk_3d(xi, yi, zi):
    """
    Realiza una caminata en tres dimensiones partiendo de una posición inicial.

    :param xi: Coordenada x inicial.
    :param yi: Coordenada y inicial.
    :param zi: Coordenada z inicial.
    :return: Tupla con la posición final y el tiempo de procesamiento.
    """
    start_time = time.time()

    x, y, z = xi, yi, zi
    xf, yf, zf = np.zeros(shape=len(numbers)), np.zeros(shape=len(numbers)), np.zeros(shape=len(numbers))

    for i in range(len(numbers)):
        # Uso de random para escoger al azar mis numeros pseudoaleatorios para elegir la dirección de movimiento
        rand_num = random.choice(numbers)
        if rand_num < 1 / 6:
            dx, dy, dz = (0, 1, 0)  # Arriba
        elif rand_num < 2 / 6:
            dx, dy, dz = (0, -1, 0)  # Abajo
        elif rand_num < 3 / 6:
            dx, dy, dz = (1, 0, 0)  # Derecha
        elif rand_num < 4 / 6:
            dx, dy, dz = (-1, 0, 0)  # Izquierda
        elif rand_num < 5 / 6:
            dx, dy, dz = (0, 0, 1)  # Adelante
        else:
            dx, dy, dz = (0, 0, -1)  # Atrás

        x += dx
        xf[i] = x
        y += dy
        yf[i] = y
        z += dz
        zf[i] = z
        print("Paso " + str(i + 1) + " = (x,y,z) = (" + str(x) + "," + str(y) + "," + str(z) + ")")
        if (x, y, z) == (45, 23, 17):
            print(f"La rana llegó a la posición (45, 23, 17) en {i + 1} pasos.")
            break

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xf, yf, zf, "b")
    plt.show()

    end_time = time.time()
    processing_time = end_time - start_time
    return (x, y, z), processing_time

walk, time_taken = random_walk_3d(0, 0, 0)
print("\nDistancia del origen = " + str((walk[0] ** 2 + walk[1] ** 2 + walk[2] ** 2) ** 0.5) + " Unidades")
print(f"Tiempo de procesamiento: {time_taken} segundos")
