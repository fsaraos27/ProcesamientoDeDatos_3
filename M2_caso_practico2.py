import pandas as pd
print("")
print("Nombre de columnas")
""" Fecha_Hora_Consulta;RUT;Especialidad;Diag;RUT2;Costo_consulta """

# Conectarse a la BD y transformarla a un DataFrame
df_consultas = pd.read_csv("/Users/franciscosaraosgarcia/Desktop/Ejercicios_Ucatolica/Caso_Practico2/consultas.csv", encoding = "utf-8", sep = ";" )
df_consultas = pd.DataFrame(df_consultas)

# imprime la informacion como un DataFrame
print(df_consultas)

# Imprime el tipo de datos de las columnas
print(df_consultas.dtypes)

# Se cambia el tipo de datos de la columna: object a datatime64
df_consultas["Fecha_Hora_Consulta"] = df_consultas["Fecha_Hora_Consulta"].astype("datetime64")

# Imprime el tipo de datos de las columnas
print(df_consultas.dtypes)
print("Se imprime el total de filas, columnas y datos")
print("Cantidad Filas y Columnas: ", df_consultas.shape)
print("Cantidad de Datos: ", df_consultas.size)

# Se cambia el indice por los RUT
df_consultas = df_consultas.set_index("RUT")
print(df_consultas)
print("")

# Se imprimen los 10 primeros valores
print(df_consultas.head(10))
print("")

# Se imprimen los 10 ultimos valores
print(df_consultas.tail(10))
print("")

# Se trae el rut 6.079.686-2
print(df_consultas.loc["6.079.686-2" ])

# Trae la fila del indice 23
print("Trae la fila del indice 23 : ")
print(df_consultas.iloc[23])
print("")

# Trae las filas del 76 al 89
print("Trae las filas del 76 al 89 : ")
print(df_consultas.iloc[76:90])

# Cambiar nombres de las columnas: Fecha_Hora_Consulta y RUT2
df_consultas = df_consultas.rename(columns = {"Fecha_Hora_Consulta" : "Fecha_Consulta"})
print(df_consultas.dtypes)
print(df_consultas)
df_consultas = df_consultas.rename(columns = {"RUT2" : "RUT_medico"})
print(df_consultas)
print("")

# Agrega el valor 10.000 a los NaN de Costo_Consulta
df_consultas = df_consultas.fillna(10000)
print(df_consultas)
print(df_consultas.iloc[76:90])
print("")
print("")

# Conectarse a la BD consultas2, transformarla a un DataFrame y agregar las columnas faltantes a df_consultas
df_consultas2 = pd.read_csv("/Users/franciscosaraosgarcia/Desktop/Ejercicios_Ucatolica/Caso_Practico2/consultas2.csv", encoding = "utf-8", sep = ";")
df_consultas2 = pd.DataFrame(df_consultas2)
df_consultas2 = df_consultas2.set_index("RUT")
df_consultas2 = df_consultas2.rename(columns = {"Fecha_Hora_Consulta" : "Fecha_Consulta"})
df_consultas2 = df_consultas2.rename(columns = {"RUT2" : "RUT_medico"})
print(df_consultas2)
print("")
df_consultas = df_consultas.append(df_consultas2)
print("")
print(df_consultas)
print("")

# Borrar filas
df_consultas = df_consultas.drop(df_consultas.iloc[0:10].index)
print(df_consultas)
