int1 = lambda x: int(x) - 1

N, M = map(int, input().split())

red = [True] + [False] * (N-1)
n_ball = [1] * N

for _ in range(M):
    x,y = map(int1, input().split())
    if red[x]:
        red[y] = True
        n_ball[x] -= 1
        n_ball[y] += 1
        if n_ball[x] == 0:
            red[x] = False
    else:
        n_ball[x] -= 1
        n_ball[y] += 1

print(sum(red))