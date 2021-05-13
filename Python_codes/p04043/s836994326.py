a=[0]*11
x=list(map(int,input().split()))
for i in x:
	a[i] += 1
if(a[5]==2 and a[7]==1):
	print("YES")
else:
	print("NO")