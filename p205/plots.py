import numpy as np
import matplotlib.pyplot as plt
from p205 import time_kruskal, time_kruskal_2
from p205 import greedy_tsp, dist_matrix
from p205 import len_circuit, exhaustive_tsp
import time

# NO VAAA SERGIO NO VAAAA

def plot_comparison(n_graphs, n_nodes_ini, n_nodes_fin, step):
    sizes = list(range(n_nodes_ini, n_nodes_fin + 1, step))

    # Tiempos de ejecución de Kruskal
    kruskal_times = time_kruskal(n_graphs, n_nodes_ini, n_nodes_fin, step)

    # Tiempos de ejecución de Greedy TSP
    tsp_greedy_times = []
    for size in sizes:
        dist_matrix_greedy = dist_matrix(size)
        start = time.time()
        greedy_tsp(dist_matrix_greedy)
        end = time.time()
        tsp_greedy_times.append(end - start)

    # Tiempos de ejecución de Exhaustive TSP
    tsp_exhaustive_times = []
    for size in sizes:
        dist_matrix_exhaustive = dist_matrix(size)
        start = time.time()
        exhaustive_tsp(dist_matrix_exhaustive)
        end = time.time()
        tsp_exhaustive_times.append(end - start)

    # Crear gráficos
    plt.plot(sizes, kruskal_times, label='Kruskal')
    plt.plot(sizes, tsp_greedy_times, label='Greedy TSP')
    plt.plot(sizes, tsp_exhaustive_times, label='Exhaustive TSP')

    plt.xlabel('Número de nodos')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de Kruskal y TSP en función del tamaño del grafo')
    plt.legend()
    plt.show()

# Parámetros de prueba
n_graphs = 10
n_nodes_ini = 5
n_nodes_fin = 20
step = 5