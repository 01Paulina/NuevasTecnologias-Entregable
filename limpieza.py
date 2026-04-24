import pandas as pd

def limpiar_datos(df):
    # 1. Hacemos una copia para no alterar el DataFrame original accidentalmente
    df_limpio = df.copy()

    # 2. Eliminar registros sin nombre o apellido (maneja nulos y espacios en blanco)
    df_limpio = df_limpio.dropna(subset=["nombre", "apellido"])
    df_limpio = df_limpio[df_limpio["apellido"].str.strip() != ""]

    # 3. Limpiar edades 
    df_limpio = df_limpio[(df_limpio["edad"] >= 0) & (df_limpio["edad"] <= 100)]

    # 4. Limpiar correos
    df_limpio = df_limpio[df_limpio["email"].str.contains(r"@.*\.", na=False, regex=True)]

    # 5. Normalizar género
    df_limpio["genero"] = df_limpio["genero"].replace({
        "M": "Masculino",
        "F": "Femenino",
        "masculino": "Masculino",
        "femenino": "Femenino"
    })

    # 6. Convertir ciudades, departamentos y países a formato correcto (Primera letra mayúscula)
    df_limpio["ciudad"] = df_limpio["ciudad"].str.capitalize()
    df_limpio["departamento"] = df_limpio["departamento"].str.capitalize()
    df_limpio["pais"] = df_limpio["pais"].str.capitalize()

    # 7. Eliminar contraseñas muy cortas 

    df_limpio["password"] = df_limpio["password"].astype(str)
    df_limpio = df_limpio[df_limpio["password"].str.len() >= 3]

    # 8. Resetear índices para que queden ordenados
    df_limpio = df_limpio.reset_index(drop=True)

    return df_limpio

def limpiar_cursos(df):
    
    
    print("Columnas originales:")
    print(df.columns)
    
    #1. Normalizar nombres de columnas
    df.columns = df.columns.str.strip()

    #2. Limpiar valores nulos (strings vacíos y 'null')
    df = df.replace(["", " ", "null", "None"], pd.NA)

    #3. Eliminar espacios en columnas de texto
    df = df.replace(["", " ", "null", "None"], pd.NA)
    
    columnas_texto = ["nombreCurso", "descripcionCurso", "categoria", "dificultad"]
    for col in columnas_texto:
        df[col] = df[col].astype(str).str.strip()

    #4. Corregir dificultad
    df["dificultad"] = df["dificultad"].replace({
        "medio": "intermedio",
        "basico": "básico",
        "avanzado": "avanzado"
    })

    #5. Convertir numeroNiveles a numérico
    df["numeroNiveles"] = pd.to_numeric(df["numeroNiveles"], errors="coerce")
    df = df[(df["numeroNiveles"] >= 1) & (df["numeroNiveles"] <= 10)]

    #6. Eliminar filas con nulos importantes
    df = df.dropna(subset=["nombreCurso", "descripcionCurso", "numeroNiveles"])

    #7. Corregir nombres de cursos
    df["nombreCurso"] = df["nombreCurso"].replace({
        "fundamentos java": "fundamentos de java",
        "spring boot avanzado": "spring boot avanzado",
        "arquitectura microservicios spring cloud": "arquitectura de microservicios con spring cloud"
    })

    #8. Guardar archivo limpio
    df.to_csv("cursos_limpio.csv", index=False)
    print("Limpieza completada. Archivo guardado como cursos_limpio.csv")
    print(df.head())

    return df