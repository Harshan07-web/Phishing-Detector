import re
import socket
import urllib.parse as urlparse
from tldextract import extract

def extract_url_features(url):
    # Ensure URL has a scheme for accurate parsing
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url

    # Parse URL
    parsed = urlparse.urlparse(url)
    hostname = parsed.hostname or ""
    path = parsed.path or ""
    query = parsed.query or ""
    ext = extract(url) 

    
    # --- Base features ---
    NumDots = url.count('.')
    SubdomainLevel = len(ext.subdomain.split('.')) if ext.subdomain else 0
    PathLevel = path.count('/')
    UrlLength = len(url)
    NumDash = url.count('-')
    NumDashInHostname = hostname.count('-')
    AtSymbol = 1 if '@' in url else 0
    TildeSymbol = 1 if '~' in url else 0
    NumUnderscore = url.count('_')
    NumPercent = url.count('%')
    NumQueryComponents = query.count('=') if query else 0
    NumAmpersand = query.count('&')
    NumHash = url.count('#')
    NumNumericChars = len(re.findall(r'[0-9]', url))
    NoHttps = 0 if url.lower().startswith('https') else 1
    RandomString = 1 if re.search(r'[a-zA-Z0-9]{15,}', hostname) else 0
    
# Your original regex was slightly wrong. Use re.fullmatch
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    IpAddress = 1 if re.fullmatch(ip_pattern, hostname) else 0

    DomainInSubdomains = 1 if ext.domain in ext.subdomain else 0
    DomainInPaths = 1 if ext.domain in path else 0
    HttpsInHostname = 1 if 'https' in hostname else 0
    HostnameLength = len(hostname)
    PathLength = len(path)
    QueryLength = len(query)
    DoubleSlashInPath = 1 if '//' in path else 0
    
    sensitive_words = ['secure', 'account', 'login', 'bank', 'update', 'verify']
    NumSensitiveWords = sum(word in url.lower() for word in sensitive_words)
            
    # --- Placeholder features ---
    # (These remain the same)
    EmbeddedBrandName = 0
    PctExtHyperlinks = 0
    PctExtResourceUrls = 0
    ExtFavicon = 0
    InsecureForms = 0
    RelativeFormAction = 0
    ExtFormAction = 0
    AbnormalFormAction = 0
    PctNullSelfRedirectHyperlinks = 0
    FrequentDomainNameMismatch = 0
    FakeLinkInStatusBar = 0
    RightClickDisabled = 0
    PopUpWindow = 0
    SubmitInfoToEmail = 0
    IframeOrFrame = 0
    MissingTitle = 0
    ImagesOnlyInForm = 0
    SubdomainLevelRT = SubdomainLevel
    UrlLengthRT = UrlLength
    PctExtResourceUrlsRT = 0
    AbnormalExtFormActionR = 0
    ExtMetaScriptLinkRT = 0
    PctExtNullSelfRedirectHyperlinksRT = 0

    # Combine all features into dict
    features = {
        "NumDots": NumDots,
        "SubdomainLevel": SubdomainLevel,
        "PathLevel": PathLevel,
        "UrlLength": UrlLength,
        "NumDash": NumDash,
        "NumDashInHostname": NumDashInHostname,
        "AtSymbol": AtSymbol,
        "TildeSymbol": TildeSymbol,
        "NumUnderscore": NumUnderscore,
        "NumPercent": NumPercent,
        "NumQueryComponents": NumQueryComponents,
        "NumAmpersand": NumAmpersand,
        "NumHash": NumHash,
        "NumNumericChars": NumNumericChars,
        "NoHttps": NoHttps,
        "RandomString": RandomString,
        "IpAddress": IpAddress,
        "DomainInSubdomains": DomainInSubdomains,
        "DomainInPaths": DomainInPaths,
        "HttpsInHostname": HttpsInHostname,
        "HostnameLength": HostnameLength,
        "PathLength": PathLength,
        "QueryLength": QueryLength,
        "DoubleSlashInPath": DoubleSlashInPath,
        
        # --- REMOVED Old Feature ---
        "NumSensitiveWords": NumSensitiveWords, 
    
        
        # --- Placeholder Features ---
        "EmbeddedBrandName": EmbeddedBrandName,
        "PctExtHyperlinks": PctExtHyperlinks,
        "PctExtResourceUrls": PctExtResourceUrls,
        "ExtFavicon": ExtFavicon,
        "InsecureForms": InsecureForms,
        "RelativeFormAction": RelativeFormAction,
        "ExtFormAction": ExtFormAction,
        "AbnormalFormAction": AbnormalFormAction,
        "PctNullSelfRedirectHyperlinks": PctNullSelfRedirectHyperlinks,
        "FrequentDomainNameMismatch": FrequentDomainNameMismatch,
        "FakeLinkInStatusBar": FakeLinkInStatusBar,
        "RightClickDisabled": RightClickDisabled,
        "PopUpWindow": PopUpWindow,
        "SubmitInfoToEmail": SubmitInfoToEmail,
        "IframeOrFrame": IframeOrFrame,
        "MissingTitle": MissingTitle,
        "ImagesOnlyInForm": ImagesOnlyInForm,
        "SubdomainLevelRT": SubdomainLevelRT,
        "UrlLengthRT": UrlLengthRT,
        "PctExtResourceUrlsRT": PctExtResourceUrlsRT,
        "AbnormalExtFormActionR": AbnormalExtFormActionR,
        "ExtMetaScriptLinkRT": ExtMetaScriptLinkRT,
        "PctExtNullSelfRedirectHyperlinksRT": PctExtNullSelfRedirectHyperlinksRT
    }

    return features