import pytest
from jar import Jar


def test_init():
    jar = Jar()


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.deposit(1000)


def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(1)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(999)