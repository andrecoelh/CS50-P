from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("Hello, Andre") == 0


def test_h():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("HOW ARE YOU?") == 20


def test_other():
    assert value("What's up?") == 100
    assert value("Cat") == 100
    assert value("Good morning") == 100