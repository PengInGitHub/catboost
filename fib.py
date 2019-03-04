class Fib():
	""" Fib is an example to showcase how a class could be
	 iterated in for ... in, same as list and tuple """

	# init two counters
	def __init__(self):
		self.first, self.second = 0, 1

	
	# iter returns the thing to iterate
	# for ... in will continuously call __next__() to get the next value of iteration
	# untill the condition of stopIteration is met

	# rescursion
	# the thing to iterate is the object itself
	# so return the object
	def __iter__(self):
		return self

	def __next__(self):
		self.first, self.second = self.second, self.first + self.second
		# condition to exit loop
		if self.first > 100000:
			raise StopIteration();
		return self.first

	def __getitem__(self,n):
		first, second = 1, 1
		for _ in range(n):
			first, second = second, first + second
		return first



# TypeError: 'Fib' object does not support indexing
if __name__ == '__main__':
	print(Fib()[6])


