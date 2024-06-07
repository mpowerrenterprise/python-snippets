def exp2(a,b):
	if a == 1:
		return a
	else:
		return a*exp2(a,b-1)
		