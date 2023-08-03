from um import count
import pytest

def main():
    test_count()

def test_count():
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks") == 1
    assert count("Um, thanks, I should, um, do something about this, um..., I guess") == 3
    assert count("yummy") == 0
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2

if __name__ == "__main__":
    main()