n = int(input())
a = list(int(input()) for i in range(n))
ans = 0
for i in range(n-1):
    m = a[i]//2
    ans += m
    a[i] -= m*2
    if a[i] == 1 and a[i+1] != 0:
        ans += 1
        a[i] -= 1
        a[i+1] -= 1
print(ans + a[-1]//2)