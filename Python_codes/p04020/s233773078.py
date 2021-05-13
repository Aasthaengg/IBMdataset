n = int(input())
a = [0]*n

for i in range(n):
    a[i] = int(input())
ans = 0
for i in range(n-1):
    if a[i] >= 2:
        ans += a[i]//2
        a[i] = a[i]%2
    if a[i] == 1 and a[i+1] >= 1:
        ans += 1
        a[i] -= 1
        a[i+1] -= 1
print(ans+a[-1]//2)
