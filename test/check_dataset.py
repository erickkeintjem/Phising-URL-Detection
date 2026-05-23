import pandas as pd

df = pd.read_csv("dataset/malicious_phish.csv")

print(df["type"].value_counts())