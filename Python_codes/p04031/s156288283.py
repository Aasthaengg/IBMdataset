n = int(input())
arr = list(map(int,input().split()))
add = sum(arr)
if add>0:
	x = int(add/n + 0.5)
else:
	x = int(add/n - 0.5)

ans = 0
for i in range(len(arr)):
	ans += ((x-arr[i])*(x-arr[i]))
print(ans)