n = int(input())
l = list(map(int,input().split()))
l.sort()
ans = 0
for i in l[::2]:
    ans +=i
print(ans)