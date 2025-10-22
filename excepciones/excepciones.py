def sumar_dos():
    # Iniciamos el bucle
    while True:
        # Petición de datos de entrada
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        # Intento de ejecución para sumar
        try:
            resultado = int(a) + int(b)
        # Si lanzó una excepción, pedir que vuelva a introducir los números
        # except
        except Exception as e:
            print("Te pedí un número")
            print(f"Error {e}" + " " + f"Tipo ERROR: {type(e).__name__}")
            print(f"ERROR: {type(e).__name__}")
        # except ZeroDivisionError:
        #     print("No se puede dividir por 0)")
        # Si todo salió bien, terminamos el bucle
        else:
            break
        # Finally se ejeccuta siempre
        finally:
            print ("Esto se ejecuta siempre. Manejo excepción finalizado")
    # Mostramos el resultado
    return resultado

print(sumar_dos())