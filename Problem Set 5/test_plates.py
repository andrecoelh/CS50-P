from plates import is_valid


def test_beginning():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("1A") == False
    assert is_valid("A1") == False


def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_number_placement():
    assert is_valid("AAA222") == True
    assert is_valid("AA22AA") == False


def test_zero_placement():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True


def test_alphanumeric():
    assert is_valid("PI3.14") == False
    assert is_valid("CS50!") == False
