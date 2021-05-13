def resolve():
	n = int(input())
	a = list(map(int, input().split()))
	ans = float('inf')
	for i in range(-100, 101):
		tmp = 0
		for j in a:
			tmp += (j - i)**2
		ans = min(ans, tmp)
	print(ans)
resolve()