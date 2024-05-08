import re

def test_phone_regex():
    assert phone_number("(12)1231231234") == "(12)1231231234"
    assert phone_number("12123)1231234") is None
    assert phone_number("12(1231231234") == "1231231234"

if __name__ == "__main__":
    test_phone_regex()