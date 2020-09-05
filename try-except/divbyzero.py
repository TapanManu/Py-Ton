for x in range(9):
	try:
		print(10/x)
	except ZeroDivisionError:
		print("division by zero")
