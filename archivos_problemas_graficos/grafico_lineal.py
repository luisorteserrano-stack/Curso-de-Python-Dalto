import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos/pedos.csv")

sns.lineplot(x="fecha", y="pedos", data=df) # Creamos el gráfico de líneas

plt.plot("01-09",15,"o") # Marcamos manualmente el punto más alto

plt.show() # Mostramos el gráfico
