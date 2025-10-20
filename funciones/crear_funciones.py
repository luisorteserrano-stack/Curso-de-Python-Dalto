# creando una función simple
def saludar():
    print ("¡Hola, mundo!")
# Ejecutando la función simple
saludar()

# creando una función con parámetros
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")
# Ejecutando la función con un argumento
saludar_persona("Ana")
# creando una función con múltiples parámetros
def saludar_persona_identificada(nombre, sexo):
    sexo = sexo.lower()
    if sexo == 'mujer':
        print(f"¡Hola, Sra. {nombre}!")
    elif sexo == 'hombre':
        print(f"¡Hola, Sr. {nombre}!")
    else:
        print(f"¡Hola, mi amor {nombre}!")
# Ejecutando la función con múltiples argumentos
saludar_persona_identificada("Luis", "Hombre")

# creando una función que retorna un valor
def crear_contraseña_random(numero):
    chars = "asdffghjk"
    num_entero = str(numero)
    numero = int(num_entero[0])
    c1 = numero - 2
    c2 = numero
    c3 = numero - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{numero*2}"
    return(contraseña)
# Ejecutando la función que retorna un valor

passwd = crear_contraseña_random(7)
print("Contraseña generada:", passwd)
print(f"La contraseña: {passwd}")

# creando una función que retorna varios valores
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division
# Ejecutando la función que retorna varios valores desempaquetando los resultados
s, r, m, d = operaciones_basicas(10, 5)
print("Suma:", s)
print("Resta:", r)
print("Multiplicación:", m)
print("División:", d)
