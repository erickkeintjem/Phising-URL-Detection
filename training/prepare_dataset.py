import pandas as pd

print("Loading dataset...")

df = pd.read_csv(
    "dataset/malicious_phish.csv"
)

print("Original size:", len(df))

df = df.dropna()

df = df.drop_duplicates(
    subset=["url"]
)

df = df[
    df["type"].isin([
        "benign",
        "phishing"
    ])
]

df["label"] = df["type"].map({
    "benign": 0,
    "phishing": 1
})

df = df[
    ["url", "label"]
]

print("\nFinal distribution:")
print(df["label"].value_counts())

df.to_csv(
    "dataset/urls.csv",
    index=False
)

print("\nDataset saved.")