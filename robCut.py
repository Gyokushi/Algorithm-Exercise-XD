source = [1,5,8,9,10,17,17,20,24,30]
def cut_Bottom_Up(source):
	n = len(source)+1
	memo = [0]*(n)
	points = [-1]*(n)
	points[0] = 0
	times = [0]*(n)
	for i in range(1,n):
		for j in range(i):
			q = source[j] + memo[i-1-j]
			if memo[i] > q: continue
			memo[i] = q
			points[i] = i-j-1
		if points[i]!=0 and points[i]!=i-1:
			times[i] = times[points[i]] + 1
		else:
			times[i] = times[points[i]]
	print 'memo:'+' '*3 + str(memo)
	print 'range:  '+ str(range(11))
	print 'points: ' + str(points)
	print 'times: '+ ' ' + str(times)


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


def cut_Memoized_Top_Down(source):
	n = len(source)
	memo = [-1]*(n+1)
	points = [-1]*(n+1)
	memo[0] = 0
	points[0] = 0
	def aux(source,n):
		if n == 0 : return memo[0] #length = 0
		if memo[n] >= 0: return memo[n] # index
		for i in range(1,n+1):# i is length? index ? 
			q = aux(source,n-i) + source[i-1]
			if memo[n] > q:
				continue
			memo[n] = q
			points[n] = i
		return memo[n]
	aux(source,n)
	print memo
	print points

cut_Bottom_Up(source)
cut_Memoized_Top_Down(source)
