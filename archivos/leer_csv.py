import csv

with open("archivos/datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
# Visual Studio Code recomienda la posibilidad de instalar "Rainbow CSV"
