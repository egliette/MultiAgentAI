import re

def phone_regex(text):
    pattern = r"\b\d{3}[-\.\s]?\d{3}[-\.\s]?\d{4}\b"
    matches = re.findall(pattern, text)
    return matches

def test_phone_regex():
    assert phone_regex("(12)1231231234") == "(12)1231231234"
    assert phone_regex("12123)1231234") is None
    assert phone_number("12(1231231234") == "1231231234"

if __name__ == "__main__":
    test_phone_regex()