def pisano_l(m):
	a=0
	b=1
	c= a+b
	for i in range(0,m*m):
		c= (a+b)%m
		a=b
		b=c
		if( a == 0 and b == 1):
			return (i+1)

def fibonacci(n):
	fib = [None]*(n+2)
	fib[0] = 0
	fib[1] = 1

	for i in range(2,n+1):
		fib[i] = fib[i-1] + fib[i-2]
	return fib[n]
	
n,m = input().split()
n = int(n)
m = int(m)
p = pisano_l(m)
x = n%p


print(fibonacci(x)%m)					