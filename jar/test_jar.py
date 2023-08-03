from jar import Jar

def main():
    test_init()
    test_str()
    test_withdraw()
    test_deposit()

def test_init():
    jar = Jar()
    assert jar.capacity ==  12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(6)
    assert jar.size == 4

if __name__ == "__main__":
    main()
