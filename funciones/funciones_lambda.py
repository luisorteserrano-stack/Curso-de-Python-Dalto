numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Creando una función lambda que multiplica un número por dos
multiplicar_por_dos = lambda x : x*2

print(multiplicar_por_dos(5))

# Creando función común que retorna números pares
def es_par(numeros):
    if (numeros % 2 == 0):
        return True
# Usando la función filter con una función común
numeros_pares = list(filter(es_par, numeros)) # Si lo convertimos a lista, obtenemos los valores filtrados  por True

print(numeros_pares)

# Lo mismo pero con lambda. Con esto se simplifica el código
numeros_pares_lambda = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares_lambda)