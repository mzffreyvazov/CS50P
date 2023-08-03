class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError()
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if n + self._size > self._capacity:
            raise ValueError("Exceeds capacity")
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Not enough cookie")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity can't be a negative number.")
        self._capacity = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("Size can't be a negative number.")
        if value > self._capacity:
            raise ValueError("Size can't exceed capacity.")
        self._size = value

    @property
    def isfull(self):
        return self._size == self._capacity



