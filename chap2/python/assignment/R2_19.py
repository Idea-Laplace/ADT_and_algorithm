"""
When using the ArithmeticProgression class of Section 2.4.2 with an increment
 of 128 and a start of 0, how many calls to next can we make before we reach
 an integer of 2^63 or larger?
"""

"""
For simplicity, we put a_0 = 0 and a_n = 128n.
128 = 2^7,
a_n = 2^7 * n = 2^63
n = 2^56.

So we need at least 2^56 + 1 calls of __next__().
"""