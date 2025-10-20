diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print(diccionario)

claves = diccionario.keys()
print(claves)

elemento = diccionario.get("edad")
print(elemento)

eliminando_elemento = diccionario.pop("ciudad")
print(diccionario)

dic_iterable = diccionario.items()
print(dic_iterable)

eliminando = diccionario.clear()
print(diccionario)