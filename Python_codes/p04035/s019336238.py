n,l = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
s,x,y,ans,num,z = sum(a),0,n-1,[],0,0
for i in range(n-1):
	num2 = a[i]+a[i+1]
	if num<num2: num,z = num2,i+1
if num>=l:
	print("Possible")
	for i in range(1,z): print(i)
	for i in range(n-1,z-1,-1): print(i)
else: print("Impossible")