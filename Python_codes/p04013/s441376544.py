n,*x=map(int,open(0).read().split());y=[x[0]-i for i in x];m=n*max(x);d=[[0]*m*2 for _ in[0]*-~n];d[0][0]=1
for i in range(1,n+1):
	for s in range(-m,m):d[i][s]=d[i-1][s]+d[i-1][s-y[i]]
print(d[n][0]-1)