n = int(input())
a = list(map(int, input().split()))
a.sort()
b = []
for i in range(a[0], a[n-1]+1) :
	ans = 0
	for j in range(len(a)) :
		ans = ans + (a[j]-i)**2
	b.append(ans)
print(min(b)) 

