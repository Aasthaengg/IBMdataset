N, M, *xy = map(int, open(0).read().split())
boxes = [1] * N
is_red = [0] * N
is_red[0] = 1

for x, y in zip(*[iter(xy)] * 2):
    x -= 1
    y -= 1
    boxes[x] -= 1
    boxes[y] += 1
    if is_red[x]:
        if boxes[x] == 0:
            is_red[x] = 0
        is_red[y] = 1
print(sum(is_red))
