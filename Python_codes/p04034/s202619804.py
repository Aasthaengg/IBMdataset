n, m = map(int, input().split())
x_y = [list(map(int, input().split())) for _ in range(m)]

aka_list = [True]
for i in range(1, n):
    aka_list.append(False)
balls = [1] * n

for i in range(m):
    if aka_list[x_y[i][0] - 1]:
        aka_list[x_y[i][1]-1] = True
    balls[x_y[i][0] - 1] -= 1
    balls[x_y[i][1] - 1] += 1
    if balls[x_y[i][0] - 1] == 0:
        aka_list[x_y[i][0] - 1] = False

print(sum([1 for i in range(len(aka_list)) if aka_list[i]]))
