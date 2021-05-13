N, M = map(int, input().split())
box = [1] * N
red = [1]
red.extend([0] * (N - 1))

for i in range(M):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    
    if red[x] == 1:
        if box[x] == 1:
            red[x] = 0
        red[y] = 1
    
    box[x] -= 1
    box[y] += 1


print(sum(red))
