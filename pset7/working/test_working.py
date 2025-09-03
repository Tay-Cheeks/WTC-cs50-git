# test the working.oy file
import pytest
from working import convert

#
def test_basic_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_minutes():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 11:05 PM") == "22:30 to 23:05"

def test_midnight_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:10 PM to 12:25 AM") == "12:10 to 00:25"

def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 12 PM")

