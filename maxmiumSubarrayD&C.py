# use divide and conquer strategy to resolve maxmium subarray problem

import random
def divide_And_conquer(m,n,arr):
	if m==n:
		return arr[m]
	mid = (m+n)//2
	leftMax = divide_And_conquer(m,mid,arr)
	rightMax = divide_And_conquer(mid+1,n,arr)
	crossMax = cross_dnc(m,mid,n,arr)

	if leftMax<=crossMax and rightMax<=crossMax:
		return crossMax
	elif crossMax<=leftMax and rightMax<=leftMax:
		return leftMax
	return rightMax

def cross_dnc(m,mid,n,arr):
	sum = 0
	leftMax = 0
	rightMax = 0
	for i in reversed(range(m,mid+1)):
		sum = sum + arr[i]
		if(sum > leftMax):
			leftMax = sum
	sum = 0
	for i in range(mid+1,n+1):
		sum = sum+arr[i]
		if (sum >rightMax):
			rightMax = sum
	return rightMax+leftMax

array = [random.randrange(-5,10) for x in range(10)]
print(array)
print(divide_And_conquer(0,len(array)-1,array))
