stock = {
	
	"google":489,
	"apple":329,
	'fb':32,
	'ama':234,
	'f':32,
	'MSFT':543

}

min_price=min(zip(stock.values(),stock.keys()))
print(min_price)