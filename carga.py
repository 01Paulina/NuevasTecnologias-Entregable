import pandas as pd

def cargar_datos(ruta_archivo):
    try:
        df_datos = pd.read_csv(ruta_archivo)
        print("\n¡Archivo cargado con éxito!")
        df_datos.info()
        return df_datos
    except FileNotFoundError:
        print(f"\nError: No se encontró el archivo en {ruta_archivo}")
        return None