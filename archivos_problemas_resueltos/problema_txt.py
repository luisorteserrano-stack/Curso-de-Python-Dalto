# 2 listas, una con nombres otra con apellidos
nombres = ["Lucas", "Matías", "Camila", "Pedro", "Roberto"]
apellidos = ["Dalto","Zing", "Dalto", "Robertix", "tarado"]

# Registrar esta info en un TXT de forma óptima

with open("archivos/nombresyapellidos.txt", "w") as arch:
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"nombre: {n}\nApellido: {a}\n-----------\n") for n,a in zip(nombres, apellidos)]
    