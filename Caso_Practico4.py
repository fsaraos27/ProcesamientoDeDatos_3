import pandas as pd
from pandas.core.arrays.categorical import contains
import numpy as np

df_pacientes = pd.read_csv("/Users/franciscosaraosgarcia/Desktop/Ejercicios_Ucatolica/Caso_Practico4/datos_pacientes3.csv",encoding="utf-8",sep=";")
print(df_pacientes)

# Eliminar columna "Precio_prod"
#del df_pacientes["Genero"]
#print(df_pacientes)

# Filtrar pacientes que no sean de chile
print(df_pacientes.loc[df_pacientes["País_origen"] != "Chile"])

# Filtra pacientes que no sean de chile con deuda mayor a 1000000
print(df_pacientes.loc[(df_pacientes["País_origen"] != "Chile") & (df_pacientes["Monto_Deuda"] > 1000000)])

# Filtrar pacientes que no sean de chile, deuda mayor a 1000000 y fonasa
print(df_pacientes.loc[(df_pacientes["País_origen"] != "Chile") & (df_pacientes["Monto_Deuda"] > 1000000) & (df_pacientes["Previsión"] == "FONASA")])

# Filtrar pacientes de chile: Santiago, concepcion, deuda mayor a 1000000 y FONASA
print(df_pacientes.loc[(df_pacientes["País_origen"] == "Chile") & (df_pacientes["Ciudad_Residencia"] == "Santiago") | (df_pacientes["Ciudad_Residencia"] == "Concepción") & (df_pacientes["Monto_Deuda"] > 1000000) & (df_pacientes["Previsión"] == "FONASAS")])

# Cargar nueva base de datos
df_pacientes3 = pd.read_csv("/Users/franciscosaraosgarcia/Desktop/Ejercicios_Ucatolica/Caso_Practico4/datos_pacientes3.csv",sep=";")
print(df_pacientes3.head())

# Filtrar rut terminados en J
df_pacientes3 = df_pacientes3.loc[df_pacientes3["RUT"].str[-1:] != "J"]
print(df_pacientes3.head())

# unir df_pacientes con df_pacientes3
print(df_pacientes)
df_pacientes = df_pacientes.set_index("RUT")
df_pacientes3 = df_pacientes3.set_index("RUT")
df_pacientes = df_pacientes.append(df_pacientes3)
print(df_pacientes)

# Ordenar df_pacientes de forma ascendente mediante Monto Deuda y Fecha nacimiento
df_pacientes3 = df_pacientes3.sort_values(by = ["Monto_Deuda", "Fecha_Nacimiento"], ascending = True)
print(df_pacientes3.head())

# Extraer la media, minimo, maximo de la deuda por tipo de prevision
df_pacientes3 = df_pacientes3.pivot_table(index = "Previsión", values = "Monto_Deuda", aggfunc = {np.mean, np.min, np.max})
print(df_pacientes3)


# Suma de cada consulta con RUT del medico
df_consultas = pd.read_csv("/Users/franciscosaraosgarcia/Desktop/Ejercicios_Ucatolica/Caso_Practico2/consultas.csv", encoding = "utf-8", sep=";")
print(df_consultas)
print(df_consultas.dtypes)
df_consultas["Costo_consulta"] = df_consultas["Costo_consulta"].astype("int64")
print(df_consultas.dtypes)

pt2 = df_consultas.pivot_table(index = "RUT2", values = "Costo_consulta", aggfunc = np.sum)
print(pt2)

# Realizar un merge mediante el RUT de cada RUT_medico
df_consultas = df_consultas.merge(pt2, left_on = "RUT_medico", right_on = "RUT_medico", how = "left")
print(df_consultas)