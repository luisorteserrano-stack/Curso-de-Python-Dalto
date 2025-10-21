import pandas as pd

df = pd.read_csv("archivos/datos.csv")
#print(df)

# cambiar el tipo de dato de una columna

# Para ver el tipo de dato
print(type(df["edad"][0])) # Resultado: <class 'numpy.int64'>

# Convertir a string los datos de una columna
df["edad"] = df["edad"].astype(str)

# Para ver el tipo de dato
print(type(df["edad"][0])) # Resultado: <class 'str'>

# Reemplazar valores
df["apellido"].replace("Dalto", "maestro",inplace=True)
print(df["apellido"])

# Trabajar con ficheros CSV con errores
df = pd.read_csv("archivos/datos_erroneos.csv")
print(df)
# Omitir filas con datos faltaltes
df = df.dropna()
print(df)

# Omitir columnas con datos faltaltes
# df = pd.read_csv("archivos/datos_erroneos.csv")
# df = df.dropna(axis=1)
# print(df)

# Eliminar filas duplicadas
#df = pd.read_csv("archivos/datos_erroneos.csv")
df = df.drop_duplicates()
print(df)

# Creando un CVS con el DataFrame resultante (Limpio)
df.to_csv("archivos/datos_limpios.csv")
