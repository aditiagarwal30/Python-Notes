def gen_fibon(n):

	a=0
	b=1
	for i in range(n):
		yield a
		a,b=b,a+b


y=int(input('Enter a number'))
for number in gen_fibon(y):
    print(number)


