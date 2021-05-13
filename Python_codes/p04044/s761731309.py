N, L = [int(x) for x in input().split()]
S = []
for s in range(N):
    S.append(input())
print(''.join(sorted(S)))