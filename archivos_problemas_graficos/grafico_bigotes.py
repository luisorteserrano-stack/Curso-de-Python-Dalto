import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos/bigotes.csv")

sns.boxplot(x="categoria", y="valor", data=df) # Creamos el gráfico de bigotes

plt.show() # Mostramos el gráfico
