n = int(input())
l = [int(i) for i in input().split()]
l.sort()
ans = 0
for i in range(n):
    ans += l[i*2]
print(ans)