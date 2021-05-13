n = int(input())
li = list(map(int,input().split()))

x = int(sum(li)/len(li))
y = sum(li)/len(li)
if y-x > 0.5:
    x += 1

ans = 0

for i in li:
    ans += (i-x)**2

print(ans)