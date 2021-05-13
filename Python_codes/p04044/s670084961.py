n,l=map(int,input().split())
a=[]
for i in range(0,n):
	a.append(input())
a.sort()
ans=""
for i in a:
	ans+=i
print(ans)