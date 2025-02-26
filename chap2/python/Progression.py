class Progression:
    """Iteration producing a generic progression.
    
    Default iterator produces the whole numbers 0, 1, 2,...
    """
    def __init__(self, start=0):
        """Intialize current to the first value of the progression."""
        self._current = start
    def _advance(self):
        """Update self._current to a new value.
        
        This should be overrides by a subclass to customize progression.
        
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    
    def __iter__(self):
        return self
    
    def print_progression(self, n):
        """Print next n values of the progression."""
        print(" ".join(str(next(self)) for j in range(n)))

