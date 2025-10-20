import paquete
import paquete.modulo_saludar

# Muestra que es un objeto tipo 'list' debido al fichero __init__.py
print (type(paquete.__path__)) 

# Muestra la ruta del paquete
print (paquete.__path__) 

# Usando una función del módulo dentro del paquete
print (paquete.modulo_saludar.saludar("Ana"))
