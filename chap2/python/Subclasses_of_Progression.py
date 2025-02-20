from Progression import Progression

class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0):
        """Iterator producing an arithmetic progression.

        increment   The fixed constant to add to each term (default = 1)
        start       The first term of the progression (default = 0)
        """
        super().__init__(start)
        self._increment = increment

    # Overriding method
    def _advance(self):
        """Update current value by adding fixed increment"""
        self._current += self._increment


class GeometricProgression(Progression):
    def __init__(self, ratio=2, start=1):
        super().__init__(start)
        self._common_ratio = ratio

    def _advance(self):
        self._current *= self._common_ratio


class FibonacciProgression(Progression):
    def __init__(self):
        self._current = 1
        self._prev = 0
    
    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current

if __name__ == "__main__":
    test0 = Progression()
    test1 = ArithmeticProgression(5)
    test2 = GeometricProgression()
    test3 = FibonacciProgression()

    test0.print_progression(10)
    test1.print_progression(10)
    test2.print_progression(10)
    test3.print_progression(10)

    for i in test1:
        print(i)
        if (i > 10): break


