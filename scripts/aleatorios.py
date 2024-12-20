import numpy as np
import matplotlib.pyplot as plt

from libs.benchmark import Benchmark

@Benchmark("main")
def main():

    # 100 números random del 1 al 10
    numeros = np.random.randint(1, 11, 100)

    frecuencia = {}

    # Se cuenta la frecuencia en la posición de cada número
    for num in numeros:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1

    numeros_unicos = [1,2,3,4,5,6,7,8,9,10]
    frecuencias_ordenadas = [frecuencia[num] for num in numeros_unicos]

    # Número mayor de frecuencia
    max_frecuencia = max(frecuencia.values())
    max_repetidos = []

    # Número menor de frecuencia
    min_frecuencia = min(frecuencia.values())
    min_repetidos = []


    # Imprimir resultados
    print("Frecuencia de cada número:")
    for num in numeros_unicos:
        print(f"Número {num}: {frecuencia[num]} veces")

        # Se obtienen los números más y menos repetidos
        if frecuencia[num] == max_frecuencia:
            max_repetidos.append(num)

        if frecuencia[num] == min_frecuencia:
            min_repetidos.append(num)

    print("\nNúmero(s) que más se repiten: ")
    for num in max_repetidos:
        print(f"Número {num}: {frecuencia[num]} veces")

    print("\nNúmero(s) que menos se repiten: ")
    for num in min_repetidos:
        print(f"Número {num}: {frecuencia[num]} veces")

    # Gráficos
    plt.figure(figsize=(15, 5))

    # Gráfico de barras
    plt.subplot(1, 3, 1)
    plt.bar(numeros_unicos, frecuencias_ordenadas)
    plt.title("Frecuencia de Números (Barras)")
    plt.xlabel("Número")
    plt.ylabel("Frecuencia")

    # Diagrama de caja y bigotes
    plt.subplot(1, 3, 2)
    plt.boxplot(numeros, vert=False)
    plt.title("Diagrama de Caja y Bigotes")
    plt.xlabel("Números")

    # Diagrama de violín
    plt.subplot(1, 3, 3)
    plt.violinplot(numeros, vert=False)
    plt.title("Diagrama de Violín")
    plt.xlabel("Números")
    plt.ylabel("Densidad")

    # Mostrar gráficos
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()