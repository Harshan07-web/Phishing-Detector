import logging
from urllib.parse import urlparse
from difflib import SequenceMatcher, get_close_matches
from typing import Optional, Tuple, Iterable
import tldextract

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

# A compact list of commonly-used domains to consider for misspelling correction.
# Tweak this list to match your audience / presentation needs.
COMMON_DOMAINS = {
    "google.com",
    "facebook.com",
    "youtube.com",
    "yahoo.com",
    "amazon.com",
    "microsoft.com",
    "apple.com",
    "linkedin.com",
    "instagram.com",
    "paypal.com",
    "github.com",
    "reddit.com",
    "whatsapp.com",
    "twitch.tv",
    "bing.com",
    "outlook.com",
    "icloud.com",
    "spotify.com",
    "netflix.com",
}

def _registered_domain_from_target(target: str) -> Optional[str]:
    """
    Return the registered domain like 'example.co.uk' or None if not parseable.
    """
    ext = tldextract.extract(target)
    if not ext.domain or not ext.suffix:
        return None
    return f"{ext.domain}.{ext.suffix}"

def _best_match(candidate: str, pool: Iterable[str]) -> Optional[Tuple[str, float]]:
    """
    Return (best_match, ratio) for 'candidate' against 'pool' using SequenceMatcher.
    Returns None if pool is empty.
    """
    pool_list = list(pool)
    if not pool_list:
        return None

    # Quick: use get_close_matches for candidate shortlist, then refine with ratio.
    shortlist = get_close_matches(candidate, pool_list, n=5, cutoff=0.6)
    if not shortlist:
        return None

    best = None
    best_ratio = 0.0
    for p in shortlist:
        ratio = SequenceMatcher(None, candidate, p).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best = p
    return (best, best_ratio) if best is not None else None

def correct_domain(url: str,
                   common_domains: Iterable[str] = COMMON_DOMAINS,
                   similarity_threshold: float = 0.86
                   ) -> Tuple[str, bool]:
    """
    Parse `url` and return (domain, corrected_flag).

    - If the parsed registered domain exactly matches a known common domain -> considered legitimate (no correction).
    - If parsed registered domain is a likely typo of a known common domain (similarity >= threshold) -> return corrected domain, corrected_flag=True
    - Otherwise return the parsed registered domain and corrected_flag=False

    Returned domain is always the 'registered domain' (domain + suffix) like 'example.com' or 'example.co.uk'.
    If parsing fails, the original input `url` is returned with corrected_flag=False.
    """
    raw = (url or "").strip()
    if not raw:
        logging.warning("Empty URL passed to correct_domain()")
        return url, False

    parsed = urlparse(raw)
    target = parsed.netloc or parsed.path  # allow urls without scheme, like 'google.com/path'
    if not target:
        logging.warning("Could not determine host part for: %s", url)
        return url, False

    registered = _registered_domain_from_target(target)
    if not registered:
        logging.warning("Invalid or unparsable domain in URL: %s", url)
        return url, False

    # If it's exactly one of the known legitimate domains, don't correct.
    if registered in common_domains:
        logging.info("Legitimate common domain detected: %s (no correction)", registered)
        return registered, False

    # Try to find a close common-domain candidate
    match = _best_match(registered, common_domains)
    if match:
        best, ratio = match
        logging.debug("Best fuzzy match for %s -> %s (ratio=%.3f)", registered, best, ratio)
        # Only correct when the best match is sufficiently similar and is different
        if ratio >= similarity_threshold and best != registered:
            logging.info("Corrected misspelt domain '%s' -> '%s' (ratio=%.2f)", registered, best, ratio)
            return best, True

    # No correction — return the cleaned registered domain
    return registered, False
