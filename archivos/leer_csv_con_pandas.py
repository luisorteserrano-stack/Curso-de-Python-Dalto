import pandas as pd
# print(type(pd))

# Creamos el DataFrame (Es una estructura de datos compuesto por Filas y Columnas)
df = pd.read_csv("archivos/datos.csv",names=["name","lastname","age"])

nombres = df["name"]
# print(nombres)
# print(df)

# cadena = "0123456789"
# print(cadena[0:5])

df_ordenado_descendente = df.sort_values("age")
df_ordenado_ascendente = df.sort_values("age",ascending=False)

print(df_ordenado_ascendente)


df = pd.read_csv("archivos/datos.csv")
df2 = pd.read_csv("archivos/datos.csv")

# Concatenamos los dos DataFrames
df_concatenado = pd.concat([df,df2])
print(df_concatenado)

primer_fila = df.head(3)
print(primer_fila)

ultimas_fila = df.tail(3)
print(ultimas_fila)