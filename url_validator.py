import re
from urllib.parse import urlparse


def is_valid_url(url):
    url = (url or "").strip()
    if not url:
        return False
    if " " in url:
        return False

    # Require a hostname.
    parsed = urlparse(url if url.startswith(("http://", "https://")) else f"https://{url}")

    if not parsed.netloc or parsed.netloc.endswith("."):
        return False

    host = parsed.netloc

    # Allow IPv4 host.
    if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", host):
        parts = host.split(".")
        if all(0 <= int(p) <= 255 for p in parts):
            return True
        return False

    # Disallow non-domain-like hosts (e.g., "halo dunia").
    # Host must be composed of labels separated by dots.
    if not re.fullmatch(r"[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+", host):
        return False

    # Require TLD of letters only and length >= 2.
    if not re.search(r"\.([A-Za-z]{2,})$", host):
        return False

    return True
