n = int(input())
l = list(map(int,input().split()))
l.sort()
res = 0
for i in range(n*2):
    if i%2==0:
        res += l[i]
print(res)