n,l=map(int,input().split())
li=[input() for _ in range(n)]
li.sort()
res=""
for i in range(n):
    res+=li[i]
print(res)