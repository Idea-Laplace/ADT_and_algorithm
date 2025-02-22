"""
The SequenceIterator calss of Section 2.3.4 provides what
is known as a forward iterator. Implement a class named
ReversedSequenceIterator that serves as reverse iterator
for any Python sequence type. The first call to next should
return the last element of the sequence, the second call to
next should return the second-to-last element, and so forth.
"""

class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the givne sequence."""
        self._seq = sequence    # keep a reference to the underlying data.
        self._k = -1            # will increment to 0 on first call to next.
    
    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1
        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration()
    
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self


class ReverseSequenceIterator:
    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence
        self._k = len(sequence)

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k -= 1
        if self._k >= 0:
            return(self._seq[self._k])
        else:
            raise StopIteration()
    
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self


if __name__ == "__main__":
    sequence = [i for i in range(5)]
    test1 = SequenceIterator(sequence)
    test2 = ReverseSequenceIterator(sequence)

    for val in test1:
        print(val, end=' ')
    print()
    for val in test2:
        print(val, end=" ")
    print()


