def lst():
	l=list()
	for i in range(1,21):
		a=i**2
		l.append(a)
	print(l)
	print("first 5 values are:",l[0:5])
	print("last 5 values are:",l[-5:])
	t1=tuple(l)
	print(t1)
lst()
	
