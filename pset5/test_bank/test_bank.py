#test the bank file

from bank import value

#test hello
def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0

#test h
def test_h():
    assert value("Hey") == 20
    assert value("Hi") == 20
    assert value("Hiya") == 20

#other greetings
def test_other_greeting():
    assert value("Sup") == 100
    assert value("!Yebo") == 100
    assert value("morning!") == 100

#case-sensitive
def test_case_sensitive():
    assert value("hELLo") == 0
    assert value("hI") == 20
    assert value("123Yaaas") == 100


