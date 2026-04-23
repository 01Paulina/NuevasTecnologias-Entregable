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