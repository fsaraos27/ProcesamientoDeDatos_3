# pasar a dolar cada deuda, guardar en lista, iterar en la lista, mostrar 10 primeros valores
print("")

# RUT;Nombre;Genero;Fecha_Nacimiento;Previsión;Monto_Deuda

import pandas as pd

df_pacientes = pd.read_csv("/Users/franciscosaraosgarcia/Desktop/Ejercicios_Ucatolica/Caso_Practico3/datos_pacientes.csv", encoding = "utf-8", sep = ";" )
# df_pacientes = pd.DataFrame(df_pacientes)
print(df_pacientes)

# print(df_pacientes["RUT"].str[11])


# itera sobre la columna monto deuda y cambia el valor a dolares mostrando los 10 primeros en pantalla
listaDolar = []
for index, row in df_pacientes.iterrows():
    valor = row["Monto_Deuda"]
    valor /= 200
    listaDolar.append(valor)

print(listaDolar[0:10])

# Muestra los nombres con los primeros 10 caracteres de los nombres
print(df_pacientes["Nombre"].str[0:10])

# Cambiar los nombres a Mayusculas
df_pacientes["Nombre"] = df_pacientes["Nombre"].str.upper()
print(df_pacientes.head())

# Extraer los nombres con letra Ñ
print(df_pacientes.loc[df_pacientes["Nombre"].str.find("Ñ")])


# Cargar informacion de un DataFrame a otro
df_pacientes2 = pd.read_csv("/Users/franciscosaraosgarcia/Desktop/Ejercicios_Ucatolica/Caso_Practico3/datos_pacientes2.csv", encoding = "utf-8", sep = ";" )
# df_pacientes2 = pd.DataFrame(df_pacientes2)
print(df_pacientes2)

# Eliminar filas con datos corruptos: XXXX
df_pacientes2 = df_pacientes2.loc[~(df_pacientes2["RUT"].str.contains("XXXX")) & ~(df_pacientes2["Nombre"].str.contains("XXXX"))]
print(df_pacientes2)

# Separar nombres y apellidos con espacios
df_pacientes2["Nombre"] = df_pacientes2["Nombre"].str.replace("-", " ")
print(df_pacientes2)

# Limpiar _ de fecha de nacimiento
print(df_pacientes2)
df_pacientes2["Fecha_Nacimiento"] = df_pacientes2["Fecha_Nacimiento"].str.replace("_/","/")
print(df_pacientes2)

# Unir los Data Frame
print("")
df_pacientes = df_pacientes.append(df_pacientes2)
print(df_pacientes.tail())
print("")

# Setear Index por la columna RUT
df_pacientes = df_pacientes.set_index("RUT")
print(df_pacientes)

# Separar la columna nombre en 4 (Primer nombre, Segundo nombre, Primer apellido, Segundo apellido)
print(df_pacientes["Nombre"].str.split(" "))
df_pacientes3 = df_pacientes["Nombre"].str.split(" ", expand = True)
print(df_pacientes3)
df_pacientes3.columns = ["Primer nombre", "Segundo nombre", "Primer apellido", "Segundo apellido"]
print(df_pacientes3)


# Agregar columnas al Data Frame 
df_pacientes = df_pacientes.join(df_pacientes3)
print(df_pacientes)
print("")

# Conectar BD "Nacionalidad"
nacionalidad = pd.read_csv("/Users/franciscosaraosgarcia/Desktop/Ejercicios_Ucatolica/Caso_Practico3/nacionalidad.csv", encoding = "utf-8", sep = ";" )
print(nacionalidad)
nacionalidad = nacionalidad.set_index("RUT")
print(nacionalidad)
print("")
print(df_pacientes)
print("")
# Unir data Frame "nacionalidad" con Data Frame ortiginal
df_pacientes = df_pacientes.join(nacionalidad)
print(df_pacientes)

# Asociar Data Frame "nacionalidad" con los Rut de las personas
df_pacientes = df_pacientes.merge(nacionalidad,left_index=True,right_on="RUT",how="left")
print(df_pacientes)
print("")