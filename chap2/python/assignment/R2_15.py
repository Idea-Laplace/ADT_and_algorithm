"""
R-2.15
The Vector class of Section 2.3.3 provides a constructor that
takes an integer d, and produces a d-dimensional vecotr with
all coordinates equal to 0. Another convenient form for creating
a new vector would be to send the constructor a parameter that
is some iterable type representing a sequence of numbers, and to
creat a vector with dimension equal to the length of that sequence
and coordinates equal to the sequence values. Modify the constructor
so that either of these forms is acceptable; that is, if a single
integer is set, it produces a vector of that dimension with all 0s,
but if a sequence of numbers is provided, it produces a vector with
coordinates based on that sequence.
"""


class Vector:
    """Represent a vector in a multidimensional space."""
    
    def __init__(self, *d):
        if len(d) == 1:
            self._coords = [0] * d[0]
        else:
            self._coords = list(d)

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of 2 vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree.')

        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree.')

        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    
    def __rsub__(self, other):
        return -self + other
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] * other
        elif isinstance(other, Vector):
            if (len(self) != len(other)):
                raise ValueError("dimensions must agree.")
            result = 0
            for i in range(len(self)):
                result += self[i] * other[i]
        else:
            raise TypeError("Operands must be either numeric scalar or vector.")
        return result
    
    def __rmul__(self, other):
        return self * other
        
    
    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other
    
    def __str__(self):
        """Produce string representation of vector."""
        # Insert '<', '>' instead of '[', ']' as the delimiter for 'Vector'.
        return '<' + str(self._coords)[1:-1] + '>'


if __name__ == '__main__':
    test1 = Vector(5)
    test2 = Vector(5)
    test3 = Vector(1, 2, 3)

    for i in range(5):
        test1[i] = i
        test2[i] = 2 * i
    print(test1)
    print(test2)
    print(test3)
    print()
    print(test1 + test2)
    print(test2 - test1)
    print(-test1)
    print(test1 + [5, 3, 10, -2, 1])
    print([5, 3, 10, -2, 1] + test1)
    print()
    print(3 * test1)
    print(test1 * 3)
    print(test1 * test2)