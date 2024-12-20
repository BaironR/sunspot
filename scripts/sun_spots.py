import pandas as pd
import matplotlib.pyplot as plt
from libs.benchmark import Benchmark

def obtener_anio(fecha):
    anio=fecha[:4]
    return anio

@Benchmark("main")
def main():
    df = pd.read_csv("../data/Sunspots.csv")
    df.drop(columns="Unnamed: 0", inplace=True)

    cant_filas_con_datos_faltantes = df.count().iloc[1]
    cant_filas_sin_datos_faltantes = df.dropna().count().iloc[1]

    media = df["Monthly Mean Total Sunspot Number"].mean()
    desv_estandar = df["Monthly Mean Total Sunspot Number"].std()

    for columna in df.columns:
        print(f"Tipo de variable de la columna {columna}: {type(columna)}")

    print(f"Existen {cant_filas_con_datos_faltantes - cant_filas_sin_datos_faltantes} datos faltantes")
    print(f"Existen {cant_filas_sin_datos_faltantes} entradas de datos.")
    print(f"Media del promedio de manchas solares: {media:.3f}")
    print(f"Desviación estándar del promedio de manchas solares: {desv_estandar:.3f}")

    sunspot_mean = "Monthly Mean Total Sunspot Number"
    plt.hist(df[sunspot_mean], bins=20)
    plt.ylabel(sunspot_mean)
    plt.show()

    df.plot(x="Date", y=sunspot_mean, kind='line')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()