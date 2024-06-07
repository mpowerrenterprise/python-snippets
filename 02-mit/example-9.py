def expl(a,b):
	ans=1
	while(b>0):
		ans*=a
		b-=1
	return ans

print(expl(2,3))