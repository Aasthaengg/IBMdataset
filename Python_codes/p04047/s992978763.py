n = int(input())
l = list(map(int,input().split()))

l.sort()
ans = 0
for i in range(n*2):
    if i%2 != 0:
        continue
    ans +=l[i]

print(ans)