N, L = map(int, input().split())
A = list(map(int, input().split()))

start = -1
for i in range(N-1):
    if A[i] + A[i + 1] >= L:
        start = i
if start < 0:
    print("Impossible")
    exit()

ans = [start + 1]
for i in range(start + 1, N - 1):
    ans.append(i+1)
for i in reversed(range(start)):
    ans.append(i+1)

ans.reverse()
print("Possible")
print(*ans, sep="\n")