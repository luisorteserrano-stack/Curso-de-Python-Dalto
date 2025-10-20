def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido} es muy {adjetivo}."

# frase_resultado = frase("Juan", "Pérez", "inteligente")
# Utilizando argumentos de palabra clave ó keyword arguments
frase_resultado = frase(adjetivo = "inteligente", nombre = "Juan", apellido = "Pérez")
print(frase_resultado)

# Creando la función con un parámetro opcional y un valor por defecto
def frase_opcional(nombre, apellido, adjetivo = "genial"):
    return f"Hola {nombre} {apellido} es muy {adjetivo}."
print(frase_opcional("Ana", "García"))
print(frase_opcional("Ana", "García", "amable"))