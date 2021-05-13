n, m = map(int, input().split())

A = [1] * (n + 1)
red = [False] * (n + 1)
red[1] = True

for i in range(1, m + 1):
	x, y = map(int, input().split())
	if red[x]:
		red[y] = True
	A[x] -= 1
	A[y] += 1
	if A[x] == 0:
		red[x] = False

print(len([red[i] for i in range(1, n + 1) if red[i]]))