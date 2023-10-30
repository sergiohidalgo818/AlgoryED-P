import numpy as np
import itertools
from typing import List, Dict, Callable, Iterable, Tuple
import queue
from queue import PriorityQueue
import random

# I - A


def init_cd(n: int) -> np.ndarray:
    if n <= 0:
        return np.array([])

    array = np.array([-1 for i in range(n)])
    return array


def union(rep_1: int, rep_2: int, p_cd: np.ndarray) -> int:

    if p_cd[rep_2] < p_cd[rep_1]:  # el representante 2 tiene mayor rango
        # por tanto el representante 2 pasa a ser el padre del 1
        p_cd[rep_1] = rep_2
        return rep_2
    elif p_cd[rep_2] > p_cd[rep_1]:  # el representante 1 tiene mayor rango
        # por tanto el representante 1 pasa a ser el padre del 2
        p_cd[rep_2] = rep_1
        return rep_1
    else:  # ambos representantes tienen mismo rango
        p_cd[rep_2] = rep_1  # da igual cual será el nuevo padre
        p_cd[rep_1] -= 1  # se selecciona el 1 como padre del 2
        return rep_1


def find(ind: int, p_cd: np.ndarray) -> int:

    z = ind
    # mientras no se haya encontrado el representane
    while p_cd[z] >= 0:
        # se irá subiendo en el arbol
        z = p_cd[z]

    # se comprime el camino
    while p_cd[ind] >= 0:
        # y es el padre/rango de la posicion ind
        y = p_cd[ind]
        # se cambiara por z(el nuevo representante)
        p_cd[ind] = z
        # y pasará a ser el nuevo indice
        ind = y
    return z

# II - A


def create_pq(n: int, l_g: List) -> queue.PriorityQueue:
    if n <= 0 or len(l_g) <= 0:
        return PriorityQueue(0)

    # l_g -> (ramax, ramay, peso)
    queue = PriorityQueue(n)
    # se insertan los nodos en la cola de prioridad
    for i in range(n):
        # donde el formato es (priority, data)
        # l_g[i][2] es el peso
        # l_g[i][0] y l_g[i][1] representan las ramas
        queue.put((l_g[i][2], (l_g[i][0], l_g[i][1])))


def kruskal(n: int, l_g: List) -> Tuple[int, List]:
    l_t = []  # nuevo grafo
    cd = init_cd(n)  # se inicializa el conjunto disjunto
    queue = create_pq(n, l_g)  # se inicializa la cola de prioridad
    while not queue.empty():  # mientras dicha cola no este vacia
        _, (u, v) = queue.get()  # se popean los vertices
        x = find(u, cd)  # se busca por una rama
        y = find(v, cd)  # y uego por otra rama
        if x != y:
            l_t.append((u, v))  # si son distintos se introduce tal cual
        union(x, y, cd)  # se hace la union de ambos
    return (n, l_t)


# II - B

def complete_graph(n_nodes: int, max_weight=50)-> Tuple[int, List]:
    graph_gen = list()
    
    for i in n_nodes:

        w = random.randint(1, max_weight)

def time_kruskal(n_graphs: int, n_nodes_ini: int, n_nodes_fin: int, step: int)-> List:
    pass

def time_kruskal_2(n_graphs: int, n_nodes_ini: int, n_nodes_fin: int, step: int)-> List:
    pass