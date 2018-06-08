def operation():
	while(True):
		a=int(input("Enter the first number:-"))
		b=int(input("Enter the second number:-"))
		c=input("Enter the operation to be perform:-")

		if (c=='+' or c=='add'):
			d=a+b
			print(d)
		elif (c=='-' or c=='sub'):
			d=a-b
			print(d)
		elif (c=='*' or c=='multi'):
			d=a*b
			print(d)
		elif (c=='/' or c=='div'):
			d=a/b
			print(d)
		else:
			print("Try again")
operation()
