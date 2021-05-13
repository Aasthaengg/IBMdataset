N, L = map(int, input().split())
S = [input() for i in range(N)]
S.sort()
S2 = []
for i in range(N):
    S2.append(S[i])
print(*(S2), sep='')