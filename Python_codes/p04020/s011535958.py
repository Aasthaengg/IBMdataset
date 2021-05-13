N = int(input())

ans = 0
tmp = -10
for i in range(N):
    a = int(input())
    if tmp == i-1 and a > 0:
        ans += 1
        a -= 1
    ans += a//2
    if a%2 == 1:
        tmp = i
print(ans)