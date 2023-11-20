import numpy as np
import matplotlib.pyplot as plt
from p205 import time_kruskal, time_kruskal_2
import time


def plot_comparison(n_graphs, n_nodes_ini, n_nodes_fin, step):
    number_of = int((n_nodes_fin - n_nodes_ini)/step)
    n_each = int(n_graphs/number_of)

    

    sizes = [i for i in range(n_nodes_ini, n_nodes_fin+n_nodes_ini, step)]

    # Tiempos de ejecución de Kruskal
    kruskal_times = time_kruskal(n_graphs, n_nodes_ini, n_nodes_fin, step)
    kruskal_times_2 = time_kruskal_2(n_graphs, n_nodes_ini, n_nodes_fin, step)

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, kruskal_times,  marker='o', label='Kruskal')
    plt.xlabel('Número de nodos')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de Kruskal en función del tamaño del grafo')
    plt.legend()
    plt.grid(True)
    plt.savefig('kruskal_times.png')
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, kruskal_times_2,  marker='o', label='Kruskal 2 (CD)')
    plt.xlabel('Número de nodos')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de Kruskal en función del tamaño del grafo')
    plt.legend()
    plt.grid(True)
    plt.savefig('kruskal_2_times.png')
    plt.close()

# Parámetros de prueba
if __name__=='__main__':
    n_graphs = 500
    n_nodes_ini = 10
    n_nodes_fin = 500
    step = 10

    plot_comparison(n_graphs, n_nodes_ini, n_nodes_fin, step)