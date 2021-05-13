n, m = map(int, input().split())
cl = [1 for _ in range(n)]
rl = [1]+[0 for _ in range(n-1)]

for i in range(m):
    x_n, y_n = map(int, input().split())
    cl[x_n-1] -= 1
    cl[y_n-1] += 1
    if rl[x_n-1] == 1 and cl[x_n-1]>0:
        rl[y_n-1] = 1
    elif rl[x_n-1] == 1 and cl[x_n-1] == 0:
        rl[x_n-1] = 0
        rl[y_n-1] = 1
    elif rl[x_n-1] == 0:
        pass
print(sum(rl))
