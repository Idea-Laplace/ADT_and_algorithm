"""
In section 2.3.5, we note that our version of Range calss has
implicit support for iteration, due to its explicit support of
both __len__ and __getitem__. The class also receives implicit
support of Boolean test, "k in r" for Range r. This test is 
evaluated based on a forward iteration through the range, as
evidenced by the relative quickness of the test2 in Range(10000000)
versus 9999999 in Range(10000000). Provide a more efficient implementation
of the __contains__ method to determine whether a particular value lies
within a given range. The running time of your method should be
independent of the length of the range.
"""
from time import time

class Range:
    """A class that mimics the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("step cannot be 0.")

        # If stop is omitted(None), the first argument become stop.
        if stop is None:
            start, stop = 0, start
 
        # ceil((stop - start) / step)
        self._length = max(0, (stop - start + step - 1) // step)
        # need knowledge of strat and step(but not stop) to support __getitem__ 
        self._start = start
        self._step = step
    
    def __len__(self):
        return self._length
    
    def __getitem__(self, k):
        if k < 0:
            # attempt to convert negative index
            k += len(self)
        if not 0 <= k < self._length:
            raise IndexError("index out of range.")

        return self._start + k * self._step

    def __contains__(self, k):
        """
        Even though the cotains method is implicitly defined by
        __len__ and __getitem__, the process is evaluated based
        on a forward iteration, potentially harms the performance
        according to its input value.
        """
        if 0 <= k - self._start < len(self) * self._step:
            if (k - self._start) % self._step == 0:
                return True
        return False

if __name__ == "__main__":
    case1 = 0
    case2 = 0
    for i in range(10):
        start_t = time()
        i = 2 in Range(0, 10000000, 3)
        print(i)
        end_t = time()
        case1 += (end_t - start_t)
        print(10000000 * (end_t - start_t))

        start_t = time()
        i = 9999999 in Range(0, 10000000, 3)
        end_t = time()
        case2 += end_t - start_t
        print(i)
        print(10000000 * (end_t - start_t))
        print()
    print(case2 / case1)
        
