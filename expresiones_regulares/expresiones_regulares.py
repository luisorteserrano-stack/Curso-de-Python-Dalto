import re

texto = """Hola maestro, esta es la cadena 1, cómo estas?
Esta es la segunda línea abbbbb de texto, ababab línea 2.
Estad
Hola YY Esta 255 la tercera 3. y 12345 final definitiva."""

print (texto)

# Haciendo una búsqueda simple
resultado = re.search("Hola",texto)
resultado = re.findall("esta",texto)
resultado = re.findall("Esta", texto, flags=re.IGNORECASE)

# Haciendo una búsqueda con expresiones regulares
# \d -> busca dígitos numéricos del 0 al 9
resultado = re.findall(r"\d",texto)

# \D -> busca TODO MENOS dígitos numéricos del 0 al 9
resultado = re.findall(r"\D",texto)

# \w -> busca caracteres alfanuméricos del [a-z A-Z 0-9 _]
resultado = re.findall(r"\w",texto)

# \w -> busca TODO MENOS caracteres alfanuméricos del [a-z A-Z 0-9 _]
resultado = re.findall(r"\W",texto)

# \s -> busca espacios en blanco --> espacios, tabs, saltos de línea
resultado = re.findall(r"\s",texto)

# \S -> busca TODO MENOS espacios en blanco --> espacios, tabs, saltos de línea
resultado = re.findall(r"\S",texto)

# \n -> busca saltos de línea
resultado = re.findall(r"\n",texto)

# . -> busca TODO MENOS saltos de línea
resultado = re.findall(r".",texto)

# \ -> cancelar caracteres especiales, cancelando con "\" y busca puntos "."
resultado = re.findall(r"\.",texto)

#  busca un número seguido de un punto y un espacio en blanco ó salto línea
resultado = re.findall(r"\d\.\s",texto)

# Busca "Hola" al principio de una líena
# Con esto cada líena lo detecta como comienzo de cada línea "flags=re.M"
resultado = re.findall(f'^Hola',texto,flags=re.M)

# Busca el final de una línea
resultado = re.findall(f'Estad$',texto,flags=re.M)

# {n} -> Busca n cantidad de veces el valor de la izquierda (grupos)
resultado = re.findall(r'\d{3}\s',texto)

# {n.m} -> al menos n, como máximo m
resultado = re.findall(r'\d{4,5}\s',texto)
resultado = re.findall(r'ab{2,5}',texto) # Busca la "a" seguido de 2 ó 5 "b"
resultado = re.findall(r'(ab){2,5}',texto) # Busca el grupo "ab" repetido 2 ó 5 veces
# pero no devuelve más que un "ab"
resultado = re.findall(r'[ab]{2,5}',texto) # Busca el caracter "a" ó "b" repetido 2 ó 5 veces

# | -> Busca una cosa ó la otra
resultado = re.findall(r'\d{6,10}|Hola',texto)

print(resultado)
