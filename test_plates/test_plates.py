from plates import is_valid

def main():
    test_min_and_max()
    test_two_letters_at_start()
    test_number_in_the_middle()
    test_number_zero
    test_punctuation
    

def test_min_and_max():
    assert is_valid("aa") == True
    assert is_valid("abcdef") == True
    assert is_valid("a") == False
    assert is_valid("abcdefgh") == False

def test_two_letters_at_start():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("12") == False

def test_number_in_the_middle():
    assert is_valid("ABC123") == True
    assert is_valid("ABC12D") == False

def test_number_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid("PI 14") == False

if __name__ == "__main__":
    main()