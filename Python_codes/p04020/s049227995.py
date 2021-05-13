n = int(input())
ans = 0
nex = 0
for i in range(n):
    now = int(input())
    if nex == 1 and now > 0:
        now -= 1
        nex = 0
        ans += 1
    elif nex == 1 and now == 0:
        nex = 0 
    ans += now//2
    if now % 2 == 1:
        nex = 1
print(ans)