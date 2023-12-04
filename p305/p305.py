"""
Ejercicio p305.py
Autores: Sergio Hidalgo y Miguel Ibanez
"""

from typing import Tuple, Union
import numpy as np
from math import ceil

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
    t_smallers = [u for u in t if u < mid]
    t_greaters = [u for u in t if u > mid]
    return t_smallers, mid, t_greaters


def qsel(t: np.ndarray, k: int) -> Union[int, None]:
    """
    Esta funcion aplica de manera recursiva Quick Select
        usando split.
    Args:
        t: array con los elementos.
        k: posicion del elemento a encontrar.
    Returns:
        Union: De el valor de k si existe y None si no.
    """

    # control de errores
    if k >= len(t):
        return None

    if len(t) == 1 and k == 0:
        return t[0]

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
        k: posicion del elemento a encontrar.
    Returns:
        Union: De el valor de k si existe y None si no.
    """

    # control de errores
    if k >= len(t):
        return None

    aux_t = t.copy()

    # mientras aux_t tenga mas de un elemento y no sea el primero
    while len(aux_t) > 1 or k > 0:
        t_smallers, mid, t_greaters = split(aux_t)
        m = len(t_smallers)
        if k == m:
            return mid
        elif k < m:
            aux_t = t_smallers
        else:
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

    n, remain = divmod(len(t), GROUPSIZE)
    
    k = int(ceil(GROUPSIZE/2)) 

    medians = [np.sort(t[j * GROUPSIZE : (j+1) * GROUPSIZE])[k-1] for j in range(0, n)]
    
    if remain:
        k = int(ceil(remain/2))
        medians.append(np.sort(t[-remain: ])[k-1])
    
    
    k = int(ceil(len(medians)/2))    
    if len(medians) <= CUTOFF:            # if tabla_size <= cutff, sort and return k-position
        pivot = np.sort(medians)[k - 1] 
    else:
        pivot = qsel5_nr(medians, k)

    return pivot
    
def qsel5_nr(t: np.ndarray, k: int)-> Union[int, None]:
    """
    Esta funcion aplica de manera no recursiva Quick Select 5
        usando split.
    Args:
        t: array con los elementos.
        k: posicion del elemento a encontrar.
    Returns:
        Union: De el valor de k si existe y None si no.
    """

    if k >= len(t):
        return None

    if len(t) == 1 and k == 0:
        return t[0]
    

    if len(t) <= CUTOFF:
        return np.sort(t)[k-1]
    
    mid = pivot5(t)
    s_1, pivot_value, s_2 = split_pivot(t, mid)
    m = len(s_1)
    

    if k == m +1:
        return pivot_value
    
    elif k < m +1:
        return qsel5_nr(s_1, k)
    else:
        k = k - m-1 
        return qsel5_nr(s_2, k)
