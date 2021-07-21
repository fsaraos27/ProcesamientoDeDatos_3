import pandas as pd
from pandas.core.arrays.categorical import contains
import numpy as np

print("")

# Cargamos el archivo "Detalle Boletas" en un Data Frame
df_boletas = pd.read_csv("/Users/franciscosaraosgarcia/Desktop/Ejercicios_Ucatolica/Trabajo_Final_UC/detalle_boletas.csv", encoding = "utf-8", sep = ",")
#df_boletas = pd.DataFrame(df_boletas)
print(df_boletas)
print(df_boletas.dtypes)

# Eliminar columna "Precio_prod"
del df_boletas["Precio_prod"]
print(df_boletas)

# Crear columna "Pais_Venta" con valores "Chile"
df_boletas["Pais_Venta"] = "Chile"
print(df_boletas)

# Cambiar el nombre de la columna "NXXX" por "Num Boleta"
df_boletas = df_boletas.rename(columns = {"NXXX" : "Num Boleta"})
print(df_boletas)

# Eliminar caracteres extras en la columna "Fecha"
df_boletas["Fecha"] = df_boletas["Fecha"].str.replace("!","")
df_boletas["Fecha"] = df_boletas["Fecha"].str.replace("{","")
df_boletas["Fecha"] = df_boletas["Fecha"].str.replace("-","")
df_boletas["Fecha"] = df_boletas["Fecha"].str.replace(".","")
print(df_boletas)

# Separar la columna "Fecha" en tres columnas: "Año", "Mes", "Dia"
print(df_boletas["Fecha"].str.split("/"))
df_boletas2 = df_boletas["Fecha"].str.split("/", expand = True)
print(df_boletas2)
df_boletas2.columns = ["Año", "Mes", "Dia"]
print(df_boletas2)

# Agregar nuevas columnas de "Fecha" al Data Frame
df_boletas = df_boletas.join(df_boletas2)
print(df_boletas)

# Eliminar columna "Fecha"
del df_boletas["Fecha"]
print(df_boletas)

# Eliminar filas con valores de la columna "ID" con valores "4XXXXX" y la columna "Num Boleta" con valores "55417XXXXXXX"
df_boletas = df_boletas.loc[~(df_boletas["ID"].str.contains("4XXXXX")) & ~(df_boletas["Num Boleta"].str.contains("55417XXXXXXX"))]
print(df_boletas)

# Cargar csv "Lista productos"
lista_productos = pd.read_csv("/Users/franciscosaraosgarcia/Desktop/Ejercicios_Ucatolica/Trabajo_Final_UC/lista productos.csv", encoding = "utf-8", sep = ",")
print(lista_productos)

lista_productos["ID"] = lista_productos["ID"].astype("object")
print(lista_productos.dtypes)
print(df_boletas.dtypes)

# Unir ambos Data Frame
detalle_boletas2 = pd.merge(df_boletas, lista_productos, on = "ID", how = "left")
print(detalle_boletas2)

# Crear columna "Ingreso Total" con el total entre la columna "Cantidad y Precio Unitario"
detalle_boletas2["Ingreso Total"] = detalle_boletas2["Cantidad"] * detalle_boletas2["Precio Unitario"]
print(detalle_boletas2)

# Calcular e imprimir estadisticos descriptivos de la columna "Cantidad" para todo el Data frame
df_boletas = df_boletas.pivot_table(index = "ID", values = "Cantidad", aggfunc = {np.mean, np.min, np.max, np.std})
print(df_boletas)

print("")

# Calcular e imprimir estadisticos descriptivos de la columna "Ingreso Total" para todo el Data frame
detalle_boletas2 = detalle_boletas2.pivot_table(index = "ID", values = "Ingreso Total", aggfunc = {np.mean, np.min, np.max, np.std})
print(detalle_boletas2)

print("")
