N, L = map(int, input().split())
A = list(map(int, input().split()))

for i in range(1, N):
    if A[i-1] + A[i] >= L:
        X = i
        break
else:
    print("Impossible")
    exit()

ans = []
for i in range(1, X):
    ans.append(i)
for i in range(N-1, X, -1):
    ans.append(i)
ans.append(X)
print("Possible")
print(*ans, sep="\n")
