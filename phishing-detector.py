import re

def phishing_detector(url):
    score = 0

    # Long URL
    if len(url) > 75:
        score += 1

    # IP address in URL
    if re.search(r'(\d{1,3}\.){3}\d{1,3}', url):
        score += 2

    # @ symbol
    if '@' in url:
        score += 2

    # Too many dots
    if url.count('.') > 3:
        score += 1

    # Suspicious words
    suspicious_words = [
        'login',
        'verify',
        'update',
        'secure',
        'account',
        'bank'
    ]

    for word in suspicious_words:
        if word in url.lower():
            score += 1

    if score >= 4:
        return "Phishing Website"
    elif score >= 2:
        return "Suspicious Website"
    else:
        return "Legitimate Website"


url = input("Enter URL: ")
result = phishing_detector(url)

print("\nResult:", result)
