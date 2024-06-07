def numBin(num):
	if num >=1:
		print(round(num%2))
		numBin(num/2)

#numBin(8);


def numBin2(num):
	while num>=1:
		print(round(num%2))
		num=num/2

numBin2(10)
