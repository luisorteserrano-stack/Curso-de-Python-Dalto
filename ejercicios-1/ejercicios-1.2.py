frase = input("Escribe una frase y te calculo cuánto tardarías si tuvieras que decirla: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

if cantidad_de_palabras > 20:
    print("Esa es una frase bastante larga, no te pedí un testamento")

print(f"La frase tiene {cantidad_de_palabras} palabras. Y tardarías {cantidad_de_palabras / 2} segundos en decirla.")
print(f"Dalto tardaría {cantidad_de_palabras *100 // 2 * 1.3 / 100} segundos en decirla.")
