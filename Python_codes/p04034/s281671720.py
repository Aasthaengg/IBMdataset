n,m = map(int,input().split())
dic = {}
ls = [1]*(n+1)
ls[0] = 0
ans = 0
dic[1] = 1
for i in range(m):
    a,b = map(int,input().split())
    ls[a] -= 1
    ls[b] += 1
    if dic.get(a,0) != 0:
        if dic.get(b,0) == 0:
            dic[b] = 1
    else:
        if ls[b] == 1:
            dic[b] = 0
for j in range(n+1):
    if ls[j] > 0 and dic.get(j,0) != 0:
        ans += 1
print(ans)