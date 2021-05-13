N, M = map(int, input().split())
c = [1] * N
r = [True] + [False] * (N-1)
for i in range(M):
    x, y = map(int, input().split())
    if r[x-1] == True:
        r[y-1] = True
    if c[x-1] == 1:
        r[x-1] = False
    c[x-1] -= 1
    c[y-1] += 1
print(sum(r))
