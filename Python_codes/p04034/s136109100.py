n,m = map(int,input().split())
possible = [0]*n
kosuu = [1]*n
possible[0] = 1
L = []

for i in range(m):
    x,y = map(int,input().split())
    L.append((x,y))

for i in range(m):
    x,y = L[i][0],L[i][1]
    x,y = x-1,y-1
    if kosuu[x] >=2 and possible[x] == 1:
        possible[y] = 1
        kosuu[x] -=1
        kosuu[y] +=1
    elif kosuu[x] == 1 and possible[x] == 1:
        possible[x] = 0
        possible[y] = 1
        kosuu[x] = 0
        kosuu[y] +=1
    elif kosuu[x] >=2 and possible[x] == 0:
        kosuu[x] -=1
        kosuu[y] +=1
    elif kosuu[x] == 1 and possible[x] == 0:
        kosuu[x] = 0
        kosuu[y] +=1
print(sum(possible))