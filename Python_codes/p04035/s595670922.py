n,l=map(int,input().split())
a=list(map(int,input().split()))
f=-1
for i in range(n-1):
	if a[i]+a[i+1]>=l:
		f=i
		break
if f==-1:
	print("Impossible")
	exit()
print("Possible")
for i in range(n-1):
	if i<f:
		print(i+1)
	elif i>f:
		print(n-i+f)
print(f+1)