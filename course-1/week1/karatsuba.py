def main():
	x = int(input('enter first number to multiply: '))
	y = int(input('                        second: '))
	ans1 = x * y
	ans2 = karatsuba(x, y)
	print('with python multiplication:    {}'.format(ans1))
	print('with karatsuba multiplication: {}'.format(ans2))
	if ans1 == ans2:
		print("It works :)")
	else:
		print("It doesn't work :(")

def karatsuba(x, y):
	"""
	karatsuba(x, y):
	Function that uses karatsuba multiplication(divide and conquer) to return x times y
	"""
	if x < 10 and y < 10:
		return x * y
	else:
		n = max(len(str(x)), len(str(y))) // 2
		a = x // 10**n
		b = x %  10**n
		c = y // 10**n
		d = y %  10**n
		ac = karatsuba(a, c)
		bd = karatsuba(b, d)
		ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
		return ac * (10**(2*n)) + ad_plus_bc * (10**n) + bd # the 2*n makes sure correct no. of zeros are added to ac, even if max(lenx,leny) is odd

main()