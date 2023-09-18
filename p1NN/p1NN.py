import numpy as np
from typing import Tuple
import timeit
from typing import List

# 1A
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
    # con np.dot :
    # m_r: np.ndarray = m_1.dot(m_2)

    # m_1 -> (i,j) m_2 -> (k,z)
    # bucle de filas m_1
    for i in range(shape_m_1[0]):
        # bucle de columnas m_2
        for z in range(shape_m_2[1]):
            num = 0
            # bucle de sumas y multiplicaciones
            for k,j in enumerate(range(shape_m_1[1])):
                # se multiplica cada numero correspondiente 
                # de la fila de m_1 y la columna de m_2
                num += m_1[i,j]*m_2[k,z]

            # se multimplican ambos valores
            m_r[i,z] = num

    return m_r

# lista de tiempos
l_timings = []
for i in range(10, 21):
    # dimension de la matriz
    dim = 10+i**2
    # crea una matriz de dimension dimXdim con valores 
    # aleatorios entre 0 y 1 
    m = np.random.uniform(low=0, high=1, size=(dim, dim)) 
    # guarda con el comando "magico" %timeit los valores de 
    # tiempo que tarda en realizar la funcion 
    # con 5 repeticiones de 10 iteraciones cada una
    timings = %timeit -o -n 10 -r 5 -q matrix_multiplication(m, m)
    # se guarda en la lista
    l_timings.append([dim, timings.best])

print("\nTimings arrays " +str(l_timings))

#1B
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

    # en cualquier otro caso es igual y por tanto se devuelve 
    # su posicion en la tabla
    return m

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
        # en cualquier otro caso es igual y por tanto se devuelve 
        else:
            return m
        
        # si no se ha devuelto se calcula de nuevo el mediano
        m = int((f+l)/2)


l_timingsbb = []
for size in enumerate(range(5, 15)):
    t = list(range(2**i * size[1]))
    key = size[0]
    timings = %timeit -n 100 -r 10 -o -q rec_bb(t, 0, len(t) - 1, key)
    l_timingsbb.append([len(t), timings.best])
    a_timings = np.array(l_timingsbb)

print("\nTimings bbrec " + str(a_timings))

l_timingsbbi = []
for size in enumerate(range(5, 15)):
    t = list(range(2**i * size[1]))
    key = size[0]
    timings = %timeit -n 100 -r 10 -o -q bb(t, 0, len(t) - 1, key)
    l_timingsbbi.append([len(t), timings.best])
    a_timingsbbi = np.array(l_timingsbbi)

print("\nTimings bbi " + str(a_timingsbbi))