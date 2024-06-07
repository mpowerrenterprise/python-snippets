stock={
	
	'google':520.55,
	'fb':79.16,
	'yahoo':30.10,
	'amazon':306.23,
	'aapl':99.23
}

print("The min value is ",min(zip(stock.values(),stock.keys())))
print("The max value is ",max(zip(stock.values(),stock.keys())))
print(sorted(zip(stock.values(),stock.keys())))

#stock.values() is the number values.
#stock.keys() are the keys.
#At first we zip them together.
#Then we use min and max function.
