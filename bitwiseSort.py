def bsort(arr,l,r,x):
	if x==0 or l>=r:
		return 
	i = l-1
	for j in range(l,r+1,1):
		if (arr[j] & x) == 0:
			i += 1
			arr[j],arr[i] = arr[i],arr[j]
	bsort(arr,l,i,x>>1)
	bsort(arr,i+1,r,x>>1)
def sort(arr,n):
	bsort(arr,0,n-1,1<<32)
