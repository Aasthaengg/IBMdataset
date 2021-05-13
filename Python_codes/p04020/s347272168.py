n = int(input())
lis = [int(input()) for i in range(n)]

ans = 0
for i in range(n):
    temp, mod = divmod(lis[i], 2)
    ans += temp
    if i < n-1 and lis[i+1] != 0:
        lis[i+1] += mod

print(ans)