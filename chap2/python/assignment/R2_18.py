"""
R-2.18
Give a short fragment fo Python code that uses the progression classes
form Section 2.4.2 to find the 8th value of a Fibonacci progression that
starts with 2 and 2 as its first two values.
"""

import sys
sys.path.append('../')
from Progression import Progression

class FibonacciProgression(Progression):
    def __init__(self, lead: int=1, lag: int=0):
        super().__init__(lead)
        self._prev = lag

    def _advance(self):
        self._prev, self._current = self._current, self._current + self._prev

if __name__ == '__main__':
    test_fibo = FibonacciProgression(2)
    test_fibo.print_progression(8)