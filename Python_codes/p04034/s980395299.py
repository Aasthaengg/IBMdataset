N, M = map(int,input().split())
B = [list(map(int,input().split())) for k in range(M)]
H = [1]*N
E = [0]*N
E[0] = 1
for e in B:
    x, y = e[0]-1, e[1]-1
    if E[x] == 1:
        if H[x] == 1:
            E[x] = 0
            E[y] = 1
        else:
            E[y] = 1
    H[x] -= 1
    H[y] += 1
print(E.count(1))
