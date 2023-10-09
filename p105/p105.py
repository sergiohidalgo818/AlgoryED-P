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
    tam = len(h) - 1
    if i < 0 or i > tam:
        return None

    l = 2 * i + 1
    r = 2 * i + 2     
   
    while l <= tam:
        largest = i 
        if h[i] > h[l]:
            largest = l
        if r <= tam and h[i] > h[r] and h[r] < h[largest]:
            largest = r
        if largest > i:
            h[i], h[largest] = h[largest], h[i]
            i = largest
        else:
            break

    

def insert_min_heap(h: np.ndarray, k: int)-> np.ndarray:
    if h is None:
        return np.array([k])

    h = np.append(h, k)
    i = len(h) -1

    while i > 0 and h[(i-1)//2] > h[i]:
        h[i], h[(i-1)//2] = h[(i-1)//2], h[i]
        i = (i-1)//2
    return h



def create_min_heap(h: np.ndarray):
    if h is None:
        return None
    
    j = ((len(h))-1)//2

    while j >-1:
        min_heapify (h, j)
        j -= 1
    return h
            
def remove_min_hep(h: np.ndarray):
    if len(h) == 0:
        raise IndexError('Empty heap')
    
    root = h[0]
    
    # swapp the root with the last node
    h[0] =  h[len(h)-1]
    
    h.pop()
    min_heapify(h, 0)
    
    return root

#II-B
def pq_ini():
    q = np.ndarray
    return q

def pq_insert(h: np.ndarray, k: int)-> np.ndarray:
    insert_min_heap(h, k)
    return h

def pq_remove(h: np.ndarray)-> Tuple[int, np.ndarray]:
    root = remove_min_hep(h)
    return root, h

