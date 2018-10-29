def fact(x):
	f=1
	if x<0:
		print("Enter a positive number")
	elif x==0:
		print("Factorial : 1")
	elif x==1:
		print("Factorial : 1")
	else:
		while x>1:
			f=f*x
			x=x-1
	return f
x=int(input("Enter a number : "))
print(fact(x))
