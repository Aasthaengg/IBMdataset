N, L, *A = map(int, open(0).read().split())

k = -1
for i in range(N - 1):
    if A[i] + A[i + 1] >= L:
        k = i + 1
        break

if k == -1:
    print("Impossible")
else:
    print("Possible")
    for j in range(1, k):
        print(j)
    for j in reversed(range(k + 1, N)):
        print(j)
    print(k)