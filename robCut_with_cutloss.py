source = [1,5,8,9,10,17,17,20,24,30]

def cut_Bottom_Up(source,cost = 0):
	n = len(source)
	points = [-1]*(n+1)
	points[0] = 0
	times = [0]*(n+1)
	prices = [0]*(n+1)
	for i in range(1,n+1):
		for j in range(i):
			q = source[j] + prices[i-1-j] - times[points[i]] * cost if j == i-1 else source[j] + prices[i-1-j] - (times[points[i]] + 1) * cost
			if prices[i] > q: 
				continue
			prices[i] = q
			points[i] = j + 1
		if points[i] != i :
			times[i] = times[points[i]] + 1
		else:
			times[i] = times[points[i]]


	print 'range:  '+ str(range(11))
	print 'points: ' + str(points)
	print 'times:  ' + str(times)
	print 'prices: ' + str(prices)


# def cut_Memoized_Top_Down(source):
# 	n = len(source)
# 	memo = [-1]*n
# 	points = [-1]*n
# 	def aux(source,n):
# 		if n == 0: return 0 #length = 0
# 		if memo[n-1] >= 0: return memo[n-1] # index
# 		for i in range(n):# i is length? index ? 
# 			memo[n-1] = max(memo[n-1], aux(source,n-i-1) + source[i])
# 		return memo[n-1]
# 	aux(source,n)
# 	print memo


def cut_Memoized_Top_Down(source,cost = 0):
	n = len(source)
	memo = [-1]*(n+1)
	points = [-1]*(n+1)
	times = [0]*(n+1)
	memo[0] = 0
	points[0] = 0
	def aux(source,n):
		if n == 0 : return memo[0] #length = 0
		if memo[n] >= 0: return memo[n] # index
		for i in range(1,n+1):# i is length? index ? 
			q = aux(source,n-i) + source[i-1] - times[points[i]] * cost if i==n else aux(source,n-i) + source[i-1] - (times[points[i]] + 1) * cost
			if memo[n] > q:
				continue
			memo[n] = q
			points[n] = i
		if points[n]!= n:
			times[n] = times[points[n]] + 1
		else:
			times[n] = times[points[n]]

		return memo[n]
	aux(source,n)

	print 'range:  '+ str(range(11))
	print 'memo:   ' + str(memo)
	print 'points: ' + str(points)
	print 'times:  ' + str(times)


print 'bottom-up:----------------------------------'
cut_Bottom_Up(source,0.8)
print 'top-down:================================='
cut_Memoized_Top_Down(source,0.8)
