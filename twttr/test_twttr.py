from twttr import shorten

def main():
    test_upper_lower_cases()
    test_number()
    test_punctuation()

def test_upper_lower_cases():
    assert "a" not in shorten("alan")
    assert "e" not in shorten("eeire")
    assert "MY NM S" == shorten("MY NAME IS")
    assert shorten("SomeoNe is MIsSinG") == "SmN s MsSnG"

def test_number():
    assert shorten("456") == "456"
    assert shorten("10 20") == "10 20"

def test_punctuation():
    assert shorten("alan!") == "ln!"
    assert shorten("do you?") == "d y?"
    assert shorten("my name is, well...") == "my nm s, wll..."


if __name__ == "__main__":
    main()