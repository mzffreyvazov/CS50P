from fuel import *
import pytest
from unittest.mock import patch
def main():
    test_convert_percent()
    test_user_input()
    test_print_percent()

def test_user_input():
    input = "1/2"
    expected_output = (1, 2)
    with patch('builtins.input', return_value=input):
        output = user_input()
    assert output == expected_output

def test_print_percent():
    assert print_percent(100) == "F"
    assert print_percent(1) == "E"
    assert print_percent(107) == None
    assert print_percent(40) == "40%"

def test_convert_percent():
    assert convert_percent((1, 2)) == 50.0
    assert convert_percent((1, 5)) == 20.0
    with pytest.raises(ZeroDivisionError):
        convert_percent((1, 0))

if __name__ == "__main__":
    main()