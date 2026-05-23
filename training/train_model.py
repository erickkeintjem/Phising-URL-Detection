import pandas as pd
import joblib

from scipy.sparse import hstack

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from feature_extractor import extract_features

print("Loading dataset...")

df = pd.read_csv(
    "dataset/training_urls.csv"
)

print("Total data:", len(df))

print("Extracting features...")

url_features = df["url"].apply(
    extract_features
).tolist()

X_features = pd.DataFrame(url_features)

print("Creating TF-IDF...")

vectorizer = TfidfVectorizer(
    analyzer="char",
    ngram_range=(2, 4),
    max_features=5000
)

X_tfidf = vectorizer.fit_transform(
    df["url"]
)

print("Scaling features...")

scaler = StandardScaler()

X_features_scaled = scaler.fit_transform(
    X_features
)

print("Combining features...")

X = hstack([
    X_tfidf,
    X_features_scaled
])

y = df["label"]

print("Splitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training model...")

model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_train,
    y_train
)

print("Evaluating model...")

y_pred = model.predict(
    X_test
)

print("\nAccuracy:")
print(
    accuracy_score(
        y_test,
        y_pred
    )
)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        y_pred
    )
)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred
    )
)

joblib.dump(
    model,
    "model/phishing_model.pkl"
)

joblib.dump(
    vectorizer,
    "model/vectorizer.pkl"
)

joblib.dump(
    scaler,
    "model/scaler.pkl"
)

print("\nModel saved successfully.")