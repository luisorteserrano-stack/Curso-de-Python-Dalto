# Faltó el proge y los pibes van a armar la clase

# pedir el nombre y edad de los compañeros que vinieron a clase
def obtener_compañeros(cantidad_compañeros):
    # Lista para almacenar los compañeros
    compañeros = []
    # Pedir datos de cada compañero
    for i in range(cantidad_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre, edad)
        # Agregar el compañero a la lista
        compañeros.append(compañero) 
    # Ordenar la lista de compañeros por edad usando una función lambda
    compañeros.sort(key=lambda x: x[1])
    # Obtener el asistente de clase (el más joven) y el profesor (el mayor)
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    # retornamos la tupla con los resultados
    return asistente, profesor
# Desepmpaquetamos y llamamos a la función ypara mostrar los resultados
asistente, profesor = obtener_compañeros(5)

print(f"El asistente de clase es: {asistente}")
print(f"El profesor es: {profesor}")

