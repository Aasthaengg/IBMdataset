N = int(input())
A = [int(input()) for i in range(N)]

c = ans = 0
for a in A:
    if a==0:
        ans += c//2
        c = 0
    else:
        c += a
ans += c//2
print(ans)