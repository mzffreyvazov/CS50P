from working import convert
import pytest

def main():
    test_convert()

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 17 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9AM to 8PM")

if __name__ == "__main__":
    main()