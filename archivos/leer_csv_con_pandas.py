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

# Accediendo a la cantidad de filas y columnas con shape

filas_columnas = df.shape
filas_totales = filas_columnas[0]
columnas_totales = filas_columnas[1]
print(filas_columnas)
print(filas_totales)
print(columnas_totales)

# ó bien puedo hacerlo desempaquetando
filas_totales, columnas_totales = df.shape
print(filas_totales)
print(columnas_totales)

# Obteniendo data estadística del DataFrame

df_info = df.describe()
print(df_info)

# Accediendo a un elemento específico del df con loc
# Accedemos al valor de la fila 2 y de la columna "edad" 
elemento_especifico_loc = df.loc[2,"edad"]
print(elemento_especifico_loc)

# Lo mismo pero con iloc
elemento_especifico_iloc = df.iloc[2,2]
print(elemento_especifico_iloc)

# accediendo a todas las filas de una columna usando slices
apellidos = df.iloc[:,1]
print(apellidos)

# accediendo a la fila 3 usando slices
fila_3 = df.iloc[2,:]
print(fila_3)

# accediendo a las filas con edad mayor a 30 usando slices
mayor_que_30 = df.loc[df["edad"]>30,:]
print(mayor_que_30)