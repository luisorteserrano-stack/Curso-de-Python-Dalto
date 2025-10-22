import re

email = "lucasdaltonuevogmail@gmail.c"

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# "+" ecuentra 1 ó más coincidencias, entonces lo muestra
# Lo que hace es buscar alguna coincidencia en todo el patrón encerrado el corchetes
# [a-zA-Z]{2,} que al menos tenga dos letras y sin límite máximo

result = re.match(pattern, email)

if result:
    print("Dirección de correo válida")
else:
    print("Dirección de correo inválida")