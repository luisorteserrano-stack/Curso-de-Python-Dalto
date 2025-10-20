# Creando diccionarios con dict()
diccionario = dict(nombre="Luis", edad=30, ciudad="Madrid")
print(diccionario)  # Salida: {'nombre': 'Luis', 'edad':

#las listas no pueden ser claves de diccionarios y usamos frozenset para conjuntos inmutables
diccionario = {frozenset([1, 2, 3]): "Conjunto como clave", (4, 5): "Tupla como clave"}
print(diccionario)  # Salida: {frozenset({1, 2, 3}): 'Conjunto como clave', (4, 5): 'Tupla como clave'} 

# Creando diccionario con el método de diccionarios fromkeys()
diccionario = dict.fromkeys(["nombre", "edad", "ciudad"], "Desconocido")
print(diccionario)  # Salida: {'nombre': 'Desconocido', 'edad': 'Desconocido', 'ciudad': 'Desconocido'}
print(diccionario["nombre"])  # Salida: Desconocido

# Creando diccionario con el método de diccionarios fromkeys() valor por defecto a None
diccionario = dict.fromkeys(["nombre", "edad", "ciudad"])
print(diccionario)  # Salida: {'nombre': None, 'edad': None,

# Creando diccionario con el método de diccionarios fromkeys() valor por defecto a No lo sé
diccionario = dict.fromkeys(["nombre", "edad", "ciudad"], "No lo sé")
print(diccionario)  # Salida: {'nombre': 'No lo sé', 'edad': 'No lo sé', 'ciudad': 'No lo sé'}
