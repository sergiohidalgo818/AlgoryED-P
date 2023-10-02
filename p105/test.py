import numpy as np
from typing import Tuple
from p105 import *
from random import randint
import numpy as np
import json

if __name__=='__main__':

    file_name = "data/exe_data.json"
    # m_1: np.ndarray = np.empty((3,3))
    # m_2: np.ndarray = np.empty((3,3))

    # shape_m_1 = np.shape(m_1)
    # shape_m_2 = np.shape(m_2)

    # print("m1:\n")
    # for i in range(shape_m_1[0]):
    #     for j in range(shape_m_1[1]):
    #         m_1[i][j] = float(input('Elemento (%d,%d): ' % (i, j)))
 
    # print("\nm2:\n")

    # for i in range(shape_m_2[0]):
    #     for j in range(shape_m_2[1]):
    #         m_2[i][j] = float(input('Elemento (%d,%d): ' % (i, j)))


    # m_r: np.ndarray = np.empty ((shape_m_1[0],shape_m_2[1])) 


    # print("\nm1\n" + str(m_1))
    # print("\nm2\n" + str(m_2))

    # # Si son incompatibles, devuelve None
    # if shape_m_1[1] != shape_m_2[0]:
    #     print("No se pueden mult")
    #     exit()

    # m_rauto: np.ndarray = m_1.dot(m_2)

    # for i in range(10, 21):
    #     # dimension de la matriz
    #     dim = 10+i**2
    #     # crea una matriz de dimension dimXdim con valores 
    #     # aleatorios entre 0 y 1 
    #     m = np.random.uniform(low=0, high=1, size=(dim, dim)) 

    #     m_1: np.ndarray = m
    #     m_2: np.ndarray = m

    #     shape_m_1 = np.shape(m_1)
    #     shape_m_2 = np.shape(m_2)
    #     m_r: np.ndarray = np.empty ((shape_m_1[0],shape_m_2[1])) 

    #     for i in range(shape_m_1[0]):
    #         # bucle de columnas m_2
    #         for j in range(shape_m_2[1]):
    #             num = 0
    #             # bucle de sumas y multiplicaciones
    #             for x in range(shape_m_1[1]):
    #                 # se multiplica cada numero correspondiente 
    #                 # de la fila de m_1 y la columna de m_2
    #                 num += m_1[i,x]*m_2[x,j]

    #             # se multimplican ambos valores
    #             m_r[i,j] = num
    #         m_rauto: np.ndarray = m_1.dot(m_2)

    #         print("fun = " +str(m_r))
    #         print("auto = " +str(m_rauto))

    # data = []
    #
    # with open(file_name, 'w') as outfile:  
    #    json.dump(data, outfile)

    for j in range(3):
        size = randint(8, 14)
        auxl = list()
        for i in range(size):

           auxl.append(randint(0, 50))

        print("NO ORDENADA",auxl)
        aux = np.random.permutation(auxl)
        print(np.size(aux))
        create_min_heap(aux)
        print("ORDENADA",aux)
        print("\n")