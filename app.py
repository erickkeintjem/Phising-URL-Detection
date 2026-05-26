from flask import Flask
from flask import render_template
from flask import request
from flask import Response

import csv
import joblib

from io import StringIO
from urllib.parse import urlparse

from scipy.sparse import hstack

from feature_extractor import extract_features
from feature_extractor import explain_url

from db_helper import get_history
from db_helper import save_scan
from db_helper import get_statistics
from db_helper import get_chart_data

from url_validator import is_valid_url
from url_normalizer import normalize_url

app = Flask(__name__)

TRUSTED_DOMAINS = [
    "google.com",
    "github.com",
    "youtube.com",
    "facebook.com",
    "instagram.com",
    "wikipedia.org",
    "microsoft.com",
    "apple.com",
    "openai.com",
    "linkedin.com",
    "x.com",
    "twitter.com",
    "amazon.com",
    "netflix.com",
    "yahoo.com",
    "reddit.com"
]

def is_trusted_domain(url):

    parsed = urlparse(url)

    domain = parsed.netloc.lower()

    if domain.startswith("www."):
        domain = domain[4:]

    return domain in TRUSTED_DOMAINS

model = joblib.load(
    "model/phishing_model.pkl"
)

vectorizer = joblib.load(
    "model/vectorizer.pkl"
)

scaler = joblib.load(
    "model/scaler.pkl"
)

@app.route("/")
def home():

    return render_template(
        "index.html"
    )

@app.route("/scan", methods=["POST"])
def scan():

    url = request.form["url"]

    if not is_valid_url(url):

        return render_template(
            "result.html",
            url=url,
            result="INVALID URL",
            confidence=0,
            features=[],
            reasons=[
                "URL tidak valid. Pastikan format URL benar."
            ]
        )

    normalized_url = normalize_url(
        url
    )

    tfidf = vectorizer.transform(
        [normalized_url]
    )

    features = extract_features(
        url
    )

    features_scaled = scaler.transform(
        [features]
    )

    final_features = hstack([
        tfidf,
        features_scaled
    ])

    if is_trusted_domain(url):

        result = "SAFE"

        confidence = 100

        reasons = [
            "Domain termasuk daftar situs terpercaya."
        ]

        save_scan(
            url,
            result,
            confidence
        )

        return render_template(
            "result.html",
            url=url,
            result=result,
            confidence=confidence,
            features=features,
            reasons=reasons
        )

    prediction = model.predict(
        final_features
    )[0]

    probability = model.predict_proba(
        final_features
    )[0]

    confidence = round(
        max(probability) * 100,
        2
    )

    result = (
        "PHISHING"
        if prediction == 1
        else "SAFE"
    )

    reasons = explain_url(
        url
    )

    save_scan(
        url,
        result,
        confidence
    )

    return render_template(
        "result.html",
        url=url,
        result=result,
        confidence=confidence,
        features=features,
        reasons=reasons
    )

@app.route("/history")
def history():

    data = get_history()

    return render_template(
        "history.html",
        history=data
    )

@app.route("/admin")
def admin():

    stats = get_statistics()

    history = get_history()

    chart_labels, chart_data = get_chart_data()

    threat_rate = 0

    if stats["total_scan"] > 0:

        threat_rate = round(
            (
                stats["total_phishing"]
                /
                stats["total_scan"]
            ) * 100,
            2
        )

    return render_template(
        "admin.html",
        stats=stats,
        threat_rate=threat_rate,
        history=history[:10],
        safe_count=stats["total_safe"],
        phishing_count=stats["total_phishing"],
        chart_labels=chart_labels,
        chart_data=chart_data
    )

@app.route("/export")
def export_csv():

    data = get_history()

    output = StringIO()

    writer = csv.writer(
        output
    )

    writer.writerow([
        "ID",
        "URL",
        "Prediction",
        "Confidence",
        "Scan Date"
    ])

    for row in data:
        writer.writerow(row)

    csv_data = output.getvalue()

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=scan_history.csv"
        }
    )

@app.route("/about")
def about():

    return render_template(
        "about.html"
    )

if __name__ == "__main__":

    app.run(
        debug=True
    )