import pytest
from fuel import convert, gauge

""" TEST FOR CONVERT """
def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/10") == 10
    assert convert("1/100") == 1

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("cat/dog") #not integers
    with pytest.raises(ValueError):
        convert("3/1") #x greater than y
    with pytest.raises(ZeroDivisionError):
        convert("9/0")
    with pytest.raises(ValueError):
        convert("-1/2")

""" TEST GAUGE """
def test_gauge_extremes():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(100) == "F"

def test_gauge_mid():
    assert gauge(65) == "65%"
    assert gauge(85) == "85%"
    assert gauge(30) == "30%"
