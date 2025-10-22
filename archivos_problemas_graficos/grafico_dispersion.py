import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos/dispersion.csv")

sns.scatterplot(x="tiempo", y="dinero", data=df) # Creamos el gráfico de dispersión

plt.show() # Mostramos el gráfico
