n = int(input())
li = [int(x) for x in input().split()]
li.sort()
ans = 0
for i in range(0,2*n,2):
    ans += min(li[i],li[i+1])
print(ans)
