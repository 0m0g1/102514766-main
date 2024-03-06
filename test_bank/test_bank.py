from bank import value


def test():
    assert value("Hello") == 0
    assert value("How are you?") == 20
    assert value("What's up?") == 100
