n, m = map(int, input().split())
C = [1]*n
P = [0]*n
P[0] = 1

for i in range(m):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    if P[x] != 0:
        if C[x] == 1:
            P[x] = 0
            C[x] -= 1
            P[y] = 1
            C[y] += 1
        else:
            C[x] -= 1
            P[y] = 1
            C[y] += 1
    else:
        C[x] -= 1
        C[y] += 1
    #print(i)
    #print(P)
    #print(C)
print(sum(P))
