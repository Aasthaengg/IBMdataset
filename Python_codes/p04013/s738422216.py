from collections import Counter

N, A = map(int, input().split())
X = list(map(int, input().split()))

X2 = [0]*N

for i in range(N):
    X2[i] = X[i] - A

C = Counter([0, X2[0]])

for x in X2[1:]:
    C2 = Counter()
    for s, c in C.items():
        C2[s+x] += c
    C += C2

print(C[0]-1)
