n,m = map(int,input().split())
canred = set()
canred.add(1)
balls = [1 for i in range(n)]
for i in range(m):
    x,y = map(int,input().split())
    if x in canred:
        canred.add(y)
    balls[x-1]-=1
    balls[y-1] += 1
    if balls[x-1] == 0:
        canred.discard(x)


print(len(canred))