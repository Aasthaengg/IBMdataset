n, m = map(int, input().split())
red = [1] + [0] * (n - 1)
num = [1] * n
for i in range(m):
    x, y = map(int, input().split())
    if red[x - 1] == 1:
        red[y - 1] = 1
        if num[x - 1] == 1:
            red[x - 1] = 0
    num[x - 1] -= 1
    num[y - 1] += 1
    
print(sum(red))