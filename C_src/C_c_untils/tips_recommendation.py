def recommend_practices(is_phishing: bool) -> list:
    """Return safety or awareness tips based on detection."""
    if is_phishing:
        return [
            "❌ Do not click on suspicious links.",
            "⚠️ Verify the sender or domain manually.",
            "🔒 Avoid sharing personal information online.",
            "📧 Check for spelling or grammar mistakes in emails."
        ]
    else:
        return [
            "✅ Keep your browser and antivirus up to date.",
            "🔐 Always prefer HTTPS links.",
            "💡 Bookmark trusted websites instead of typing them."
        ]
