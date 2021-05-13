n = int(input())
l = list(map(int,input().split()))
l = sorted(l)
ans = 0
for i in range(len(l)):
    if i%2==0:
        ans += l[i]
print(ans)
