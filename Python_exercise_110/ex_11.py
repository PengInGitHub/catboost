class Bike:

	def __init__(self, wheel, color):
		self.wheel = wheel
		self.color = color

	def move(self):
		print('the bike is running')

my_bike = Bike(2, 'blue')
print()
my_bike.move()
