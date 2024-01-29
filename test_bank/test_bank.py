from bank import value

def main():
    test_for_zero()
    test_for_20()
    test_for_100()

def test_for_zero():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_for_20():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("hey") == 20
    assert value("Hey") == 20
    assert value("howdy") == 20
    assert value("Howdy") == 20

def test_for_100():
    assert value("what's up") == 100
    assert value("What's up") == 100

if __name__ == "__main__":
    main()