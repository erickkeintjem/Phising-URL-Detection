# PhishGuard - Phishing URL Detection System

## Deskripsi

PhishGuard adalah aplikasi berbasis web yang digunakan untuk mendeteksi URL phishing menggunakan Machine Learning.

Sistem menganalisis URL berdasarkan:

- TF-IDF Vectorization
- Lexical Feature Extraction
- Logistic Regression

Kemudian sistem memberikan:

- Status URL (SAFE / PHISHING)
- Confidence Score
- Risk Analysis
- Scan History
- Dashboard Statistik

---

## Fitur

- URL Scanning
- Phishing Detection
- Explainable Result
- Risk Analysis
- Scan History
- Admin Dashboard
- Export CSV
- URL Validation

---

## Dataset

Dataset berasal dari Kaggle:

- Benign URLs
- Phishing URLs
- Malware URLs
- Defacement URLs

Total data training:

10.000 URL

- 5.000 Safe URLs
- 5.000 Phishing URLs

---

## Machine Learning

Model:

- Logistic Regression

Feature Engineering:

- TF-IDF
- URL Length
- Digit Count
- Special Characters
- Subdomain Count
- HTTPS Usage
- Suspicious Words
- IP Address Detection
- URL Shortener Detection

Accuracy:

91.95%

---

## Technology Stack

Backend:

- Python
- Flask

Machine Learning:

- Scikit-Learn
- Pandas
- NumPy
- SciPy

Database:

- SQLite

Frontend:

- HTML
- CSS
- JavaScript

---

## Installation

Clone repository:

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

Masuk ke folder project:

```bash
cd REPOSITORY
```

Install dependency:

```bash
pip install -r requirements.txt
```

Jalankan aplikasi:

```bash
python app.py
```

Buka browser:

```text
http://127.0.0.1:5000
```

---

## Project Structure

```text
app.py
db_helper.py
feature_extractor.py
risk_analyzer.py
url_validator.py

model/
dataset/
templates/
static/
```

---

## Author

Nama Anda
Universitas Anda
2026
