import pandas as pd
import limpieza
import carga

RUTA_ARCHIVO = "./data/raw/datos.csv"
df_datos = None
isLoader = False

while True:
    print("\nMENÚ PRINCIPAL")
    print("1. Cargar datos")
    print("2. Limpiar datos")
    print("3. Mostrar datos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            print("\n¿Qué archivo deseas cargar?")
            print("1. datos.")
            print("2. cursos.")

            tipo = input("Seleccione una opción: ")
            if tipo == "1":
                ruta = "./data/raw/datos.csv"
                df_datos = carga.cargar_datos(ruta)
            elif tipo == "2":
                ruta = "./data/raw/cursos.csv"
                df_curso = carga.cargar_cursos(ruta)
            else:
                print("\nOpción inválida.")
                continue

            
            isLoader = True
            print ("Carga completa")

            if df_datos is not None:
                df_datos.info()
                
            if df_curso is not None:
                df_curso.info()


        case "2":
            if isLoader:
                
                df_datos = limpieza.limpiar_datos(df_datos)
                df_datos.to_csv("datos_limpios.csv", index=False)
                print("\nLimpieza completada y archivo guardado como 'datos_limpios.csv'")
            else:
                print("\nPor favor, primero carga los datos usando la opción 1.")

        case "3":
            if isLoader:
                print("\nMostrando los primeros 5 registros de tus datos actuales:")
                print(df_datos.head())
            else:
                print("\nNo hay datos cargados en memoria.")

        case "4":
            print("\nSaliendo del programa.")
            break

        case _:
            print("\nOpción inválida. Por favor, selecciona un número del 1 al 4.")