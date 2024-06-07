x = int(input('Enter a perfect square : '))
guess = 0 # Our guess answer
while guess**2 < x:
    guess += 1 # Shorthand for guess = guess + 1
print('Square root of ' + str(x) + ' is ' + str(guess))