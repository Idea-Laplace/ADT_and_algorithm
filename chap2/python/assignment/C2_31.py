"""
C-2.31
Write a Python class that extends the Progression class so that
each value in the progression is the absolute value of the difference
between the previous two values. You should include a constructor that
accepts a pair of numbers as the first two values, using 2 and 200 as
the default.
"""

import sys
sys.path.append("..")
from Progression import Progression


class AbsProgression(Progression):
    def __init__(self, first=2, second=200):
        super().__init__(first)
        self._prev = second
        self._flag = True
    
    def _advance(self):
        if self._flag == True:
            self._current, self._prev = self._prev, self._current
            self._flag = False
        else:
            self._current, self._prev = abs(self._current - self._prev), self._current
    

if __name__ == '__main__':
    test = AbsProgression()

    test.print_progression(10)

