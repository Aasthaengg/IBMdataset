N,M=map(int,input().split())
L=[1]*N
S=[-1]*N
S[0]=1
for i in range(M):
	x,y=map(int,input().split())
	if S[x-1]==1:
		S[y-1]=1
	L[x-1]-=1
	L[y-1]+=1
	if L[x-1]==0:
		S[x-1]=-1
print(S.count(1))