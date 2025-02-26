class Range:
	"""A class that mimics the built-in range class."""

	def __init__(self, start, stop=None, step=1):
		"""Initialize a Range instance.

		Semantics is similar to built-in range class.
		"""

		if step == 0:
			raise ValueError("step cannot be 0.")

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
		
