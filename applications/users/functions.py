import random
import string

def code_generator(size = 6, chars = string.digits):
	return ''.join(random.choice(chars) for i in range(size))

