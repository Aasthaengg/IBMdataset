n = int(input())
a = list(map(int, input().split()))

a.sort()
ans = 0
for i in range(2*n):
	if not i&1:
		ans += a[i]

print(ans)
