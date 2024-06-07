def squrt(x):
	ans=0
	if x>=0:
		while ans*ans < x:ans = ans +1
		if ans*ans!=x:
			print(x)
			return None
		else: return ans
	else:
		print(x,'Is a negative number')
		return None


x = squrt(16)

print(x)


