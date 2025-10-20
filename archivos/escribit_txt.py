with open("archivos/texto_de_dalto_2.txt", "w", encoding="UTF-8") as archivo:
    # Con "w" sobreescribe el archivo si no existe
    #archivo.write("Probando a escribir dentro de un archivo")
    # Con writelines espera un iterable y con "\n" hacemos el salto de línea (Es el proceso inverso a readlines())
    archivo.writelines(["Hola cómo estás\n", "probando\n"])
    archivo.writelines(["Hola también\n", "segunda línea"])
