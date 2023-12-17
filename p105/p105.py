import numpy as np
from typing import Tuple
from typing import List

# I-A


def matrix_multiplication(m_1: np.ndarray, m_2: np.ndarray) -> np.ndarray:

    # Se obtienen las dimensiones de cada matriz
    shape_m_1 = np.shape(m_1)
    shape_m_2 = np.shape(m_2)
    # Si son incompatibles, devuelve None
    if shape_m_1[1] != shape_m_2[0]:
        return None

    # la matriz resultante tendra las filas de m1 y columnas de m2
    m_r: np.ndarray = np.empty((shape_m_1[0], shape_m_2[1]))
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
                num += m_1[i, x]*m_2[x, j]

            # se multiplican ambos valores
            m_r[i, j] = num

    return m_r


# I-B
def rec_bb(t: List, first: int, last: int, key: int) -> int:
    # m es la parte media de la lista (primero + ultimo)/2
    if first > last:
        return None
    
    m = int((first+last)/2)
    # si el elemento del medio es mayor que el numero a buscar
    if t[m] > key:
        # se cambia el ultimo por el mediano menos 1
        # y se llama de nuevo a la funcion
        rec_bb(t, first, m-1, key)
    # si el elemento del medio es menor que el numero a buscar
    elif t[m] < key:
        # se cambia el primero por el mediano mas 1
        # y se llama de nuevo a la funcion
        rec_bb(t, m+1, last, key)
    # si es igual se devuelve m
    elif t[m] == key:
        return m

    # si el primero y el segundo son iguales
    elif first == last:
        # returna None
        return None


def bb(t: List, first: int, last: int, key: int) -> int:
    # m es la parte media de la lista (primero + ultimo)/2
    m = int((first+last)/2)

    # mientras el elemento del medio sea distinto a la key
    while t[m] != key:

        # si el elemento del medio es mayor que el numero a buscar
        if t[m] > key:
            # se cambia el ultimo por el mediano menos 1
            last = m-1
        # si el elemento del medio es menor que el numero a buscar
        elif t[m] < key:
            # se cambia el primero por el mediano mas 1
            first = m+1
        # si es igual se devuelve m
        elif t[m] == key:
            return m
        # si no se ha devuelto se calcula de nuevo el mediano
        m = int((first+last)/2)

    # si el primero y el segundo son iguales
    if first == last:
        return None

# I-C


def matrix_multiplication_dot(m_1: np.ndarray, m_2: np.ndarray) -> np.ndarray:

    # Se obtienen las dimensiones de cada matriz
    shape_m_1 = np.shape(m_1)
    shape_m_2 = np.shape(m_2)

    # Si son incompatibles, devuelve None
    if shape_m_1[1] != shape_m_2[0]:
        return None

    # la matriz resultante tendra las filas de m1 y columnas de m2
    m_r: np.ndarray = np.empty((shape_m_1[0], shape_m_2[1]))
    # Si son compatibles, se multiplican y se devuelve la matriz resultante
    # con np.dot :
    m_r: np.ndarray = m_1.dot(m_2)

    return m_r

# II-A


def min_heapify(h: np.ndarray, i: int):
    tam = len(h) - 1

    # control de errores
    if i < 0 or i > tam:
        return None

    # dato hijo izquierdo
    left = 2 * i + 1

    # dato hijo derecho
    right = 2 * i + 2

    while left <= tam:
        # se toma como minimo inicial el elemento
        # en la posicion del indice de la funcion
        minimum = i

        # se comparan los elementos de la izquierda y
        # el del indice introducido en la funcion
        # si el introducido es mas grande que el izquierdo
        if h[i] > h[left]:
            # el izquierdo pasa a ser el minimo
            minimum = left

        # si el derecho es menor que el introducido y
        # que el minimo o el derecho mayor o igual al tamaño
        if right <= tam and h[i] > h[right] and h[right] < h[minimum]:
            # el derecho pasa a ser el minimo
            minimum = right

        # en caso de que sea mayor que el introducido
        if minimum > i:
            # se hace swap entre el elemento introducido y el minimo
            h[i], h[minimum] = h[minimum], h[i]
            # y el introducido sera el minimo
            i = minimum
        # en otro caso para
        else:
            break


def insert_min_heap(h: np.ndarray, k: int) -> np.ndarray:

    # control de errores
    if h is None:
        return np.array([k])

    i = len(h)
    # se añade al final de la array
    h = np.append(h, k)

    # mientras la i se mayor que 0 y
    # el padre es mayor que el elemento en i
    while i > 0 and h[(i-1)//2] > h[i]:
        # se swapean el elemento i y su padre
        h[i], h[(i-1)//2] = h[(i-1)//2], h[i]
        # y se continua la ejecuccion por el
        i = (i-1)//2
    return h


def create_min_heap(h: np.ndarray):

    # control de errores
    if h is None:
        return None
    size = len(h)
    for i in range(size, -1, -1):
        min_heapify(h, i)
    return h

def min_heap_extract(h: np.ndarray) -> Tuple[int, np.ndarray]:

    tam = len(h)

    # control de errores
    if tam == 0:
        return list()

    # el elemento raiz sera el primero
    root = h[0]

    # aux es el ultimo elemento de la lista
    aux = int(h[tam-1])
    for i in range(tam-1, 0, -1):
        # aux2 pasa a ser el penultimo elemento de la list
        aux2 = int(h[i-1])
        # se guarda el valor de aux en el penultimo lugar
        h[i-1] = aux
        # y aux pasara a ser aux 2
        aux = int(aux2)

        # de esta manera en la siguiente iteracion aux sera el
        # elemento que va a ser sustituido

    # create min heap para que pase a ser heap
    # y h[:-1] para reducir el tamaño de la array

    return root, create_min_heap(h[:-1])

# II-B


def pq_ini():
    # se crea una array de numpy de tipo 0 y se devuelve
    q = np.ndarray(shape=0)
    return q


def pq_insert(h: np.ndarray, k: int) -> np.ndarray:
    # se inserta llamando a insert_min_heap
    return insert_min_heap(h, k)


def pq_remove(h: np.ndarray) -> Tuple[int, np.ndarray]:
    # se elimina llamando a min_heap_extract
    return min_heap_extract(h)


def min_heap_sort(h: np.ndarray) -> np.ndarray:

    # se crea un min heap y una lista de retorno
    h = create_min_heap(h)
    ret = list()

    # mientras la longitud sea mayor que 0
    while len(h) > 0:
        # se va extrayendo la raiz (numero mas pequeño)
        root, h = min_heap_extract(h)
        # y se va añadiendo a la lista de retorno
        ret.append(root)

    return np.array(ret)
