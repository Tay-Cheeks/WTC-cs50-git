#Tests the um.py file

import pytest
from um import count

# test valid use case
def test_valid():
    assert count("hey, um") == 1
    assert count("um") == 1

#test for word boundaries
def test_word_boundaries():
    assert count("yummy") == 0
    assert count("um, um") == 2
    assert count("album") == 0
    assert count("umami") == 0

#test for punctuation
def test_punctuation():
    assert count("hello, um, I'm Thumi!") == 1
    assert count("um?? um um") == 3

#test for case sensitivity
def test_case_sensivtive():
    assert count("UM") == 1
    assert count("uM! Mumu, um") == 2

def no_ums():
    assert count(" ") == 0
    assert count("ums") == 0


