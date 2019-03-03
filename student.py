class Student():
	"""Class Student"""

	def __init__(self, name):
		self.name = name

	# getter of birth
	@property
	def birth(self):
		return self._birth

	# setter of birth
	@birth.setter
	def birth(self, value):
		self._birth = value

	# read-only
	@property
	def age(self):
		return 2019 - self._birth
	
	def __str__(self):
		return 'Student object (name=%s)' % (self.name)

	__repr__ = __str__

student = Student('li')
student.birth = 1992
print(Student('li'))

		