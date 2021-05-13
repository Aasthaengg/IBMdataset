n,m = map(int,input().split())

check = [1]+[0]*n
numlis = [1]*(n+1)

for i in range(m):
    x, y = map(int, input().split())
    if numlis[x-1] > 1 and check[x-1] == 1:
        check[y-1] = 1
        numlis[x-1] -= 1
        numlis[y-1] += 1
    elif numlis[x-1] == 1 and check[x-1] == 1:
        check[y-1] = 1
        check[x-1] = 0
        numlis[x-1] -= 1
        numlis[y-1] += 1
    else:
        numlis[x-1] -= 1
        numlis[y-1] += 1
    

print(sum(check))