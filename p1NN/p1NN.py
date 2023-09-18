import numpy as np
from typing import Tuple
import timeit
from typing import List

def matrix_multiplication(m_1: np.ndarray, m_2: np.ndarray)-> np.ndarray:

    #Se obtienen las dimensiones de cada matriz
    shape_m_1 = np.shape(m_1)
    shape_m_2 = np.shape(m_2)

    #Si son incompatibles, devuelve None
    if shape_m_1[1] != shape_m_2[0]:
        return None
   
    #Si son compatibles, se multiplican y se devuelve la matriz resultante 
    m_t: np.ndarray = m_1.dot(m_2)

    return m_t


def rec_bb(t: List, f: int, l: int, key: int)-> int:
    pass

def bb(t: List, f: int, l: int, key: int)-> int:
    pass


l_timings = []
for i in range(10, 21):
    dim = 10+i**2
    m = np.random.uniform(low=0, high=1, size=(dim, dim)) 
    timings = %timeit -o -n 10 -r 5 -q matrix_multiplication(m, m)
    l_timings.append([dim, timings.best])

print("\nTimings arrays " +l_timings)


l_timingsbb = []
for size in enumerate(range(5, 15)):
    t = list(range(2**i * size))
    key = ...
    timings = %timeit -n 100 -r 10 -o -q rec_bb(t, 0, len(t) - 1, key)
    l_timingsbb.append([len(t), timings.best])
    a_timings = np.array(a_timings)

print("\nTimings bb " + l_timingsbb)

l_timingsbbi = []
for size in enumerate(range(5, 15)):
    t = list(range(2**i * size))
    key = ...
    timings = %timeit -n 100 -r 10 -o -q bb(t, 0, len(t) - 1, key)
    l_timingsbbi.append([len(t), timings.best])
    a_timingsbbi = np.array(l_timingsbbi)

print("\nTimings bb " + a_timingsbbi)