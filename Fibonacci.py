#Akshay Darje#
#M-11#

def fib(x):
	l=[0,1]
	a=0
	b=1
	if x<0:
		print("Enter a positive number ")
	elif x==0:
		print([0])
	elif x==1:
		print([0,1])
	else:
		for i in range (x-2):
			f=a+b
			l.append(f)
			a=b
			b=f
	return l
x=int(input("Enter number of terms : "))
print(fib(x))
