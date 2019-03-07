# global variable
x = 'global'

def fn():
	print('inside: ', x)

fn()
print('outside: ', x)


# modify global variable

y = 'global'

def fn():
	# UnboundLocalError: local variable 'y' referenced before assignment
	global y
	y = y*2
	print('modify global: ', y)
fn()