import pandas as pd

# df = pd.read_csv("dataframes/edges.csv")
# # Guardar
# df.to_pickle("dataframes/edges.pkl")

# Recuperar
df = pd.read_pickle("dataframes/edges.pkl")


print(df.columns)
# print(df)
