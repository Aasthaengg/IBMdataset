N = int(input())
L = sorted(list(map(int,input().split())))
ans = 0
for i in range(2*N):
    if i % 2 == 1:
        continue
    else:
        ans += L[i]
print(ans)
