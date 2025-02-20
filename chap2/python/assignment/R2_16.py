"""
Our Range class, from Section 2.3.5, relies on the formula
max(0, (stop - start + step - 1) // step)
to compute the number of elements in the range. It is not
immediately evident why this formula provides the correct
calculation, even if assuming a positive step size. Justify
this formula, in your own words.
"""

"""
If stop <= start, trivially the length is 0, so we need the
max built-in function instead of the bare expression,
(stop - start + step - 1) // step

When normal case, that is, stop > start,
stop - start yields the number of k in the range of start <= k < stop.
Let n = stop - start, then the above expression is:

(n + (step - 1)) // step, which is equivalent to ceil(n / step)
(Note that n // step is floor(n / step))

Let n // step = q, (n + step - 1) // step = q if and only if n is multiple of step,
q + 1 otherwise.

Since the 'start' is always counted as long as stop is larger than start,
The length is equal to ceil(n / step), not floor(n / step).

Hence, the formula (stop - start + step - 1) // step is appropriate for
computing the length of Range(start, stop, step).
"""