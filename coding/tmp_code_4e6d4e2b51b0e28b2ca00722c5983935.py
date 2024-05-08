import re

def phone_regex(text):
    pattern = r"\b\d{3}[-\.\s]?\d{3}[-\.\s]?\d{4}\b"
    matches = re.findall(pattern, text)
    return matches