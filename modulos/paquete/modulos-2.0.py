# Ejemplo de uso de un módulo desde otro módulo
import funciones_buenas.saludar

# import sys

# Agregar el directorio padre al path de búsqueda de módulos
# sys.path.append("/Users/luis/Documents/Curso de Python Dalto/funciones_buenas") 
# print (sys.path)

# import saludar as modulo_saludar

# print(modulo_saludar.saludar("Pedro"))

print(funciones_buenas.saludar.saludar("Pedro"))
