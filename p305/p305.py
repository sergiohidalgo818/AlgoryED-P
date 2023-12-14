"""
Ejercicio p305.py
Autores: Sergio Hidalgo y Miguel Ibanez
"""

from typing import Tuple, Union, Dict, List
from collections import OrderedDict
import numpy as np
from math import ceil

# I-A

def split(t: np.ndarray) -> Tuple[np.ndarray, int, np.ndarray]:
    """
    Esta funcion reparte los elementos de t entre dos arrays
        con los elementos menores y mayores que el primero.
    Args:
        t: array con los elementos.
    Returns:
        Tuple: Una tupla de los elementos menores, el elemento y los mayores.
    """

    mid = t[0]
    # tabla de los menores y tabla de los mayores con list comprehension
    t_smallers = [u for u in t if u < mid]
    t_greaters = [u for u in t if u > mid]
    return t_smallers, mid, t_greaters


def qsel(t: np.ndarray, k: int) -> Union[int, None]:
    """
    Esta funcion aplica de manera recursiva Quick Select
        usando split.
    Args:
        t: array con los elementos.
        k: posicion del elemento a encontrar (de 0 a len(t).
    Returns:
        Union: De el valor de k si existe y None si no.
    """

    # control de errores
    if k >= len(t):
        return None

    if len(t) == 1 and k == 0:
        return t[0]
    
    # si la lista es menor que CUTOFF se usa np.sort
    if len(t) <= CUTOFF:
        return np.sort(t)[k]

    t_smallers, mid, t_greaters = split(t)
    m = len(t_smallers)

    if k == m:
        return mid
    elif k < m:
        return qsel(t_smallers, k)
    else:
        return qsel(t_greaters, k-m-1)


def qsel_nr(t: np.ndarray, k: int) -> Union[int, None]:
    """
    Esta funcion aplica de manera iterativa Quick Select
        usando split.
    Args:
        t: array con los elementos.
        k: posicion del elemento a encontrar (de 0 a len(t).
    Returns:
        Union: De el valor de k si existe y None si no.
    """

    # control de errores
    if k >= len(t) or k<0:
        return None

    aux_t = t.copy()

    # mientras aux_t tenga mas de un elemento y no sea el primero
    while len(aux_t) > 1 or k > 0:

        # si la lista es menor que CUTOFF se usa np.sort
        if len(t) <= CUTOFF:
            return np.sort(t)[k]
        
        t_smallers, mid, t_greaters = split(aux_t)
        m = len(t_smallers)

        # si k es len(t_smallers)
        if k == m:
            # el numero en la mitad es el buscado
            return mid
        elif k < m:
            # si es menor esta en los pequeños
            aux_t = t_smallers
        else:
            # si es mayor esta en los mayores
            k = k-m-1
            aux_t = t_greaters

    return aux_t[0]


# I-B

CUTOFF = 5
GROUPSIZE = 5

def split_pivot(t: np.ndarray, mid: int) -> Tuple[np.ndarray, int, np.ndarray]:
    """
    Esta funcion reparte los elementos de t entre dos arrays
        con los elementos menores y mayores que el mid.
    Args:
        mid: pivote.
        t: array con los elementos.
    Returns:
        Tuple: Una tupla de los elementos menores, el elemento y los mayores.
    """
    # tabla de los menores y tabla de los mayores con list comprehension
    t_smallers = [u for u in t if u < mid]
    t_greaters = [u for u in t if u > mid]
    return t_smallers, mid, t_greaters



def pivot5(t: np.ndarray) -> int:
    """
    Esta funcion devuelve el pivote.
    Args:
        t: array con los elementos.
    Returns:
        pivot: el pivote.
    """

    # division para comprobar en cuantos grupos se parte
    # y si hay algun grupo que no alcanza el groupsize
    n, remain = divmod(len(t), GROUPSIZE)
    
    # posicion mediana del array
    k = int(ceil(GROUPSIZE/2)) -1

    medians = [np.sort(t[j * GROUPSIZE : (j+1) * GROUPSIZE])[k] for j in range(0, n)]
    
    if remain:
        k = int(ceil(remain/2)) -1
        medians.append(np.sort(t[-remain: ])[k])
    
    
    # posicion mediana de las medianas
    k = int(ceil(len(medians)/2)) - 1   
    
    # si la lista es menor que CUTOFF se usa np.sort
    if len(medians) <= CUTOFF:
        pivot = np.sort(medians)[k] 
    else:
        pivot = qsel5_nr(medians, k)

    return pivot
    
def qsel5_nr(t: np.ndarray, k: int)-> Union[int, None]:
    """
    Esta funcion aplica de manera no recursiva Quick Select 5
        usando split_pivot y pivot5.
    Args:
        t: array con los elementos.
        k: posicion del elemento a encontrar (de 0 a len(t)).
    Returns:
        Union: De el valor de k si existe y None si no.
    """

    # control de errores
    if k >= len(t) or k<0:
        return None

    aux_t = t.copy()
    while len(aux_t) > 1 or k > 0:
        
        # si la lista es menor que CUTOFF se usa np.sort
        if len(aux_t) <= CUTOFF:
            return np.sort(aux_t)[k]

        # busqueda del pivote y particion de la lista
        mid = pivot5(aux_t)
        t_smallers, pivot_value, t_greaters = split_pivot(aux_t, mid)
        
        # misma logica que el quick select tradicional
        m = len(t_smallers)
        if k == m:
            return pivot_value
        
        elif k < m:
            aux_t = t_smallers
        else:
            k = k - m-1 
            aux_t = t_greaters


    return aux_t[0]


# I-C

def qsort_5(t: np.ndarray)-> np.ndarray:
    """
    Esta funcion aplica de manera recursiva Quick Sort 5
        usando split_pivot y pivot5.
    Args:
        t: array con los elementos.
    Returns:
        ndarray: La array ordenada.
    """

    # control de errores
    if len(t) == 0:
        return t


    # si la lista es menor que CUTOFF se usa np.sort
    if len(t) <= CUTOFF:
        return np.sort(t)
    
    # busqueda del pivote y particion de la lista
    mid = pivot5(t)
    t_smallers, pivot_value, t_greaters = split_pivot(t, mid)

    # se une a los pequeños el pivote y a la array resultante, los mayores
    return  np.append(np.append(qsort_5(t_smallers), pivot_value), qsort_5(t_greaters))


# II-A
def change_pd(c: int, l_coins: list[int])-> np.ndarray:
    """
    Esta funcion aplica el algoritmo change con
        programacion dinamica.
    Args:
        c: cantidad optima de monedas.
        l_coins: lista de monedas.
    Returns:
        ndarray: La array generada.
    """
    # En n obtenemos la cantidad de monedas en la lista
    n = len(l_coins)

    #Creamos una matriz llena de ceros de tam cantidad de monedas / cantidad optima
    dp = np.zeros((n + 1, c + 1), dtype=int)

    # Inicializamos la primera fila de la matriz con valores cantidad optima + 1
    for i in range(1, c + 1):
        dp[0][i] = c + 1

    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if l_coins[i - 1] <= j:
                # Calculamos el minimo entre los dos valores de la matriz si es menor:
                dp[i][j] = min(1 + dp[i][j - l_coins[i - 1]], dp[i - 1][j])
            else:
                # Copiamos el valor de la fila anterior si es mayor
                dp[i][j] = dp[i - 1][j]

    return dp

def optimal_change_pd(c: int, l_coins: List[int]) -> Dict[int, int]:
    """
    Calcula la cantidad optima de monedas para el cambio.
    Args:
        c: cantidad optima de monedas.
        l_coins: lista de monedas.
    Returns:
        ndarray: Diccionario que contiene las monedas utilizadas y sus cantidades
    """

    # Obtenemos la cantidad de monedas en la lista
    n = len(l_coins)

    # Usamos change_pd para generar la matriz 
    dp = change_pd(c, l_coins)

    # Creamos un diccionario ordenado para almacenar las cantidades de cada tipo de moneda
    coin_counts = OrderedDict()

    i, j = n, c
    while i > 0 and j > 0:
        # Si los valores de la matriz son iguales, pasamos a la siguiente fila en la matriz
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            if l_coins[i - 1] <= j:
                # Si la moneda actual es menor o igual al tam actual de la lista, 
                # agregamos la moneda al conteo y actualizamos
                if l_coins[i - 1] in coin_counts:
                    coin_counts[l_coins[i - 1]] += 1
                else:
                    coin_counts[l_coins[i - 1]] = 1
                j -= l_coins[i - 1]
    return coin_counts

def knapsack_fract_greedy(l_weights: List[int], l_values: List[int], bound: int) -> Dict[int, float]:
    """
    Esta funcion resuelve el problema de la mochila fraccionaria utilizando un enfoque codicioso
    Calcula los pesos a tomar de cada elemento en la solucion greedy del problema de la mochila fraccionaria.
    Args:
        l_weights: Lista de pesos de los elementos
        l_values: Lista de valores de los elementos
        bound: limite del peso de la mochila
    Returns:
        ndarray: La array generada.
    """
    n = len(l_weights)
    value_per_weight = [(l_values[i] / l_weights[i], i) for i in range(n)]
    value_per_weight.sort(reverse=True)

    taken_weights = {i: 0.0 for i in range(n)}
    current_weight = 0

    for vpw, i in value_per_weight:
        if current_weight + l_weights[i] <= bound:
            taken_weights[i] = 1.0
            current_weight += l_weights[i]
        else:
            remaining = bound - current_weight
            taken_weights[i] = remaining / l_weights[i]
            break

    return taken_weights 


def knapsack_01_pd(l_weights: List[int], l_values: List[int], bound: int) -> int:
    """
    Resuelve el problema de la mochila 0-1 y calcula el valor optimo de la mochila 0-1 obtenido mediante programacion dinamica.
    Args:
        l_weights: Lista de pesos de los elementos.
        l_values: Lista de valores de los elementos.
        bound: limite de peso de la mochila.
    Returns:
        int: El valor optimo de la mochila
    """

    # Obtienemos la longitud de la lista de pesos
    n = len(l_weights)
    
    # Inicializamos la matriz de programacion dinamica
    dp = np.zeros((bound + 1, n + 1), dtype=int)

    # Iteramos sobre los elementos y el limite de peso
    for i in range(1, n + 1):
        for j in range(bound + 1): 
            # Comprueba si el peso del elemento actual cabe en el limite actual
            if l_weights[i - 1] <= j: 
                # Calcula el valor maximo tomando el valor actual mas el valor en la fila anterior y la columna correspondiente al peso restante
                dp[i][j] = max(dp[i - 1][j], l_values[i - 1] + dp[i - 1][j - l_weights[i - 1]])
            else:
                # Si el peso del elemento actual excede el limite actual, se mantiene el valor anterior
                dp[i][j] = dp[i - 1][j]

    # Retorna el valor optimo de la mochila 0-1 obtenido mediante programacion dinmica
    return dp[n][bound]