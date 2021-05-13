R = list()
L = list()
N = int(input())
R.append(0)
for i in range(N):
    k = int(input())
    L.append(k)
    if k == 0:
        R.append(len(L))
R.append(N)
S = sum(L)
for i in range(len(R) - 1):
    if sum(L[R[i] : R[i + 1]]) % 2 == 1:
        S = S - 1
print(S // 2)
