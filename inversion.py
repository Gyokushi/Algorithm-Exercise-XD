#calculte the number of inversions in an array, use mergeSort
import random

def merge(items, p, q, r):
    inversion = 0;
    L = items[p:q+1]
    R = items[q+1:r+1]
    i = j = 0
    k = p
    while i < len(L) and j < len(R):
        if(L[i] < R[j]):
            items[k] = L[i]
            i += 1
        else:
            items[k] = R[j]
            inversion += len(L)-i
            j += 1
        k += 1
    if(j == len(R)):
        items[k:r+1] = L[i:]
    return inversion



def mergesort(items, p, r):
    inversion = 0
    if(p < r):
        q = (p+r)//2
        inversion += mergesort(items, p, q)
        inversion += mergesort(items, q+1, r)
        inversion += merge(items, p, q, r)
    return inversion


items = [random.randrange(20) for x in range(0,6)]
print(items)
inversion = mergesort(items, 0, len(items)-1)
print (inversion)
# def binarySearch(item,x):
#     low = 0;
#     high = len(item)-i
#     while low<=high:
#         mid = (low+high)//2
#         if(item[mid] == x):
#             return mid
#         elif (item[mid] < x):
#             low = mid+1
#         else:
#             high = mid-1
#     return None

# print (binarySearch(items,1))

