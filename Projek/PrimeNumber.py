class prime:
    def __init__(self, value):
        self._value = value

    def getter(self):
        return self._value

    def setter(self, x):
        self._value = x

    def factors(self):
        if self._value <= 0:
            return False
        self._factors = []
        for i in range(1, self._value + 1):
            if self._value % i == 0:
                self._factors.append(i)
        return self._factors

    def state(self):
        if len(self._factors) <= 2:
            return "Prime Number"
        return "Not a Prime Number"


Num = prime(13)
Num.setter(37)
print(Num.factors())
print(Num.state())
