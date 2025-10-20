archivo_sin_leer = open("archivos/texto_de_dalto.txt", encoding="utf-8")

# Lee archivo completo
# archivo = archivo_sin_leer.read()
# print(archivo

# Lee línea por línea
# lineas = archivo_sin_leer.readlines()
# print(lineas)
    # Prueba
# Leer una sola línea (Consume mucha memoria)
linea_1 = archivo_sin_leer.readline()

# Prueba 2
# Cerrar el archivo
archivo_sin_leer.close()

print(linea_1)