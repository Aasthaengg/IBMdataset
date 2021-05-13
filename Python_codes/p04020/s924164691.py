n = int(input())
ls = [0] * n
for i in range(n):
    a = int(input())
    ls[i] = a

ans = 0
for i in range(n-1):
    if ls[i] % 2 == 1 and ls[i+1] > 0:
        ls[i] += 1
        ls[i+1] -= 1
    ans += ls[i] // 2
ans += ls[-1] // 2
print(ans)
