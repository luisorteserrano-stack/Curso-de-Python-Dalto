with open("archivos/texto_de_dalto_2.txt", "a", encoding="UTF-8") as archivo:
    # Con "a" agrega el archivo si no existe
    #archivo.write("Probando a escribir dentro de un archivo")
    # Con writelines espera un iterable y con "\n" hacemos el salto de línea (Es el proceso inverso a readlines())
    archivo.writelines(["\nHola cómo estás agregando\n", "probando\n"])
    archivo.writelines(["Hola también agregando\n", "segunda línea\n"])
    for i in range(5):
        archivo.writelines(f"Línea {i+1} agregada\n")