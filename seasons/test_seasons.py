from seasons import convert
import pytest
def main():
    test_convert()

def test_convert():
    assert convert("2005-02-09") == None
    assert convert("2004-08-12") == None



if __name__ == "__main__":
    main()