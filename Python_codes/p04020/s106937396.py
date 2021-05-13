n = int(input())
a = [int(input()) for _ in range(n)]
ans = 0
for i in range(n):
	if a[i] >= 2:
		ans += a[i] // 2
		a[i] = a[i] % 2
	if i != n-1:
		if a[i] >= 1 and a[i+1] >= 1:
			k = min(a[i], a[i+1])
			ans += k
			a[i] -= k
			a[i+1] -= k
print(ans)