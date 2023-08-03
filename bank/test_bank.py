from bank import *

def main():
    test_firstcase()

def test_firstcase():
    assert value("hello") == 0
    assert value("hi, how are you") == 20
    assert value("my name is bla") == 100
    assert value("Hello") == 0