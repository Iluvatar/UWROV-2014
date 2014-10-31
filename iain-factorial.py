def factorial(n):
	if n == 0:
		return 1;
	else:
		return n * factorial(n - 1)
		
def printFactorial(n):
	print n, "! = ", factorial(n)

def upToFactorial(n):
	for i in range(1, n):
		printFactorial(i)

def factorialWhile(n):
	initial = n
	total = n
	while n > 1:
		total *= (n - 1)
		n -= 1
	print initial, "! = ", total
		
		
		
upToFactorial(8)
print
printFactorial(10)
print
factorialWhile(50000)