class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometiste el error: {err}")

# raise ZeroDivisionError "Qué boludo, dividiste por cero")

# Lanzando mi propia excepcion
# raise MiExcepcion ("Jajajaja, persona poco culta")

# Manejandola
try:
    raise MiExcepcion ("Jajajaja, persona poco culta")
except:
    print("Como vas a cometer ese error?")
