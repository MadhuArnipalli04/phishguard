import re

def extract_features(url):
    features = []
    # URL Length
    features.append(len(url))
    # Number of dots
    features.append(url.count('.'))
    # Number of hyphens
    features.append(url.count('-'))
    # HTTPS present
    features.append(1 if "https" in url else 0)
    # Number of digits
    features.append(sum(c.isdigit() for c in url))
    # Special characters
    features.append(url.count('@') + url.count('?') + url.count('='))
    return features