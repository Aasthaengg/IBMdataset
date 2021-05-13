N,A=map(int,input().split())
l=list(map(int,input().split()))
d={}
def func(n,s,i):
	if n<0:
		return
	if (n,s,i) in d:
		return
	if n==0:
		if s==0:
			d[(n,s,i)]=1
		else:
			d[(n,s,i)]=0
		return
	if i>=N:
		if s==0 and n==0:
			d[(n,s,i)]=1
		else:
			d[(n,s,i)]=0

		return
	else:
		func(n-1,s-l[i],i+1)
		func(n,s,i+1)
		d[(n,s,i)]=d[(n-1,s-l[i],i+1)]+d[(n,s,i+1)]
ans=0
for j in range(1,N+1):
	func(j,j*A,0)
	ans+=d[(j,j*A,0)]
print(ans)