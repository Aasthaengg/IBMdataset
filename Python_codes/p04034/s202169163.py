def int_(num_str):
    return int(num_str) - 1

N, M = map(int, input().split())
balls = [1] * N
red = {0}
for i in range(M):
    x, y = map(int_, input().split())
    if x in red:
        if balls[x] == 1:
            red.remove(x)
            red.add(y)
        else:
            red.add(y)
    balls[x] -= 1
    balls[y] += 1
print(len(red))