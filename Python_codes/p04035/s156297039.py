# def makelist(n, m):
# 	return [[0 for i in range(m)] for j in range(n)]

yes = "Possible"
no = "Impossible"

N, L = map(int, input().split())
a = [0] + list(map(int, input().split()))

c = 0
Mi = -1
for i in range(1, N):
	if c < a[i] + a[i+1]:
		c = max(c, a[i] + a[i+1])
		Mi = i

if c < L:
	print(no)
else:
	print(yes)
	for i in range(1, N):
		if i != Mi:
			print(i)
		else:
			break
	for i in reversed(range(1, N)):
		if i != Mi:
			print(i)
		else:
			break
	print(Mi)
