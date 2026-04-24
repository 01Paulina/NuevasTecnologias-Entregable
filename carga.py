import pandas as pd

def cargar_datos(ruta_archivo):
    try:
        df_datos = pd.read_csv(ruta_archivo)
        print("\n¡Archivo cargado con éxito!")
        df_datos.info()
        return df_datos
    except FileNotFoundError:
        print(f"\nError: No se encontró el archivo en {ruta_archivo}")
        return df_datos

def cargar_cursos(ruta_archivo):
    try:
        
        df_curso = pd.read_csv(ruta_archivo)
        print("\n¡Archivo de cursos cargado con éxito!")
        return df_curso 
    except Exception as e:
        print(f"\nError al cargar cursos: {e}")
        return df_curso