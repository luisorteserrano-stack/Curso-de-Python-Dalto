# Ejemplo de importación de un módulo completo
# import modulo_saludar as m_saludar

# Ejemplo de importación de funciones específicas desde un módulo
from modulo_saludar import saludar, saludar_raro

saludo = saludar("Luis")
saludo_raro = saludar_raro("Luis")

print(saludo)
print(saludo_raro)

# Para ver los atributos y funciones del módulo importado
# print (dir(m_saludar))

# Accedemos al nombre del módulo importado
# print(m_saludar.__name__)

# Accemos al nomre del módulo actual
# print(__name__)
