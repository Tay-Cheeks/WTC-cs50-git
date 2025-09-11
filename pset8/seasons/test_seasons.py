import pytest
from datetime import date
from seasons import mins_between, num_english, format_words, parse_DOB

""" TEST PARSE_DOB """
def test_parse_DOB_valid():
    assert parse_DOB("2000-01-01") == date(2000, 1, 1) #parse_DOB returns a date object

def test_parse_DOB_isleap():
    assert parse_DOB("2020-02-29") == date(2020, 2, 29)

def test_parse_DOB_invalid():
    with pytest.raises(ValueError):
        parse_DOB("12-12-1998")

def test_parse_DOB_nonsense():
    with pytest.raises(ValueError):
        parse_DOB("banana")

""" TEST MINS-BETWEEN """
def test_mins_between_same_day():
    start_date = date(2000, 1, 1)
    end_date = date(2000, 1, 1)
    assert mins_between(start_date, end_date) == 0

def test_mins_between_multiple_days():
    start_date = date(2000, 1, 1)
    end_date = date(2000, 1, 3)
    assert mins_between(start_date, end_date) == 2880

""" TEST NUM_ENGLISH """
def test_num_english_basic():
    assert num_english(1) == "One"

def test_num_english_large():
    assert num_english(1440) == "One thousand four hundred forty"

def test_num_english_zero():
    assert num_english(0) == "Zero"

""" TEST FORMAT_WORDS """
def test_format_words_basic():
    assert format_words("six hundred") == "six hundred minutes"

def test_format_words_large():
    assert format_words("one thousand four hundred forty") == "one thousand four hundred forty minutes"

def test_format_words_empty():
    assert format_words("") == " minutes"
