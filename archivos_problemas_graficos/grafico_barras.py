import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos/cofla_ingresos.csv")

sns.barplot(x="fuentes", y="ingresos", data=df) # Creamos el gráfico de barras

# Oteniendo total de ingresos
total_ingresos = df["ingresos"].sum()

# Mostramos por consola el total de ingresos
print(f"El total de ingresos es de: ${total_ingresos} USD")

plt.show() # Mostramos el gráfico
