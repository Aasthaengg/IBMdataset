N, M = map(int, input().split())
kouho = {}
kouho[1]=True
Nlist = [1]*(N+1)
ans = 0
for i in range(M):
    x, y = map(int, input().split())
    if x in kouho:
        kouho[y] = True
        Nlist[x] -= 1
        Nlist[y] += 1
    else:
        Nlist[x] -= 1
        Nlist[y] += 1
    if Nlist[x]==0:
        if x in kouho:
            del kouho[x]

for i in range(1, N+1):
    if Nlist[i] == 0:
        continue
    if i in kouho:
        ans += 1

print(ans)
