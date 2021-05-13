N, M = map(int, input().split())

red = [0]*N
red[0] = 1

q = [1]*N

for _ in range(M):
    x, y = map(int, input().split())
    red[y-1] |= red[x-1]
    q[x-1] -= 1
    q[y-1] += 1
    if q[x-1] == 0:
        red[x-1] = 0

print(sum([1 for i in range(N) if q[i]>0 and red[i]]))