def factorial(n):
	if n == 0:
		return 1
	elif n <= 2:
		return n
	else:
		return n * factorial(n - 1)

print factorial(int(raw_input('factorial? ')))