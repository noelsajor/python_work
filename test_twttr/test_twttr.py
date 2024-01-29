from twttr import shorten

def test_twttr():
    assert shorten("cafetera") == "cftr"
    assert shorten("laptop") == "lptp"