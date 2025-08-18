#test cases for plates file

from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ABC4567") == False

def test_starts_with_letters():
    assert is_valid("AB1234") == True
    assert is_valid("A123") == False
    assert is_valid("1234") == False

def test_numberRule():
    assert is_valid("ad456") == True
    assert is_valid("as34r") == False
    assert is_valid("we05") == False
    assert is_valid("ABDC") == True #no numbers so still valid as the number conditional isnt triggered

def test_char():
    assert is_valid("OUTLAW") == True
    assert is_valid("CS50!") == False
    assert is_valid("DUDEWHERESMYCAR") == False



