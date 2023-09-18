import numpy as np
from typing import Tuple
import timeit

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


l_timings = []
for i in range(10, 21):
    dim = 10+i**2
    m = np.random.uniform(low=0, high=1, size=dim)
    timings = %timeit -o -n 10 -r 5 -q matrix_multiplication(m, m)
    l_timings.append([dim, timings.best])