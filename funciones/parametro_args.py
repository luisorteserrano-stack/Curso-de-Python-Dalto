# Forma incorrecta de usar parámetros en una función
# def suma(lista):
#     numeros_sumados = 0
#     for numero in lista:
#         numeros_sumados += numero
#     return numeros_sumados
# 
# resultado = suma([4,5,9])

# Utilizando *args para aceptar un número variable de argumentos (siempre al final, porque si no se omite el resto de parámetros)
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus números es: {sum(numeros)}"

resultado = suma("Lucas",4,5,9)
print(resultado)

# Forma óptima de sumar valores
def suma_total(numeros):
    return sum([*numeros]) # Utilizando el operador * para desempaquetar la lista

resultado_total = suma_total([4,5,9]) # Pasando una lista completa
print(resultado_total)