#test file for twttr function

from twttr import shorten

#test lowercase use for our shorten function
def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("Hello") == "Hll"

#test uppercase use
def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"

def test_mixedcase():
    assert shorten("TwITter") == "TwTtr"
    assert shorten("ApPLe") == "pPL"

def test_numbers_symbols():
    assert shorten("123") == "123"
    assert shorten("@pple!") == "@ppl!"
