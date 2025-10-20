# Creando un conjunto con set
conjunto = set(["Dato 1", 2, 3, 4, 5])
print(conjunto)  # Salida: {'Dato 1', 2, 3, 4, 5}

# Creando un conjunto con set y una tupla como elemento
conjunto = set(["Dato 1", ("dato1tupla", "dato2tupla"), 3, 4, 5])
print(conjunto)  # Salida: {('dato1tupla', 'dato2tupla'), 3, 4, 5, 'Dato 1'}

conjunto1 = frozenset(["Dato 1", 2, 3, 4, 5]) # Conjunto inmutable para que sea hashable
conjunto2 = set([conjunto1, "Dato 3"])
print(conjunto2)  # Salida: {frozenset({2, 3, 4, 5, 'Dato 1'}), 'Dato 3'}

# Teoría de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

resultado = conjunto1.issubset(conjunto2) # False
resultado = conjunto1 <= conjunto2 # False
print(resultado)
resultado = conjunto2.issubset(conjunto1) # True
resultado = conjunto2 <= conjunto1 # True
print(resultado)
resultado = conjunto1.issuperset(conjunto2) # True
resultado = conjunto1 > conjunto2 # True
print(resultado)
resultado = conjunto2.issuperset(conjunto1) # False
resultado = conjunto2 > conjunto1 # False 
print(resultado)

# Verificar si hay algún número en común entre dos conjuntos
resultado = conjunto1.isdisjoint(conjunto2) # False
print(resultado)
# Cuando ningún elemento coincide entre ambos conjuntos
