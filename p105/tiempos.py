import json
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define tu función teórica f(N)
def f(N):
    # Aquí debes implementar tu función teórica
    # Por ejemplo, podrías usar una función cuadrática
    return 2 * N**3 + 3 * N + 1

# Define la función para ajustar los tiempos reales a la función teórica
def tofit(x, a, b):
    return a * f(x) + b

def graficasDot():
    # Supongamos que tienes un array de tiempos reales a_timings
    with open('./data/array.exe_data.json', 'r') as file:
        data = json.load(file)

    array_mult = np.array(data['array_mult'])

    # Extraer los valores de N y los tiempos de ejecución

    x = array_mult[: , 0]
    #o (mas "pythonico"?) x = a_timings.T[0].T
    y = array_mult[: , 1]
    
    # Normaliza los tiempos dividiendo por el primer valor (opcional)
    y = y / y[0]

    # Ajusta los datos a la función tofit usando curve_fit
    pars, _ = curve_fit(tofit, x, y)

    # Recuperar los parámetros ajustados (a y b)
    a, b = pars

    # Generar valores ajustados usando la función teórica
    y_fit = a * f(x) + b

    # Graficar los tiempos reales y el ajuste calculado por la función
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o', label='Tiempos reales')
    plt.plot(x, y_fit, label='Ajuste')
    plt.xlabel('Tamaño de entrada (N)')
    plt.ylabel('Tiempo de Ejecución Normalizado')
    plt.title('Ajuste de Tiempos de Ejecución')
    plt.legend()
    plt.grid(True)

    # Guardar la primera gráfica en un archivo PNG
    plt.savefig('ej1.png')
    plt.close()

def graficasMult():
    # Cargar los datos desde el archivo JSON
    with open('./data/array.exe_data.json', 'r') as file:
        data = json.load(file)

    array_mult = np.array(data['array_mult'])
    array_dot = np.array(data['array_dot'])

    # Extraer los valores de N y los tiempos de ejecución
    N_mult, tiempos_mult = array_mult[:, 0], array_mult[:, 1]
    N_dot, tiempos_dot = array_dot[:, 0], array_dot[:, 1]

    # Crear la primera gráfica para array_mult
    plt.figure(figsize=(10, 5))
    plt.plot(N_mult, tiempos_mult, marker='o', label='multiplication')
    plt.xlabel('N')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Tiempo matrix_multiplication() ')
    plt.legend()
    plt.grid(True)

    # Guardar la primera gráfica en un archivo PNG
    plt.savefig('grafica_array_mult.png')
    plt.close()

    # Crear la segunda gráfica para array_dot
    plt.figure(figsize=(10, 5))
    plt.plot(N_dot, tiempos_dot, marker='o', label='numpy', color='orange')
    plt.xlabel('N')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Tiempo matrix_multiplication() numpy')
    plt.legend()
    plt.grid(True)

    # Guardar la segunda gráfica en un archivo PNG
    plt.savefig('grafica_array_dot.png')
    plt.close()


def graficasBB():
    # Cargar los datos desde el archivo JSON
    with open('./data/exe_data.json', 'r') as file:
        data = json.load(file)

    bb_iter = np.array(data['bb_iter'])
    bb_rec = np.array(data['bb_rec'])

    # Extraer los valores de N y los tiempos de ejecución
    N_bbi, tiempos_bbi = bb_iter[:, 0], bb_iter[:, 1]
    N_bbrec, tiempos_bbrec = bb_rec[:, 0], bb_rec[:, 1]

    # Crear la primera gráfica para array_mult
    plt.figure(figsize=(10, 5))
    plt.plot(N_bbi, tiempos_bbi, marker='o', label='bbisearch')
    plt.xlabel('N')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Tiempo bb() ')
    plt.legend()
    plt.grid(True)

    # Guardar la primera gráfica en un archivo PNG
    plt.savefig('grafica_bbi.png')
    plt.close()

       # Crear la primera gráfica para array_mult
    plt.figure(figsize=(10, 5))
    plt.plot(N_bbrec, tiempos_bbrec, marker='o', label='bbrecsearch')
    plt.xlabel('N')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Tiempo bb_rec() ')
    plt.legend()
    plt.grid(True)

    # Guardar la primera gráfica en un archivo PNG
    plt.savefig('grafica_bb_rec.png')
    plt.close()


    # Crear la primera gráfica para array_mult
    plt.figure(figsize=(10, 5))
    plt.plot(N_bbi, tiempos_bbi, marker='o', label='bbisearch')
    plt.plot(N_bbrec, tiempos_bbrec, marker='o', label='bbrecsearch')
    plt.xlabel('N')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Tiempo bbi() & bb_rec() ')
    plt.legend()
    plt.grid(True)

    # Guardar la primera gráfica en un archivo PNG
    plt.savefig('grafica_bbi_rec.png')
    plt.close()



def graficasCreateHeap():
    # Cargar los datos desde el archivo JSON
    with open('./data/exe_data.json', 'r') as file:
        data = json.load(file)

    timings_minh = np.array(data['l_timings_min'])

    # Extraer los valores de N y los tiempos de ejecución
    N_minh, tiempos_createminh = timings_minh[:, 0], timings_minh[:, 1]

    # Crear la primera gráfica para array_mult
    plt.figure(figsize=(10, 5))
    plt.plot(N_minh, tiempos_createminh, marker='o', label='createMinheap')
    plt.xlabel('N')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Tiempo create_min_heap() ')
    plt.legend()
    plt.grid(True)

    # Guardar la primera gráfica en un archivo PNG
    plt.savefig('grafica_minheap.png')
    plt.close()


def graficasShortHeap():
    # Cargar los datos desde el archivo JSON
    with open('./data/exe_data.json', 'r') as file:
        data = json.load(file)

    l_timings_minsh = np.array(data['l_timings_minsh'])

    # Extraer los valores de N y los tiempos de ejecución
    N_minhsh, tiempos_minhsh = l_timings_minsh[:, 0], l_timings_minsh[:, 1]

    # Crear la primera gráfica para array_mult
    plt.figure(figsize=(10, 5))
    plt.plot(N_minhsh, tiempos_minhsh, marker='o', label='shortMinheap')
    plt.xlabel('N')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Tiempo min_heap_sort() ')
    plt.legend()
    plt.grid(True)

    # Guardar la primera gráfica en un archivo PNG
    plt.savefig('grafica_shortheap.png')
    plt.close()


if __name__ == "__main__":
    graficasMult()
    graficasDot()
    graficasBB()
    graficasCreateHeap()
    graficasShortHeap()