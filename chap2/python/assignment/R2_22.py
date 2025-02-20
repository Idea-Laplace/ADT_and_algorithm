"""
R-2.22
The collections.Sequence abstract base class does not provide support for
comparing two sequences to each other. Modify our Sequence class from Code
Fragment 2.14 to include a definition for the __eq__ method, so that expression
seq1 == seq2 will return True precisely when the two sequences are element by
element equivalent.
"""

from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        """"""

    @abstractmethod
    def __getitem__(self, i):
        """"""

    def __eq__(self, other):
        if not isinstance(other, Sequence):
            raise TypeError("Operand type must agree.")
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True
    
    def __contains__(self, val):
        for i in range(len(self)):
            if self[i] == val:
                return True
        return False
    
    def index(self, val):
        for i in range(len(self)):
            if self[i] == val:
                return i
        raise ValueError("value not in sequence.")
    
    def count(self, val):
        k = 0
        for i in range(len(self)):
            if self[i] == val:
                k += 1
        return k
