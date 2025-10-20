# Con este comando se abre y se cierra el archivo con with open
with open("archivos/texto_de_dalto.txt", encoding="UTF-8") as archivo:
    
    # Leemos el archivo
    archivo_leido = archivo.read()
    
    # Mostramos el resutado
    print(archivo_leido)
    
# No es necesario cerrar el archivo al usar with open
