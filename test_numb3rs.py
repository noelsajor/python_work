from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format():
    assert validate("4.3.2.1") == True
    assert validate("3.2.1") == False
    assert validate("2.1") == False
    assert validate("1") == False

def test_range():
    assert validate("255.255.255.255") == True
    assert validate("512.1.1.1") == False
    assert validate("1.512.1.1") == False
    assert validate("1.1.512.1") == False
    assert validate("1.1.1.512") == False
