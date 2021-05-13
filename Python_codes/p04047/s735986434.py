n = int(input())
L = list(map(int, input().split()))

L = sorted(L, reverse=True)

cnt = 0
i = 0
while True:
	if i == 2*n:
		break
	cnt += min(L[i], L[i + 1])
	i += 2

print(cnt)