from numb3rs import validate

def main():
    test_validate()

def test_validate():
    assert validate("455.99.07.55") == False
    assert validate("255.99.07.55") == True
    assert validate("5.99.444.335") == False
    assert validate("105.99.87.55") == True
    assert validate("cat") == False

if __name__ == "__main__":
    main()