import re
from urllib.parse import urlparse

SUSPICIOUS_WORDS = [
    "login",
    "verify",
    "secure",
    "account",
    "update",
    "password",
    "signin",
    "banking",
    "paypal",
    "confirm"
]

SHORTENERS = [
    "bit.ly",
    "tinyurl.com",
    "goo.gl",
    "t.co"
]

SUSPICIOUS_TLDS = [
    ".xyz",
    ".top",
    ".click",
    ".info",
    ".biz"
]


def extract_features(url):

    parsed = urlparse(url)

    url_length = len(url)

    digit_count = sum(
        c.isdigit() for c in url
    )

    special_char_count = len(
        re.findall(
            r'[@\-_=#%&?]',
            url
        )
    )

    subdomain_count = parsed.netloc.count('.')

    https = int(
        parsed.scheme == "https"
    )

    suspicious_word_count = sum(
        word in url.lower()
        for word in SUSPICIOUS_WORDS
    )

    has_ip = int(
        bool(
            re.search(
                r'(\d{1,3}\.){3}\d{1,3}',
                parsed.netloc
            )
        )
    )

    is_shortened = int(
        any(
            shortener in url.lower()
            for shortener in SHORTENERS
        )
    )

    return [
        url_length,
        digit_count,
        special_char_count,
        subdomain_count,
        https,
        suspicious_word_count,
        has_ip,
        is_shortened
    ]


def explain_url(url):

    reasons = []

    parsed = urlparse(url)

    url_lower = url.lower()

    # Suspicious words
    found_words = []

    for word in SUSPICIOUS_WORDS:
        if word in url_lower:
            found_words.append(word)

    for word in found_words:
        reasons.append(
            f"Mengandung kata mencurigakan: {word}"
        )

    # HTTPS
    if parsed.scheme != "https":
        reasons.append(
            "Tidak menggunakan HTTPS"
        )

    # URL Length
    if len(url) > 75:
        reasons.append(
            "URL terlalu panjang"
        )

    # IP Address
    if re.search(
        r'(\d{1,3}\.){3}\d{1,3}',
        parsed.netloc
    ):
        reasons.append(
            "Menggunakan alamat IP sebagai domain"
        )

    # URL Shortener
    if any(
        shortener in url_lower
        for shortener in SHORTENERS
    ):
        reasons.append(
            "Menggunakan layanan URL shortener"
        )

    # Suspicious TLD
    for tld in SUSPICIOUS_TLDS:
        if parsed.netloc.lower().endswith(tld):
            reasons.append(
                f"Menggunakan domain mencurigakan ({tld})"
            )

    # Banyak subdomain
    if parsed.netloc.count('.') > 3:
        reasons.append(
            "Jumlah subdomain terlalu banyak"
        )

    # Banyak karakter spesial
    special_chars = len(
        re.findall(
            r'[@\-_=#%&?]',
            url
        )
    )

    if special_chars > 5:
        reasons.append(
            "Terlalu banyak karakter spesial pada URL"
        )

    if not reasons:
        reasons.append(
            "Tidak ditemukan indikator mencurigakan"
        )

    return reasons