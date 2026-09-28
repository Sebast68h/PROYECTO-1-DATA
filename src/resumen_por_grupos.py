import pandas as pd

df = pd.read_csv("Data/Raw/Características y composición del hogar.csv", sep=";")
adultos = df[df["P6040"] >= 18].copy()

# P1895: satisfacción con la vida, de 0 a 10.
print("Satisfacción con la vida según sexo:")
print(adultos.groupby("P6020")["P1895"].agg(["count", "mean", "median"]).round(2))

print("\nSatisfacción con la vida según estado civil:")
print(adultos.groupby("P5502")["P1895"].agg(["count", "mean", "median"]).round(2))