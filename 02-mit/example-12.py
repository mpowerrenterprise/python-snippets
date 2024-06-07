def exp3(a,b):
	if b == 1:
		return a
	if (b%2)*2==b:
		return exp3(a*a,b/2)
	else:
		return a*exp3(a,b-1)

s = exp3(2,4)
print(s)