import pandas as pd

print("Loading dataset...")

df = pd.read_csv(
    "dataset/malicious_phish.csv"
)

print("Original size:", len(df))

# Hapus data kosong
df = df.dropna()

# Hapus duplikat
df = df.drop_duplicates(subset=["url"])

# Konversi label
df["label"] = df["type"].apply(
    lambda x: 0 if x == "benign" else 1
)

# Ambil kolom yang diperlukan
df = df[["url", "label"]]

print("\nFinal distribution:")
print(df["label"].value_counts())

# Simpan dataset final
df.to_csv(
    "dataset/urls.csv",
    index=False
)

print("\nDataset saved.")