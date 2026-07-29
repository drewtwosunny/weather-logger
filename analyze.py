import pandas as pd

df = pd.read_csv("data/weather_log.csv")
print(df.groupby("city")["humidity"].median())
print(df["city"].value_counts())