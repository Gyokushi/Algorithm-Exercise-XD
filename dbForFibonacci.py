
def bottom_up(n):
	fibo = [0]*n
	fibo[0] = 1
	fibo[1] = 1
	for i in range(2,n):
		fibo[i] = fibo[i-1] + fibo[i-2]
	print fibo

def top_down(n):
	fibo = [-1]*n
	def aux(n):
		if n <= 1:
			fibo[n] = 1
			return 1
		if fibo[n] >= 0:
			return fibo[n]
		else:
			fibo[n] = aux(n-1) + aux(n-2)
		return fibo[n]
	aux(n-1)
	print fibo

bottom_up(20) 
top_down(20)
