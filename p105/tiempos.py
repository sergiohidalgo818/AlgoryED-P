import json
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math

# Funcion de coste teórico multiplicación de matríces
def f(N):
    return N**3

# Funcion de coste teorico short_min_heap
def f_heap(N):
    
    return N*(np.log10(N))

# Funcion para ajustar los tiempos reales a la función teórica
def tofit_heap(x, a, b):
    return a * f_heap(x) + b

# Funcion para ajustar los tiempos reales a la función teórica
def tofit(x, a, b):
    return a * f(x) + b

def graficasMult():
    # Se abre el archivo
    with open('./data/exe_data.json', 'r') as file:
        data = json.load(file)
    # se extrae la array de datos del diccionario
    array_mult = np.array(data['array_mult'])
    # y se extraen los valores de N y los tiempos de ejecución
    x = array_mult[: , 0]
    y = array_mult[: , 1]

    # se normalizan los tiempos 
    y = y / y[0]

    # para después ajustar los datos 
    pars, _ = curve_fit(tofit, x, y)
    a, b = pars

    # y guardar los valores de y que corresponderan con la función teórica
    y_fit = a * f(x) + b

    # Se crea la figura
    plt.figure(figsize=(10, 5))
    # Se plotean los tiempos reales
    plt.plot(x, y, marker='o', linestyle=' ', label='Tiempos reales')
    # y los ajustados
    plt.plot(x, y_fit, label='Ajuste: N^3')
    # labels sobre los los ejes de la gráfica
    plt.xlabel('Tamaño de entrada (N)')
    plt.ylabel('Tiempo de Ejecución Normalizado')
    plt.title('Ajuste de Tiempos de Ejecución')
    plt.legend()
    plt.grid(True)
    # Se guarda la imagen
    plt.savefig('ej1.png')
    plt.close()

def graficasMultDot():
    # Se abre el archivo
    with open('./data/exe_data.json', 'r') as file:
        data = json.load(file)

    # se extraen las arrays de datos del diccionario
    array_mult = np.array(data['array_mult'])
    array_dot = np.array(data['array_dot'])

    # y se extraen los valores de N y los tiempos de ejecución
    N_mult, tiempos_mult = array_mult[:, 0], array_mult[:, 1]
    N_dot, tiempos_dot = array_dot[:, 0], array_dot[:, 1]

    # A grandes rasgos esta parte es identica a la de la funcion anterior
    plt.figure(figsize=(10, 5))
    plt.plot(N_mult, tiempos_mult, marker='o', label='multiplication')
    plt.xlabel('N')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Tiempo matrix_multiplication() ')
    plt.legend()
    plt.grid(True)
    plt.savefig('grafica_array_mult.png')
    plt.close()

    # Segunda grafica pero con dot
    plt.figure(figsize=(10, 5))
    plt.plot(N_dot, tiempos_dot, marker='o', label='numpy', color='orange')
    plt.xlabel('N')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Tiempo numpy.ndarray.dot() ')
    plt.legend()
    plt.grid(True)
    plt.savefig('grafica_array_dot.png')
    plt.close()


def graficasBB():
    # Se abre el archivo
    with open('./data/exe_data.json', 'r') as file:
        data = json.load(file)

    # se extraen las arrays de datos del diccionario
    bb_iter = np.array(data['bb_iter'])
    bb_rec = np.array(data['bb_rec'])

    # y se extraen los valores de N y los tiempos de ejecución
    N_bbi, tiempos_bbi = bb_iter[:, 0], bb_iter[:, 1]
    N_bbrec, tiempos_bbrec = bb_rec[:, 0], bb_rec[:, 1]

    # Grafica de la busqueda binaria iterativa
    plt.figure(figsize=(10, 5))
    plt.plot(N_bbi, tiempos_bbi, marker='o', label='bbisearch')
    plt.xlabel('N')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Tiempo bb() iterativa ')
    plt.legend()
    plt.grid(True)
    plt.savefig('grafica_bbi.png')
    plt.close()

    # Grafica de la busqueda binaria recursiva
    plt.figure(figsize=(10, 5))
    plt.plot(N_bbrec, tiempos_bbrec, marker='o', label='bbrecsearch')
    plt.xlabel('N')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Tiempo bb_rec() ')
    plt.legend()
    plt.grid(True)
    plt.savefig('grafica_bb_rec.png')
    plt.close()


    # Grafica de las dos busquedas
    plt.figure(figsize=(10, 5))
    plt.plot(N_bbi, tiempos_bbi, marker='o', label='bbi')
    plt.plot(N_bbrec, tiempos_bbrec, marker='o', label='bbrec')
    plt.xlabel('N')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Tiempo bbi() & bb_rec() ')
    plt.legend()
    plt.grid(True)
    plt.savefig('grafica_bbi_rec.png')
    plt.close()



def graficasCreateHeap():
    # Se abre el archivo
    with open('./data/exe_data.json', 'r') as file:
        data = json.load(file)

    # se extraen las arrays de datos del diccionario
    timings_minh = np.array(data['l_timings_min'])

    # y se extraen los valores de N y los tiempos de ejecución
    N_minh, tiempos_createminh = timings_minh[:, 0], timings_minh[:, 1]

    # Grafica de la creacion de min heaps
    plt.figure(figsize=(10, 5))
    plt.plot(N_minh, tiempos_createminh, marker='o', label='createMinheap')
    plt.xlabel('N')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Tiempo create_min_heap() ')
    plt.legend()
    plt.grid(True)
    plt.savefig('grafica_createminheap.png')
    plt.close()


def graficasShortHeap():
    # Se abre el archivo
    with open('./data/exe_data.json', 'r') as file:
        data = json.load(file)

    # se extraen las arrays de datos del diccionario
    l_timings_minsh = np.array(data['l_timings_minsh'])

    # y se extraen los valores de N y los tiempos de ejecución
    x, y = l_timings_minsh[:, 0], l_timings_minsh[:, 1]

    # se normalizan los tiempos 
    y = y / y[0]

    # para después ajustar los datos 
    pars, _ = curve_fit(tofit_heap, x, y)
    a, b = pars

    # y guardar los valores de y que corresponderan con la función teórica
    y_fit = a * f_heap(x) + b


    # se normalizan los tiempos 
    y = y / y[0]

    # para después ajustar los datos 
    pars, _ = curve_fit(tofit, x, y)
    a, b = pars

    # y guardar los valores de y que corresponderan con la función teórica
    y_fit = a * f(x) + b    

    # Grafica del short minheap
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker=' ', label='shortMinheap')
    plt.plot(x, y_fit, label='Ajuste: N log(N)')
    plt.xlabel('N')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Tiempo min_heap_sort() ajustado')
    plt.legend()
    plt.grid(True)
    plt.savefig('grafica_shortheap.png')
    plt.close()


if __name__ == "__main__":
    # llamada a las funciones que van creando las graficas
    graficasMult()
    graficasMultDot()
    graficasBB()
    graficasCreateHeap()
    graficasShortHeap()