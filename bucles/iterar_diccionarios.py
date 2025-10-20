diccionario = {"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"}

for clave in diccionario.items():
    print(f"El diccionario es: {clave}")  # Salida: ('nombre', 'Ana'), ('edad', 25), ('ciudad', 'Barcelona')

# Método Dalto
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el valor es {value}")

# Otra forma de hacerlo
for key, value in diccionario.items():
    print(f"La clave es: {key} y el valor es {value}")
    
# Evitando que se coma una fruta específica
frutas = {"manzana", "plátano", "naranja"}
for fruta in frutas:
    if fruta == "plátano":
        continue
    print(f"Las frutas que me voy a comer son: {fruta}")

# Evitando que el bucle siga ejecutándose después de encontrar una fruta específica
frutas = ["manzana", "plátano", "naranja", "kiwi", "fresa", "mango", "pera"]
for fruta_a_comer in frutas:
    print(f"Solo comeré las frutas: {fruta_a_comer}")
    if fruta_a_comer == "naranja":
        break
else: # El else después del brake tampoco se ejecuta
    print("He terminado de comer frutas.")

# Iterar sobre una cadena de texto
cadena = "Hola Mundo"
for letra in cadena:
    print(letra)
    
# Iterar sobre una lista de números
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
    
# for en una sola línea (duplicamos los númeors de una lista)
numeros_duplicados = [numero * 2 for numero in numeros]
print(numeros_duplicados)  # Salida: [2, 4, 6, 8, 10]
 