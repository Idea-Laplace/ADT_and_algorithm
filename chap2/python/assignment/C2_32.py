"""
C-2.32
Write a Python class that extends the Progression class so that
each value in the progression is the square root of the previous value.
Your constructor should accept an optional parameter specifying the
start value, using 65536 as a default.
"""

import sys
sys.path.append("..")
from Progression import Progression

class SquareRootProgression(Progression):
    def __init__(self, start=65536):
        super().__init__(start)

    def _advance(self):
        if self._current < 0:
            raise ValueError("Square root for negative value.")
        self._current = self._current ** 0.5

if __name__ == '__main__':
    test = SquareRootProgression()

    test.print_progression(10)

