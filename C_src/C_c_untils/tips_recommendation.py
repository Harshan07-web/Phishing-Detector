import random
import textwrap

def recommend_practices(features: dict, predicted_label: int) -> list[str]:
    """
    Generate smart, context-aware security recommendations.

    Args:
        features (dict): URL feature vector (e.g., NumDots, AtSymbol, UrlLength, etc.)
        predicted_label (int): 1 = Phishing, 0 = Legitimate

    Returns:
        list[str]: Curated list of practical security tips.
    """
    
    # Base advice sets
    general_safety = [
        "Always verify the sender’s email address before clicking any link.",
        "Hover over a link to preview the actual destination before visiting.",
        "Keep your browser and antivirus software up to date.",
        "Avoid entering login credentials on unfamiliar websites.",
        "Use two-factor authentication wherever possible."
    ]
    
    phishing_alerts = [
        "This URL shows multiple phishing indicators — avoid interacting with it.",
        "Check for spelling mistakes or extra words in the domain name.",
        "Be cautious of URLs with unusual or excessive subdomains.",
        "Do not download attachments or enter personal information from this link.",
        "If the website requests sensitive data unexpectedly, close it immediately."
    ]

    # Context-based smart tips
    context_tips = []
    
    # Example: too many dots
    if features.get("NumDots", 0) > 3:
        context_tips.append("This link contains many dots — attackers often use this to mimic legitimate domains.")
    
    # Example: '@' symbol
    if features.get("AtSymbol", 0) > 0:
        context_tips.append("Avoid URLs containing '@' symbols — everything before '@' is ignored by browsers and can hide real destinations.")
    
    # Example: long URL
    if features.get("UrlLength", 0) > 75:
        context_tips.append("The URL seems unusually long — long URLs are often used to disguise malicious parameters.")
    
    # Example: hyphens or underscores
    if features.get("NumDash", 0) > 2 or features.get("NumUnderscore", 0) > 2:
        context_tips.append("Too many dashes or underscores may indicate a spoofed site.")
    
    # Example: numeric domain parts
    if features.get("NumNumericChars", 0) > 3:
        context_tips.append("Legitimate domains rarely include many numbers — this could be suspicious.")
    
    # Example: missing HTTPS
    if features.get("HttpsToken", 0) == 0:
        context_tips.append("The site does not use HTTPS — avoid sharing sensitive data here.")
    
    # Example: URL shortening or encoded characters
    if features.get("NumPercent", 0) > 0:
        context_tips.append("Encoded characters (%xx) can obscure malicious redirects — avoid shortened or encoded URLs.")

    # Combine recommendations
    if predicted_label == 1:  # Phishing detected
        tips = random.sample(phishing_alerts, 3) + context_tips[:3]
    else:  # Legitimate
        tips = random.sample(general_safety, 3)
        if context_tips:
            tips.append("Still, always stay cautious online — some links may look legitimate but aren't.")
    
    # Clean wrapping for CLI or HTML display
    wrapped_tips = [textwrap.fill(tip, width=100) for tip in tips]
    return wrapped_tips
