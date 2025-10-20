numeros = [1, 2, 3, 4, 5]

# Encontrando número máximo
maximo = max(numeros)
print("Número máximo:", maximo) 

# Encontrando número mínimo
minimo = min(numeros)
print("Número mínimo:", minimo)

# Redondeando un número a seis decimales
numero = 3.141592653589793
redondeanto_antes = round(numero * 100) / 100
print("Número antes de redondear:", redondeanto_antes)
redondeado = round(numero, 6)
print("Número redondeado a seis decimales:", redondeado)

# Retorna False si pasamos 0, vacío, False, None
resultado_bool_vacio = bool(0)
resultado_bool_vacio = bool()
resultado_bool_vacio = bool([])
resultado_bool_vacio = bool(())
resultado_bool_vacio = bool("")
resultado_bool_vacio = bool(None)
print("Resultado booleano de 0:", resultado_bool_vacio)   
resultado_bool_lleno = bool([3,5])
print("Resultado booleano de [3,5]:", resultado_bool_lleno)

# Retorna True si todos los elementos son verdaderos
resultado_all = all([1, 2, 3, 4, 5])
print("Resultado all con todos verdaderos:", resultado_all)
resultado_all_falso = all([1, 2, 0, 4, 5])
print("Resultado all con un falso:", resultado_all_falso)

# Suma todos los elementos de un iterable (Solo funciona con números)
suma = sum(numeros)
print("Suma de los números:", suma)
