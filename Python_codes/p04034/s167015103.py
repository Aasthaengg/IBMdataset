def solve():
    N, M = map(int, input().split())
    
    num = []
    red = []
    for i in range(N+1):
        num.append(1)
        red.append(0)
    red[1] = 1
    
    for _ in range(M):
        x, y = map(int, input().split())
        if red[x] == 1:
            red[y] = 1
        num[x] -= 1
        num[y] += 1
        if num[x] == 0:
            red[x] = 0
    
    return sum(red)

print(solve())