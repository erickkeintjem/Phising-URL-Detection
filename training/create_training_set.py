import pandas as pd

df = pd.read_csv("dataset/urls.csv")

safe = df[df["label"] == 0]
danger = df[df["label"] == 1]

safe_sample = safe.sample(
    n=5000,
    random_state=42
)

danger_sample = danger.sample(
    n=5000,
    random_state=42
)

final_df = pd.concat([
    safe_sample,
    danger_sample
])

final_df = final_df.sample(
    frac=1,
    random_state=42
)

final_df.to_csv(
    "dataset/training_urls.csv",
    index=False
)

print(final_df["label"].value_counts())
print("Total:", len(final_df))