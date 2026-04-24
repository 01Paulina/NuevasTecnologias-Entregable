import pandas as pd
import limpieza
import carga

df_datos = None
df_curso = None
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
                df_datos.info()
            elif tipo == "2":
                ruta = "./data/raw/cursos.csv"
                df_curso = carga.cargar_cursos(ruta)
                df_curso.info()
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
            print("\n¿Qué archivo deseas limpiar?")
            print("1. datos.")
            print("2. cursos.")

            tipo = input("Seleccione una opción: ")
            if tipo == "1":
                if isLoader:
                    df_limpio = limpieza.limpiar_datos(df_datos)
                    df_limpio.to_csv("datos_limpios.csv", index=False)
                    print ("\nLimpieza completada.")
            
            elif tipo == "2":
                if isLoader:
                    df_curso_limpio = limpieza.limpiar_cursos(df_curso)
                    df_curso_limpio.to_csv("cursos_limpio.csv", index=False)
                    print("\nLimpieza completada.")

        case "3":
            if isLoader:
                print("\nDatos actuales:")

                df_datos= carga.cargar_datos("./data/raw/datos.csv")
                df_curso = carga.cargar_cursos("./data/raw/cursos.csv") 
                print(df_datos.head())
                print(df_curso.head())
                
            else:
                print("\nNo hay datos cargados.")

        case "4":
            print("\nSaliendo del programa.")
            break

        case _:
            print("\nOpción inválida. Por favor, selecciona un número del 1 al 4.")