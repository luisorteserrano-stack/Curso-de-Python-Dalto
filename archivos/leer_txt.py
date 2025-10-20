# Usando open para abrir un archivo con una codificación universal (UTF-9)
archivo_sin_leer = open("archivos/texto_de_dalto.txt", encoding="utf-8")

# Lee archivo completo
# archivo = archivo_sin_leer.read()
# print(archivo)

# Lee línea por línea
# lineas = archivo_sin_leer.readlines()
# print(lineas)

# Leer una sola línea (Consume mucha memoria)
# linea_1 = archivo_sin_leer.readline()
# print(linea_1)

# Leer el archivo
archivo = archivo_sin_leer.read()
# Cerrar el archivo
archivo_sin_leer.close()
# Obtenemos eo resultado por pantalla
print(archivo)