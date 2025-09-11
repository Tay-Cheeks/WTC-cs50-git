"""
A simple Jar class that simulates a cookie jar.

Methods:
- __init__(capacity): initialize jar with given capacity (default 12).
- __str__(): return 🍪 * size.
- deposit(n): add n cookies, raise ValueError if exceeds capacity.
- withdraw(n): remove n cookies, raise ValueError if not enough cookies.
Properties:
- capacity: maximum number of cookies jar can hold.
- size: current number of cookies in the jar.
"""

class Jar:
    def __init__(self, capacity=12): #called when a new instance (object) of a class is created; default capacity=12
        #if its false(not) capacity is an integer or a +ve integer
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer!") #raised so code can halt and not create a corrupt object
        #otherwise
        self._capacity = capacity #intitialsing max capacity in the jar
        self._size = 0 #initial cookie count in the jar(empty jar)

    def __str__(self): #must return a string of cookie emojis to print
        return f"🍪" * self._size

    def deposit(self, n): #in self, n of cookies put inside
        if not isinstance(n, int) or n < 0:
            raise ValueError("Cannot deposit negative cookie!")

        if self._size + n > self._capacity:
            raise ValueError("Cookies exceed jar capacity!")
        #otherwise deposit into jar
        self._size += n

    def withdraw(self, n): #remove n cookies from jar
        if not isinstance(n, int) or n < 0:
            raise ValueError("Cannot withdraw a negative cookie!")

        if n > self._size:
            raise ValueError("There's not enough cookies in jar!")
        #otherwise, withdraw n cookies
        self._size -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

