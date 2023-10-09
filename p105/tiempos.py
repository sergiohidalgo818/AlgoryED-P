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

def mishuevos():
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

def generar_graficas():
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

if __name__ == "__main__":
    generar_graficas()
    mishuevos()
