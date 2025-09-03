#Tests the numb3rs.py file
#sys for asserting and exit

from numb3rs import validate

def test_valid_ip():
    #Typical IPs
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("189.12.132.67") == True
    assert validate("127.0.0.1") == True

def test_invalid_ip():
    #Numbers out of range
    assert validate("00.0.1.12") == False
    assert validate("512.512.512.512") == False
    assert validate("267.230.123.243") == False
    assert validate("1.2.3.1000") == False

    #Wrong inputs
    assert validate("cat") == False
    assert validate("00.0.1.12") == False #leading zeros
    assert validate("123.32.45") == False #too few parts
    assert validate("234.67.40.12.1") == False #too long
    assert validate("...") == False #only dots
    assert validate(" ") == False #not entry
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False #too long, colon used and out of range

    #Another assert format: assert validate("cat") is False
