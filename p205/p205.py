"""
Ejercicio p205.py
Autores: Sergio Hidalgo y Miguel Ibanez
"""
import itertools
from typing import Tuple
from queue import PriorityQueue
import itertools
import queue
import random
import timeit
import time
import numpy as np

TIMES_EXEC = 1000

# I - A


def init_cd(n: int) -> np.ndarray:
    """
    Esta funcion inicializa el conjunto disjunto.
    Args:
        n: Tamaño array
    Returns:
        array: Una array con el conjunto inicializado
    """
    if n <= 0:
        return np.array([])

    array = np.array([-1 for i in range(n)])
    return array


def union(rep_1: int, rep_2: int, p_cd: np.ndarray) -> int:
    """
    Esta funcion realiza la union.
    Args:
        rep_1: Representante conjunto 1
        rep_2: Representante conjunto 2
        p_cd: Array del conjunto disjunto
    Returns:
        rep_1: El nuevo representante
    """
    if p_cd[rep_2] < p_cd[rep_1]:  # el representante 2 tiene mayor rango
        # por tanto el representante 2 pasa a ser el padre del 1
        p_cd[rep_1] = rep_2
        return rep_2
    if p_cd[rep_2] > p_cd[rep_1]:  # el representante 1 tiene mayor rango
        # por tanto el representante 1 pasa a ser el padre del 2
        p_cd[rep_2] = rep_1
        return rep_1
    # ambos representantes tienen mismo rango
    p_cd[rep_2] = rep_1  # da igual cual será el nuevo padre
    p_cd[rep_1] -= 1  # se selecciona el 1 como padre del 2
    return rep_1


def find(ind: int, p_cd: np.ndarray) -> int:
    """
    Esta funcion realiza la busqueda.
    Args:
        ind: Representante a buscar
        p_cd: Array del conjunto disjunto
    Returns:
        z: El indice del representante
    """
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


def create_pq(n: int, l_g: list) -> queue.PriorityQueue:
    """
    Esta funcion inicializa la cola de prioridad.
    Args:
        n: Tamaño de la cola
        l_g: Lista de nodos que representa un grafo
    Returns:
        queue: La cola de prioridad
    """
    if n <= 0 or len(l_g) <= 0:
        return PriorityQueue(0)

    # l_g -> (ramax, ramay, peso)
    queue = PriorityQueue(n)
    # se insertan los nodos en la cola de prioridad
    for elem in l_g:
        (a, b, c) = elem
        # donde el formato es (priority, data)
        queue.put((c, (a, b)))
    return queue


def kruskal(n: int, l_g: list) -> Tuple[int, list]:
    """
    Esta funcion realiza el algoritmo de kruskal.
    Args:
        n: Tamaño de la lista
        l_g: Lista de nodos que representa un grafo
    Returns:
        tam_list_tuple: Una tupla del tamaño y la lista resultante
    """
    l_t = []  # nuevo grafo
    cd = init_cd(n)  # se inicializa el conjunto disjunto
    queue = create_pq(n, l_g)  # se inicializa la cola de prioridad
    while not queue.empty():  # mientras dicha cola no este vacia
        w, (u, v) = queue.get()  # se popean los vertices
        x = find(u, cd)  # se busca por una rama
        y = find(v, cd)  # y uego por otra rama
        if x != y:
            l_t.append((u, v, w))  # si son distintos se introduce tal cual
            union(x, y, cd)  # se hace la union de ambos

    while not queue.empty():
        queue.get()

    if len(l_t) < n-1:
        return None
    
    return (n, l_t)


# II - B

def complete_graph(n_nodes: int, max_weight=50) -> Tuple[int, list]:
    """
    Esta funcion genera un grafo con pesos pseudoaleatorios.
    Args:
        n_nodes: Numero de nodos
        max_weight: Peso maximo
    Returns:
        graph_gen: Una tupla del numero de nodos y la lista resultante
    """
    graph_gen = list()
    v = n_nodes-1
    for i in range(n_nodes):
        u = i
        for j in range(n_nodes):
            if u < v:
                w = random.randint(1, max_weight)
                graph_gen.append((u, j, w))

    return n_nodes, graph_gen


def time_kruskal(n_graphs: int,
                 n_nodes_ini: int, n_nodes_fin: int, step: int) -> list:
    """
    Esta funcion genera los tiempos que tarda toda la funcion de kruskal.
    Args:
        n_graphs: Numero de grafos
        n_nodes_ini: Numero inicial de nodos
        n_nodes_fin: Numero final de nodos
        step: Salto entre numero de nodos y numero de nodos
    Returns:
        times_list: Una lista con los tiempos resultantes
    """
    graph_list = list()
    incr = n_nodes_ini
    number_of = int((n_nodes_fin - n_nodes_ini)/step)
    n_each = int(n_graphs/number_of)
    incr = n_nodes_ini
    count = 1
    times_list = list()

    # bucle para crear los grafos con distinto numero de nodos
    for i in range(n_graphs):
        graph_list.append(complete_graph(incr))
        if count == n_each:
            incr += step
            count = 0
        count += 1

    count = 1
    val = 0

    # bucle para aplicar kruskal
    for i in graph_list:
        times = timeit.Timer(lambda: kruskal(i[0], i[1]))
        val += times.timeit(TIMES_EXEC)
        count += 1
        if count == n_each:
            times_list.append(val/count)
            count = 0
            val = 0

    return times_list


def kruskal_2(n: int, l_g: list) -> Tuple[int, tuple]:
    """
    Esta funcion realiza el algoritmo de kruskal pero
        en relacion a los conjuntos disjuntos.
    Args:
        n: Tamaño de la lista
        l_g: Lista de nodos que representa un grafo
    Returns:
        times_tam_list: Una tupla de los tiempos y la misma tupla que kruskal
    """
    l_t = []  # nuevo grafo
    cd = init_cd(n)  # se inicializa el conjunto disjunto
    queue = create_pq(n, l_g)  # se inicializa la cola de prioridad
    times = 0
    while not queue.empty():  # mientras dicha cola no este vacia
        _, (u, v) = queue.get()  # se popean los vertices
        
        start = time.time()
        x = find(u, cd)  # se busca por una rama
        y = find(v, cd)  # y luego por otra rama
        if x != y:
            l_t.append((u, v))  # si son distintos se introduce tal cual
            union(x, y, cd)  # se hace la union de ambos
        end = time.time()
        times += end - start
    return (times, (n, l_t))


def time_kruskal_2(n_graphs: int,
                   n_nodes_ini: int, n_nodes_fin: int, step: int) -> list:
    """
    Esta funcion genera los tiempos que tarda toda la funcion de kruskal
        pero en relacion a los conjuntos disjuntos.
    Args:
        n_graphs: Numero de grafos
        n_nodes_ini: Numero inicial de nodos
        n_nodes_fin: Numero final de nodos
        step: Salto entre numero de nodos y numero de nodos
    Returns:
        times_list: Una lista con los tiempos resultantes
    """
    graph_list = list()
    incr = n_nodes_ini
    number_of = int((n_nodes_fin - n_nodes_ini)/step)
    n_each = int(n_graphs/number_of)
    incr = n_nodes_ini
    count = 1
    times_list = list()

    # bucle para crear los grafos con distinto numero de nodos
    for i in range(n_graphs):
        graph_list.append(complete_graph(incr))
        if count == n_each:
            incr += step
            count = 0
        count += 1

    count = 1
    val = 0
    # bucle para aplicar kruskal
    for i in graph_list:
        valaux = 0
        valaux, _ = kruskal_2(i[0], i[1])
        val += valaux
        count += 1
        if count == n_each:
            times_list.append(val/count)
            count = 0
            val = 0

    return times_list

# III - A


def dist_matrix(n_nodes: int, w_max=10) -> np.ndarray:
    """
    Esta funcion genera una matriz de distancias.
    Args:
        n_nodes: Numero de nodes
        w_max: Numero maximo de peso
    Returns:
        m: Una array con las distancias
    """
    m = np.random.randint(1, w_max+1, (n_nodes, n_nodes))
    m = (m + m.T) // 2
    np.fill_diagonal(m, 0)
    return m


def greedy_tsp(dist_m: np.ndarray, node_ini=0) -> list:
    """
    Esta funcion genera un circuito con un algoritmo codicioso.
    Args:
        dist_m: Matriz de distancias
        node_ini: Nodo inicial
    Returns:
        visited_nodes: Una lista con el trayecto
    """
    visited_nodes = list()
    node = node_ini
    node_prov = 0

    while len(visited_nodes) < dist_m.shape[0]:
        max_dist = 9999999
        for i in range(0, dist_m.shape[1]):
            if dist_m[node][i] < max_dist and i not in visited_nodes:
                max_dist = dist_m[node][i]
                node_prov = i

        visited_nodes.append(node_prov)
        node = node_prov

    visited_nodes.append(node_ini)
    return visited_nodes


def len_circuit(circuit: list, dist_m: np.ndarray) -> int:
    """
    Esta funcion mide la longitud de un circuito
    Args:
        circuit: Lista con los nodos del circuito
        dist_m: Matriz de distancias
    Returns:
        circuit_len: La longitud del circuito
    """
    circuit_len = 0

    for i in range(len(circuit)-1):
        circuit_len += dist_m[circuit[i]][circuit[i+1]]

    return circuit_len


def repeated_greedy_tsp(dist_m: np.ndarray) -> list:
    """
    Esta funcion repite el algoritmo anterior
        desde distintos nodos iniciales
    Args:
        dist_m: Matriz de distancias
    Returns:
        final_list: Una lista con todos los circuitos
    """

    final_value = 9999999

    for i in range(0, dist_m.shape[0]):
        aux_list = greedy_tsp(dist_m, i)
        aux_value = len_circuit(aux_list, dist_m)

        if aux_value < final_value:
            final_value = aux_value
            final_list = greedy_tsp(dist_m, i)

    return final_list


def exhaustive_tsp(dist_m: np.ndarray) -> list:
    """
    Esta funcion recorre el todos los posibles
        caminos y escoge el mas corto
    Args:
        dist_m: Matriz de distancias
    Returns:
        final_list: Una lista con todos los circuitos
    """

    # lista de nodos
    list_nodes = [i for i in range(dist_m.shape[0])]
    # todas las permutaciones posibles
    perms = itertools.permutations(list_nodes)

    final_value = 9999999

    for aux_tuple in perms:

        # se forma una lista con todos los elementos de la tupla
        aux_list = [i for i in aux_tuple]
        # se les agrega el primero otra vez
        aux_list.append(aux_list[0])

        # se mide la longitud del circuito
        aux_value = len_circuit(aux_list, dist_m)

        # y se comprueba si es menor que el previo
        if aux_value < final_value:
            final_value = aux_value
            final_list = aux_list.copy()

    return final_list
