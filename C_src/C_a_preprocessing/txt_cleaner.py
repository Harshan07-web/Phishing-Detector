import re

def clean_url(url: str) -> str:
    url = url.strip().lower()  # remove spaces, lowercase
    url = re.sub(r'https?://', '', url)  # remove http/https
    url = re.sub(r'www\.', '', url)  # remove www
    url = re.sub(r'[^a-zA-Z0-9./_-]', '', url)  # remove strange characters
    return url
