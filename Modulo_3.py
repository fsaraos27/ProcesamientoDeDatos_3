# Se accede a la BD y se crea el dataFrame
print("")

import pandas as pd
df_ejemplo = pd.read_csv("/Users/franciscosaraosgarcia/Desktop/Ejercicios_Ucatolica/Caso_Practico3/ejemplo.csv", encoding = "latin-1", sep = ";" )
df_ejemplo = pd.DataFrame(df_ejemplo)
print(df_ejemplo)

# Iteracion sobre el DataFrame
for index, row in df_ejemplo.iterrows():
    print(index)
    print(row["RUT"])

# extrae el primer nombre del dataFrame
    primer_nombre = row["Nombre"].split(" ")[0]
    print(primer_nombre)

# Cuenta cada caracter de la columna Nombre
print(df_ejemplo["Nombre"].str.len())

# Extrae caracteres de un DataFrame
print(df_ejemplo["RUT"].str[0])

# Transforma a minuscula el texto de la columna
print(df_ejemplo["Nombre"].str.lower())

# Transforma a mayuscula el texto de la columna
print(df_ejemplo["Nombre"].str.upper())

# Cambia el caracter / por - en la columna fecha
print(df_ejemplo["Fecha_Nac"].str.replace("/", "-"))

# Verifica si el parametro ingresado existe: True o False
print(df_ejemplo["Fecha_Nac"].str.contains("/"))

# Encuentra la posicion del valor ingresado por parametro
print(df_ejemplo["Nombre"].str.find(" "))

# Separa los valores
print(df_ejemplo["Nombre"].str.split(" "))

# Crea columnas para separar por primer y segundo nombre, primer y segundo apellido
df = df_ejemplo["Nombre"].str.split(" ", expand=True)
print(df)

# Cambiar nombre de las columnas
df.columns = ["Primer nombre", "Segundo nombre", "Primer apellido", "Segundo apellido"]
print(df)

# Agrega columnas al DataFrame original
df_ejemplo = df_ejemplo.join(df)
print(df_ejemplo.dtypes)
print("")

# Diferencia por DataFrame cuando hay mas de una columna con el mismo nombre
df_ejemplo = df_ejemplo.join(df, rsuffix = "_df", lsuffix = "_df_ejemplo")
print(df_ejemplo.dtypes)
print("")