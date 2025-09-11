from jar import Jar
import pytest

def test_init():
    #valid_capacity
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    #default_capacity():
    jar = Jar() #if theres no input for capacity
    assert jar.capacity == 12
    assert jar.size == 0

    #invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-5) #negative int
    with pytest.raises(ValueError):
        Jar("Ten") #not an integer
    with pytest.raises(ValueError):
        Jar(3.5) #float

def test_str():
    jar = Jar(5)

    assert str(jar) == "" #jar starts with nothing before we deposit
    assert jar.size == 0
    assert jar.capacity == 5

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(5)

    jar.deposit(2)
    assert jar.size == 2

    jar.deposit(3)
    assert jar.size == 5

    jar.deposit(0)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(1) #exceeds capacity (takes Jar to 6 with a 5 capacity)
    with pytest.raises(ValueError):
        jar.deposit(-1) #negative deposit

def test_withdraw():
    jar = Jar(5) #capacity of Jar
    jar.deposit(4) #intial deposit

    jar.withdraw(2) #4-2
    assert jar.size == 2

    jar.withdraw(0)
    assert jar.size == 2

    jar.withdraw(2)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(3) #exceeds jar size, theres nothing left
    with pytest.raises(ValueError):
        jar.withdraw(-1) #can't have a -ve withdrawal



