N, M = map(int, input().split())

R = [0 for _ in range(N+1)] # possibility to include the red ball
C = [1 for _ in range(N+1)] # number of balls
R[1] = 1


for i in range(M):
    x, y = map(int, input().split())
    if R[x] == 1:
        R[y] = 1
        if C[x] == 1:
            R[x] = 0
    C[x] -= 1
    C[y] += 1
#    print('R', R)
#    print('C', C)
print(R.count(1))