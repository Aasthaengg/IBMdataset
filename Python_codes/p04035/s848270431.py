N,L=[int(i) for i in input().split()]
A=[int(i) for i in input().split()]

res=-1
for i in range(N-1):
	if A[i]+A[i+1]>=L:
		res=i
		break
if res!=-1:
	print("Possible")
	for i in range(res):
		print(i+1)
	for i in range(N-1,res,-1):
		print(i)
else:
	print("Impossible")
