import logging

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from libs.benchmark import Benchmark
from pandas.plotting import scatter_matrix

log = logging.getLogger(__name__)

@Benchmark("main")
def main():

    # El dataframe.
    df_iris = pd.read_csv("../data/iris.csv")

    # El grafico.
    plt.figure(1, figsize=(12, 8))
    scatter_matrix(df_iris[df_iris["variety"] == "Iris-virginica"])

    # Pregunta 1
    print("\n1. Tipo de datos de cada columna y el numero de valores no nulos:\n")
    print(df_iris.info())

    # Pregunta 2
    print("\n2. Estadisticas descriptivas:\n")
    print(df_iris.describe())

    # Pregunta 3
    print("\n3. Columna sepal.length:\n")
    print(df_iris["sepal.length"])

    # Pregunta 4
    print("\n4. Columna sepal.length y petal.length:\n")
    print(df_iris[["sepal.length", "petal.length"]])

    # Pregunta 5
    print("\n5. Filas donde la especie es setosa:\n")
    print(df_iris.loc[df_iris["variety"] == "Iris-setosa"])

    # Pregunta 6
    print("\n6. Filas donde sepal.length es mayor a 5:\n")
    print(df_iris.loc[df_iris["sepal.length"] > 5.0])

    # Pregunta 7.
    print("\n7. Filas donde sepal.length es mayor a 5 y petal.length es menor a 4:\n")
    print(df_iris.loc[(df_iris["sepal.length"] > 5.0) & (df_iris["petal.length"] < 4.0)])

    # Pregunta 8.
    print("\n8. Columna sepal.ratio = sepal.length / sepal.width:\n")
    df_iris["sepal.ratio"] = df_iris["sepal.length"]/df_iris["sepal.width"]
    print(df_iris["sepal.ratio"])

    # Pregunta 9.
    print("\n9. Media de sepal.length para cada especie:\n")
    print(df_iris.groupby("variety")["sepal.length"].mean())

    # Pregunta 10.
    print("\n10. Suma de petal.length para cada especie:\n")
    print(df_iris.groupby("variety")["petal.length"].sum())

    # Pregunta 11.
    print("\n11. Nuevo dataframe: df_setosa con las filas donde df_iris es setosa:\n")
    df_setosa = df_iris.loc[df_iris["variety"] == "Iris-setosa"].copy()
    print(df_setosa)

    # Pregunta 12.
    print("\n12. Funcion personalizada para convertir de cm a pulgadas en los elementos de sepal.length:\n")

    def cm_to_inches(cm):
        return cm * 0.393701

    df_iris["sepal.length.inches"]= df_iris["sepal.length"].apply(cm_to_inches)
    print(df_iris["sepal.length.inches"])

    # Pregunta 13.
    print("\n13. Guardar df_iris en un csv llamado iris_data.csv sin incluir indice:")
    df_iris.to_csv("../output/iris_data.csv", index=False)
    print("Dataframe df_iris guardado en la ruta ../output/iris_data.csv")
    log.info("Dataframe df_iris guardado en la ruta ../output/iris_data.csv")

    # Pregunta 14.
    print("\n14. Reemplazar valores NaN en sepal.width con la media de la columna:\n")
    df_iris["sepal.width"] = df_iris["sepal.width"].fillna(df_iris["sepal.width"].mean())
    print(df_iris["sepal.width"])

    # Pregunta 15.
    print("\n15. Columna petal.area = petal.length * petal.width en cm^2:\n")
    df_iris["petal.area"] = df_iris["petal.length"] * df_iris["petal.width"]
    print(df_iris["petal.area"])

    # Pregunta 16.
    print("\n16. Filas con valores duplicados en las columnas sepal.length y sepal.width:\n")
    print(df_iris[df_iris.duplicated(subset=['sepal.length', 'sepal.width'])])

    # Pregunta 17.
    print("\n17. Eliminar filas con valores duplicados en las columnas sepal.length y sepal.width:\n")
    df_iris = df_iris.drop_duplicates(subset=['sepal.length', 'sepal.width'])
    print(df_iris)

    # Pregunta 18.
    print("\n18. Columna species.id = (setosa: 0; versicolor: 1; virginica: 2):\n)")
    df_iris["species.id"] = df_iris["variety"].map({'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2})
    print(df_iris[["species.id","variety"]])

    # Pregunta 19.

    colors = {'Iris-setosa': "magenta", 'Iris-versicolor': "green", 'Iris-virginica': "orange"}

    plt.figure(1, figsize=(8, 6))

    for variety, colors in colors.items():
        subset = df_iris.loc[df_iris["variety"] == variety]
        plt.scatter(subset["sepal.length"], subset["sepal.width"], color=colors, label=variety)

    plt.title("19. Grafico de dispersion Sepal Length vs Sepal Width")
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.xticks(np.arange(min(df_iris["sepal.length"]), max(df_iris["sepal.length"]), 0.2), rotation=45)
    plt.yticks(np.arange(min(df_iris["sepal.width"]), max(df_iris["sepal.width"]), 0.2))
    plt.legend()
    plt.show()

    # Pregunta 20.
    plt.figure(2, figsize=(8, 6))

    colors = {'Iris-setosa': "magenta", 'Iris-versicolor': "green", 'Iris-virginica': "orange"}
    for variety, colors in colors.items():
        subset = df_iris.loc[df_iris["variety"] == variety]
        plt.hist(subset["petal.length"], bins=50, color=colors, label=variety, alpha=0.5)

    plt.xlabel('Petal Length')
    plt.ylabel('Frequency')
    plt.title('20. Distribucion de Petal Length por cada especie')
    plt.xticks(np.arange(min(df_iris["petal.length"]), max(df_iris["petal.length"]), 0.2), rotation=45)
    plt.yticks(np.arange(0, plt.gca().get_ylim()[1], 1))
    plt.legend()
    plt.show()

    # Pregunta 21.
    print("\n21. Columna sepal.size = (small: sepal.length menor a 5, medium: sepal.length entre 5 y 6.5, large: sepal.length mayor a 6.5):\n)")

    def size(length):
        if length < 5:
            return 'small'
        elif length > 6.5:
            return 'large'
        return 'medium'

    df_iris["sepal.size"] = df_iris["sepal.length"].apply(size)
    print(df_iris[["sepal.size", "sepal.length"]])

    # Pregunta 22.
    print("\n22. Tabla pivot con las especies como filas y sepal.size como columnas:\n")
    pivot_table = df_iris.pivot_table(index=['variety'], columns=['sepal.size'], aggfunc='size', fill_value=0)
    print(pivot_table)

    # Pregunta 23.
    print("\n23. Guardar df_iris en un Excel llamado iris_data.xlsx con cada especie en una hoja separada:\n")

    with pd.ExcelWriter('../output/iris_data.xlsx') as writer:

        varieties = df_iris["variety"].unique()

        for variety in varieties:
            df_variety = df_iris[df_iris["variety"] == variety]
            df_variety.to_excel(writer, sheet_name=variety, index=False)

    print("Dataframe df_iris guardado en la ruta ../output/iris_data.xlsx")
    log.info("Dataframe df_iris guardado en la ruta ../output/iris_data.xlsx")

    # Pregunta 24.
    print("\n24. Funcion por cada grupo para calcular sepal.length / sepal.width en sepal.ratio:\n")

    df_iris["sepal.ratio"] = df_iris.groupby('variety').apply(lambda group: group['sepal.length'] / group['sepal.width']).reset_index(0, drop=True)
    print(df_iris[["sepal.ratio", "variety"]])


if __name__ == "__main__":
    main()
