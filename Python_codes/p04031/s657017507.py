n = int(input())
arr =list(map(int , input().split()))
ans = 10001*10001
for i in range(-100 ,101):
	tot =0
	for j in arr:
		tot = tot+(i-j)*(i-j)
	ans = min(ans, tot)
print(ans)