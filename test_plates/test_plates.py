from plates import is_valid

def main():
    test_min_and_max()

def test_min_and_max():
    assert is_valid("aa") == True
    assert is_valid("abcdef") == True
    assert is_valid("a") == False
    assert is_valid("abcdefgh") == False

if __name__ == "__main__":
    main()