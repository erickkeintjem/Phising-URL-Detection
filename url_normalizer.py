import re

def normalize_url(url):

    url = url.strip().lower()

    url = re.sub(
        r'^https?://',
        '',
        url
    )

    url = re.sub(
        r'^www\.',
        '',
        url
    )

    return url