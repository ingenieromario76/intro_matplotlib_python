# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Scatter Plot")

    # NOTA: aproveche los ejemplos "scatter_plot" de clase

    # Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función y = tanh(x) --> tangente hiperbólica
    y = np.tanh(x)

    # Alumno: Graficar la función utilizando "scatter"
    # utilizando "x" e "y" ya disponible
    fig = plt.figure()
    fig.suptitle('Ejercicio_3 Tangente Hiperbólica', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)  # 1 fila, 2 columnas, axes nº1
    ax2 = fig.add_subplot(1, 2, 2)  # 1 fila, 2 columnas, axes nº2

    # Colocar la leyenda y el label con el nombre de la función

    # Elegir un marker a elección

    # Crear acá su gráfico
    ax1.plot(x, y, c='darkgreen')
    ax1.legend()
    ax1.grid()

    ax2.scatter(x, y, c='darkred')
    ax2.legend()
    ax2.grid()
    plt.show()
    print("terminamos")
