from twttr import shorten


def test_lowercase():
    assert shorten("twitter") == "twttr"


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AEIOU") == ""


def test_mixed():
    assert shorten("Faz o L e chora") == "Fz  L  chr"
    assert shorten("Lulululu") == "Llll"


def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("12345") == "12345"


def test_punctuation():
    assert shorten("What's up?") == "Wht's p?"
    assert shorten(".,!?") == ".,!?"
