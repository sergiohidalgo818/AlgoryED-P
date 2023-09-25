import numpy as np
from typing import Tuple
from typing import List

# I-A
def matrix_multiplication(m_1: np.ndarray, m_2: np.ndarray)-> np.ndarray:

    # Se obtienen las dimensiones de cada matriz
    shape_m_1 = np.shape(m_1)
    shape_m_2 = np.shape(m_2)
    # Si son incompatibles, devuelve None
    if shape_m_1[1] != shape_m_2[0]:
        return None
    
    # la matriz resultante tendra las filas de m1 y columnas de m2
    m_r: np.ndarray = np.empty ((shape_m_1[0],shape_m_2[1])) 
    # Si son compatibles, se multiplican y se devuelve la matriz resultante 

    # m_1 -> (i,x) m_2 -> (x,z)
    # bucle de filas m_1
    for i in range(shape_m_1[0]):
        # bucle de columnas m_2
        for j in range(shape_m_2[1]):
            num = 0
            # bucle de sumas y multiplicaciones
            for x in range(shape_m_1[1]):
                # se multiplica cada numero correspondiente 
                # de la fila de m_1 y la columna de m_2
                num += m_1[i,x]*m_2[x,j]

            # se multimplican ambos valores
            m_r[i,j] = num
            
    return m_r



# I-B
def rec_bb(t: List, f: int, l: int, key: int)-> int:
    # m es la parte media de la lista (primero + ultimo)/2
        
    m = int((f+l)/2)
    # si el elemento del medio es mayor que el numero a buscar
    if t[m] > key:
        # se cambia el ultimo por el mediano menos 1
        # y se llama de nuevo a la funcion
        rec_bb(t, f, m-1, key)
    # si el elemento del medio es menor que el numero a buscar
    elif t[m] < key:
        # se cambia el primero por el mediano mas 1
        # y se llama de nuevo a la funcion
        rec_bb(t, m+1, l, key)
    # si es igual se devuelve m 
    elif t[m] == key:
        return m
    
    # si el primero y el segundo son iguales  
    elif f==l:
        # returna None
        return None

def bb(t: List, f: int, l: int, key: int)-> int:
    # m es la parte media de la lista (primero + ultimo)/2
    m = int((f+l)/2)

    # mientras el elemento del medio sea distinto a la key
    while t[m] != key:

        # si el elemento del medio es mayor que el numero a buscar
        if t[m] > key:
            #se cambia el ultimo por el mediano menos 1
            l = m-1
        # si el elemento del medio es menor que el numero a buscar
        elif t[m] < key:
            # se cambia el primero por el mediano mas 1
            f = m+1
        # si es igual se devuelve m
        elif t[m] == key:
            return m
        # si no se ha devuelto se calcula de nuevo el mediano
        m = int((f+l)/2)
    
    # si el primero y el segundo son iguales  
    if f==l:
        return None

# I-C
def matrix_multiplication_dot(m_1: np.ndarray, m_2: np.ndarray)-> np.ndarray:

    # Se obtienen las dimensiones de cada matriz
    shape_m_1 = np.shape(m_1)
    shape_m_2 = np.shape(m_2)

    # Si son incompatibles, devuelve None
    if shape_m_1[1] != shape_m_2[0]:
        return None
    
    # la matriz resultante tendra las filas de m1 y columnas de m2
    m_r: np.ndarray = np.empty ((shape_m_1[0],shape_m_2[1])) 
    # Si son compatibles, se multiplican y se devuelve la matriz resultante 
    # con np.dot :
    m_r: np.ndarray = m_1.dot(m_2)

    return m_r

# II-A
def min_heapify(h: np.ndarray, i: int):

    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2     
    
    if r > h.size:
        return

    if h[r] < h[largest] and h[largest] < h[l]:
        largest = l
 
    if h[l] < h[largest] and h[largest] < h[r]:    
        largest = r
 
    if largest != i:
        h[i], h[largest] = h[largest], h[i]  
  
        min_heapify(h, largest)

    

def insert_min_heap(h: np.ndarray, k: int)-> np.ndarray:
    h[h.size+1] = k
    min_heapify(h, h.size-1)
    return h

def create_min_heap(h: np.ndarray):
    N = len(h)
 
    # Build a maxheap.
    for i in range((N/2)-1):
        min_heapify(h, i)
 
    # One by one extract elements
    for i in range(N-1):
        h[i], h[0] = h[0], h[i]  # swap
        min_heapify(h, i)
 

#II-B
def pq_ini():
    pass

def pq_insert(h: np.ndarray, k: int)-> np.ndarray:
    pass

def pq_remove(h: np.ndarray)-> Tuple[int, np.ndarray]:
    pass