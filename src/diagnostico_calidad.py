import pandas as pd

# Cada fila del archivo corresponde a una persona.
df = pd.read_csv("Data/Raw/Características y composición del hogar.csv", sep=";")
adultos = df[df["P6040"] >= 18].copy()

print("Registros originales:", len(df))
print("Adultos de todo el país:", len(adultos))

# El directorio identifica la vivienda. Para identificar a la persona usamos tres columnas.
llave_persona = ["DIRECTORIO", "SECUENCIA_P", "ORDEN"]
print("Personas duplicadas:", adultos.duplicated(subset=llave_persona).sum())

# Cuando alguien siempre vivió en el municipio, P753 queda vacío por el salto de la encuesta.
p753_vacio = adultos["P753"].isna()
siempre_vivio_aqui = adultos["P6074"] == 1
print("P753 vacío por salto de pregunta:", (p753_vacio & siempre_vivio_aqui).sum())
print("P753 vacío sin ese salto:", (p753_vacio & ~siempre_vivio_aqui).sum())

variables_bienestar = ["P1895", "P1896", "P1897", "P1898", "P1899", "P3175", "P1927"]

print("\nNulos en bienestar:")
print(adultos[variables_bienestar].isna().sum())
print("\nPorcentaje de nulos:")
print((adultos[variables_bienestar].isna().mean() * 100).round(2))

# Estas preguntas tienen escala de 0 a 10. Revisamos si hay códigos por fuera.
fuera_de_escala = (adultos[variables_bienestar] < 0) | (adultos[variables_bienestar] > 10)
print("\nValores fuera de 0 a 10:")
print(fuera_de_escala.sum())

# En P1896, el 99 significa que la persona no recibe ingresos.
print("\nPersonas con P1896 = 99:", (adultos["P1896"] == 99).sum())
print("Promedio de P1896 incluyendo el 99:", round(adultos["P1896"].mean(), 2))

ingresos_validos = adultos[(adultos["P1896"] >= 0) & (adultos["P1896"] <= 10)]
print("Promedio de P1896 entre 0 y 10:", round(ingresos_validos["P1896"].mean(), 2))

print("\nFalta identificar el municipio actual para analizar solo Bogotá.")
