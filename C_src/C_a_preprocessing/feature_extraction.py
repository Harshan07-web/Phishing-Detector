import re
import urllib.parse

def extract_features(url: str) -> dict:
    """Extract 48 handcrafted features from the URL."""
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc
    path = parsed.path

    features = {
        'url_length': len(url),
        'domain_length': len(domain),
        'path_length': len(path),
        'num_dots': url.count('.'),
        'num_hyphens': url.count('-'),
        'num_underscores': url.count('_'),
        'num_slashes': url.count('/'),
        'num_digits': sum(c.isdigit() for c in url),
        'num_letters': sum(c.isalpha() for c in url),
        'num_params': url.count('='),
        'num_ampersand': url.count('&'),
        'num_question': url.count('?'),
        'num_equal': url.count('='),
        'num_percent': url.count('%'),
        'num_at': url.count('@'),
        'num_tilde': url.count('~'),
        'num_comma': url.count(','),
        'num_semicolon': url.count(';'),
        'num_colon': url.count(':'),
        'num_hash': url.count('#'),
        'has_ip': 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0,
        'https': 1 if parsed.scheme == 'https' else 0,
        'has_www': 1 if 'www' in domain else 0,
        'has_login': 1 if 'login' in url.lower() else 0,
        'has_secure': 1 if 'secure' in url.lower() else 0,
        'has_bank': 1 if 'bank' in url.lower() else 0,
        'has_paypal': 1 if 'paypal' in url.lower() else 0,
        'has_signin': 1 if 'signin' in url.lower() else 0,
        'has_verification': 1 if 'verify' in url.lower() else 0,
        'num_subdomains': domain.count('.') - 1 if '.' in domain else 0,
        'domain_has_digits': 1 if any(c.isdigit() for c in domain) else 0,
        'starts_with_http': 1 if url.lower().startswith('http') else 0,
        'ends_with_slash': 1 if url.endswith('/') else 0,
        'is_short_url': 1 if any(s in url for s in ['bit.ly', 'goo.gl', 'tinyurl']) else 0,
        'contains_mailto': 1 if 'mailto:' in url else 0,
        'contains_exe': 1 if '.exe' in url else 0,
        'contains_zip': 1 if '.zip' in url else 0,
        'contains_php': 1 if '.php' in url else 0,
        'contains_html': 1 if '.html' in url else 0,
        'contains_javascript': 1 if '.js' in url else 0,
        'contains_pdf': 1 if '.pdf' in url else 0,
        'contains_redirect': 1 if '//' in path[1:] else 0,
        'count_uppercase': sum(1 for c in url if c.isupper()),
        'ratio_digits': sum(c.isdigit() for c in url) / len(url),
        'ratio_special_chars': sum(not c.isalnum() for c in url) / len(url)
    }

    return features
