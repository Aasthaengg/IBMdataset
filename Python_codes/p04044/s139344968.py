N, L = map(int, input().split())
A = []
for i in range(N):
	S = input()
	A.append(S)

A.sort()
for i in range(N-1):
	print(A[i], end="")
print(A[N-1])
