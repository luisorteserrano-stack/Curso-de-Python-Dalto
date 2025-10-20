animales = ['perro', 'gato', 'pez', 'loro']

for animal in animales:
    print(f"Ahora la variable animal es: {animal}")

# para iterar dos listas a la vez usamos la función zip()
animales = ['perro', 'gato', 'pez', 'loro']
numeros = [1, 2, 3, 4]

for animal, numero in zip(animales, numeros):
    print(f"El animal {animal} tiene el número {numero}")

# para iterar con la función range()
for num in range(5, 10):
    print(f"El número es: {num}")
# para iterar una lista con la función range()
for num in range(len(animales)):
    print(f"El animal es: {animales[num]}")

# para iterar una lista y obtener el índice y el valor usamos la función enumerate()
for indice, animal in enumerate(animales):
    print(f"El animal en el índice {indice} es: {animal}")
    
# Ó la forma de Dalto
for num in enumerate(animales):
    indice = num[0]
    valor = num[1]
    print(f"El animal en el índice {indice} es: {valor}")
    
# Usando el else en un bucle for
for animal in animales:
    print(f"El animal es: {animal}")
else:
    print("Se han iterado todos los animales.")
