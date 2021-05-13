temp=input().split()
N=int(temp[0])
L=int(temp[1])
a=[int(i) for i in input().split()]
flag=False
ans=[]

for i in range(N-1):
	if a[i]+a[i+1]>=L:
		print("Possible")
		flag=True
		ans.append(i)
		break
else:
	print("Impossible")

if flag==True:
	while ans[-1]>0:
		ans.append(ans[-1]-1)
	if ans[0]<N-1:
		ans.append(ans[0]+1)
		while ans[-1]<N-2:
			ans.append(ans[-1]+1)
	for i in range(N-2,-1,-1):
		print(ans[i]+1)