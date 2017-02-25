# A program which returns the power of a given integer 
# with integer and exponent provided.
def power(n,i):
	if (type(n) and type(i)) == int or (type(n) and type(i)) == float:
		if i==0:
			return 1
		else:
			i-=1
			p = n * power(n,i)
			return p
	else:
		raise TypeError("Argument must be integer or float") 