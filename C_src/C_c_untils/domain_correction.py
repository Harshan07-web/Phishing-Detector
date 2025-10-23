import tldextract

def correct_domain(url: str) -> str:
    """Correct and normalize domain structure."""
    ext = tldextract.extract(url)
    if not ext.domain or not ext.suffix:
        return url  # Invalid domain
    return f"{ext.domain}.{ext.suffix}"
