from urllib.parse import urlparse

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