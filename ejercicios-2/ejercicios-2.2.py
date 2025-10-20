# Creando una funcion que nos evuelta númeoros primos entre 0 y el argumento que pasemos

# Creamos una función que nos diga si un número es primo
def es_primo(limite):
    # Un número es primo si solo es divisible por 1 y por sí mismo
    for i in range(2, limite-1):
        # Si es divisible por algún número entre 2 y el límite -1, no es primo
        if limite % i == 0: return False
    # Si no es divisible por ningún número, es primo
    return True

# Creamos una función que nos devuelva una lista de números primos hasta un límite
def primos_hasta(limite):
    # Lista para almacenar los números primos
    primos = []
    for i in range(3,limite+1):
        # Verificamos si es primo
        resultado = es_primo(i)
        # Si es primo, lo agregamos a la lista
        if resultado == True: primos.append(i)
    # Devolvemos la lista de números primos
    return primos

resultado = es_primo(13)
print(resultado)
resultado = primos_hasta(13)
print(resultado)
