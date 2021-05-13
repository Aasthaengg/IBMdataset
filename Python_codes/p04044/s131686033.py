N, L = map(int, input().split())
res = []
for i in range(N):
    S = input()
    res.append(S)

res.sort()

print(''.join(res))